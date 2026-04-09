"""
deadline_reminder.py
--------------------
Runs on a schedule (cron) to check for missed submissions
and create GitHub Issues as reminders.
"""

import json
import os
import urllib.request
from datetime import datetime
from pathlib import Path

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
GITHUB_REPO = os.environ.get("GITHUB_REPOSITORY", "")
NOTEBOOKS_DIR = "notebooks"


def create_reminder_issue(title: str, body: str, label: str = "reminder"):
    if not GITHUB_TOKEN or not GITHUB_REPO:
        print(f"Reminder: {title}")
        return

    payload = json.dumps({
        "title": title,
        "body": body,
        "labels": [label]
    }).encode("utf-8")

    req = urllib.request.Request(
        f"https://api.github.com/repos/{GITHUB_REPO}/issues",
        data=payload,
        headers={
            "Authorization": f"token {GITHUB_TOKEN}",
            "Content-Type": "application/json",
            "Accept": "application/vnd.github.v3+json"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req) as resp:
            issue = json.loads(resp.read().decode("utf-8"))
            print(f"Reminder issue created: {issue.get('html_url', '')}")
    except Exception as e:
        print(f"Failed to create reminder: {e}")


def get_latest_day() -> int:
    """Find the highest day notebook submitted so far."""
    notebooks = Path(NOTEBOOKS_DIR)
    if not notebooks.exists():
        return 0

    max_day = 0
    for folder in notebooks.iterdir():
        if folder.is_dir() and folder.name.startswith("day_"):
            try:
                day_num = int(folder.name.split("_")[1])
                nb = folder / f"day_{day_num}.ipynb"
                if nb.exists():
                    max_day = max(max_day, day_num)
            except (ValueError, IndexError):
                pass
    return max_day


def main():
    now = datetime.now()
    hour = now.hour
    weekday = now.weekday()  # 0=Mon, 6=Sun
    day_name = now.strftime("%A")
    latest_day = get_latest_day()

    print(f"Scheduled check at {now.strftime('%H:%M')} on {day_name}")
    print(f"Latest submitted day: {latest_day}")

    # ── Weekend reminder ─────────────────────────────
    if weekday == 5:  # Saturday
        create_reminder_issue(
            title=f"🌅 Weekend Mode — Day {latest_day + 1} lighter schedule",
            body=f"""## Weekend Check-in 🌅

It's Saturday! You're on a lighter schedule today.

**Current progress:** Day {latest_day} complete

**Weekend task (pick at least one):**
- [ ] Review your weakest topic from this week
- [ ] Complete any pending HW from the week
- [ ] Watch 1–2 optional revision videos
- [ ] Practice 2–3 SQL questions on [LeetCode](https://leetcode.com/studyplan/top-sql-50/)

**No pressure — but consistency beats perfection 💪**
""",
            label="weekend"
        )
        return

    if weekday == 6:  # Sunday
        create_reminder_issue(
            title=f"☀️ Sunday — Rest + Light Prep for Week ahead",
            body=f"""## Sunday Check-in ☀️

Rest day! But if you have energy:

**Optional:**
- [ ] Read your notes from the past week (20 mins max)
- [ ] Prep your Day {latest_day + 1} notebook structure
- [ ] Watch 1 video if feeling motivated

**Tomorrow:** Day {latest_day + 1} starts. Videos by 10:30 PM, HW by 5 PM next day.

Stay consistent! 🚀
""",
            label="weekend"
        )
        return

    # ── Weekday 10:30 PM check (videos deadline) ─────
    if hour >= 17 and hour < 20:  # 10:30 PM IST = ~17:00 UTC
        expected_day = latest_day + 1
        nb_path = Path(f"{NOTEBOOKS_DIR}/day_{expected_day}/day_{expected_day}.ipynb")

        if not nb_path.exists():
            create_reminder_issue(
                title=f"🔔 Reminder — Day {expected_day} videos due by 10:30 PM tonight!",
                body=f"""## ⏰ Video Deadline Reminder

**It's almost 10:30 PM!** Have you watched today's videos?

**Day {expected_day} videos should be:**
- Watched ✅
- Code written in `notebooks/day_{expected_day}/day_{expected_day}.ipynb`
- Practice Questions (PQ) attempted

**If you haven't started:** Start now — even 30 mins is better than nothing.

**Deadline:** 10:30 PM tonight for videos + PQ
**Next deadline:** 5:00 PM tomorrow for HW

Push your notebook when done! 🚀
""",
                label="deadline-reminder"
            )
        else:
            print(f"Day {expected_day} notebook exists — no reminder needed")

    # ── Next day 5 PM check (HW deadline) ────────────
    elif hour >= 11 and hour < 13:  # 5 PM IST = ~11:30 UTC
        expected_day = latest_day
        nb_path = Path(f"{NOTEBOOKS_DIR}/day_{expected_day}/day_{expected_day}.ipynb")

        if nb_path.exists():
            # Check if HW seems complete (basic check - file size > 5KB suggests content)
            size_kb = nb_path.stat().st_size / 1024
            if size_kb < 5:
                create_reminder_issue(
                    title=f"⚠️ Day {expected_day} HW due by 5 PM today — notebook looks incomplete!",
                    body=f"""## ⚠️ HW Deadline Reminder

**It's approaching 5 PM!** Your Day {expected_day} homework should be complete.

Your notebook `day_{expected_day}.ipynb` looks like it might be incomplete (small file size).

**Check:**
- [ ] All 5 HW questions answered
- [ ] Code runs without errors  
- [ ] SQL answers written (if SQL day)
- [ ] Time spent logged

**Push your notebook NOW if you haven't!** ⏰

After pushing, the bot will automatically:
- Score your answers
- Update your checklist
- Inject Day {expected_day + 1} questions
""",
                    label="deadline-reminder"
                )
        else:
            create_reminder_issue(
                title=f"❌ Day {expected_day} notebook not found — HW deadline is 5 PM!",
                body=f"""## ❌ Missing Notebook

No notebook found for Day {expected_day}.

**Expected path:** `notebooks/day_{expected_day}/day_{expected_day}.ipynb`

Please create your notebook and push it ASAP. HW deadline is 5 PM today.

If you need the questions again, check your `Month1_Final_Checklist.md`.
""",
                label="missed-deadline"
            )


if __name__ == "__main__":
    main()
