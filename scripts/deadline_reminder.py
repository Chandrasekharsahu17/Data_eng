"""
deadline_reminder.py (v4 - DEBUGGED)

Sends reminders via GitHub Issue AND email.

Cron triggers (UTC):
17:00 weekdays  = 10:30 PM IST  — videos + PQ check
11:30 weekdays  =  5:00 PM IST  — HW check + auto-trigger scoring
04:30 Saturday  = 10:00 AM IST  — weekend lighter mode
04:30 Sunday    = 10:00 AM IST  — rest day
"""

import json
import os
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

GITHUB_TOKEN  = os.environ.get("GITHUB_TOKEN", "")
GITHUB_REPO   = os.environ.get("GITHUB_REPOSITORY", "")
NOTEBOOKS_DIR = "notebooks"
TEST_DAYS     = {10, 20, 30}

def post_issue(title: str, body: str, label: str = "reminder"):
    """Post a GitHub issue."""
    if not GITHUB_TOKEN or not GITHUB_REPO:
        print(f"[REMINDER] {title}")
        return
    
    payload = json.dumps({"title": title, "body": body, "labels": [label]}).encode()
    req = urllib.request.Request(
        f"https://api.github.com/repos/{GITHUB_REPO}/issues", data=payload,
        headers={"Authorization": f"token {GITHUB_TOKEN}", "Content-Type": "application/json",
                 "Accept": "application/vnd.github.v3+json"}, method="POST")
    try:
        with urllib.request.urlopen(req) as r:
            issue = json.loads(r.read())
            print(f"Issue: {issue.get('html_url','')}")
    except Exception as e:
        print(f"Issue failed: {e}")

def send_email(subject, heading, points, color="#3b82f6"):
    """Send email via send_email module."""
    try:
        from send_email import email_reminder
        email_reminder(subject, heading, points, color)
    except Exception as e:
        print(f"Email skipped: {e}")

def get_latest_day() -> int:
    """Find the latest day with a notebook."""
    nb = Path(NOTEBOOKS_DIR)
    if not nb.exists():
        return 0
    max_day = 0
    for folder in nb.iterdir():
        if folder.is_dir() and folder.name.startswith("day_"):
            try:
                n = int(folder.name.split("_")[1])
                if (folder / f"day_{n}.ipynb").exists():
                    max_day = max(max_day, n)
            except (ValueError, IndexError):
                pass
    return max_day

def nb_size_ok(day: int) -> bool:
    """Check if notebook is substantial (>8KB)."""
    p = Path(f"{NOTEBOOKS_DIR}/day_{day}/day_{day}.ipynb")
    return p.exists() and p.stat().st_size > 8192

def main():
    """Main reminder logic."""
    now     = datetime.now()
    hour    = now.hour
    weekday = now.weekday()
    latest  = get_latest_day()
    nxt     = latest + 1
    print(f"Scheduled check — {now.strftime('%H:%M')} | Latest day: {latest}")

    # ── Saturday ─────────────────────────────────────────────────
    if weekday == 5:
        pts = [f"Progress: Day {latest} complete ✅",
               "Review your weakest topic from this week",
               "Practice 2–3 SQL on LeetCode SQL 50",
               f"Day {nxt} videos + PQ due tonight 10:30 PM"]
        post_issue(f"🌅 Weekend — Day {nxt} lighter schedule", "\n".join(f"- {p}" for p in pts), "weekend")
        send_email(f"🌅 Weekend Check-in", f"🌅 Weekend Mode — Day {nxt}", pts, "#8b5cf6")
        return

    # ── Sunday ────────────────────────────────────────────────────
    if weekday == 6:
        pts = ["Rest day — recharge!", f"Skim notes from this week",
               f"Open day_{nxt} notebook if it exists and read the questions",
               f"Tomorrow: Day {nxt} — Videos by 10:30 PM, HW by 5 PM next day"]
        post_issue(f"☀️ Sunday — Rest + Prep for Day {nxt}", "\n".join(f"- {p}" for p in pts), "weekend")
        send_email(f"☀️ Sunday Rest Day", f"☀️ Sunday — Rest + Prep", pts, "#8b5cf6")
        return

    # ── Test day advance warning ────���─────────────────────────────
    if nxt in TEST_DAYS:
        pts = [f"Day {nxt} is a TEST DAY — no notes allowed during test",
               "45–75 minutes max",
               f"Review PQ from Day {max(1,nxt-10)} to Day {latest}",
               "Check all ❌ items from your GitHub Issues",
               "Need ≥60% to pass and move on"]
        post_issue(f"🧪 HEADS UP — Day {nxt} TEST DAY tomorrow!", "\n".join(f"- {p}" for p in pts), "reminder")
        try:
            from send_email import email_test_warning
            email_test_warning(nxt, latest)
        except Exception as e:
            print(f"Test email failed: {e}")

    # ── 10:30 PM IST check (17:00 UTC) ───────────────────────────
    if 17 <= hour < 19:
        nb_exists = Path(f"{NOTEBOOKS_DIR}/day_{nxt}/day_{nxt}.ipynb").exists()
        if not nb_exists:
            pts = [f"notebooks/day_{nxt}/day_{nxt}.ipynb doesn't exist yet",
                   f"Day {latest} was probably not passed (score <70% or incomplete HW)",
                   f"Fix Day {latest} and re-push — bot re-scores at 5 PM IST",
                   "Or run the workflow manually from the Actions tab"]
            post_issue(f"🔔 10:30 PM — Day {nxt} notebook not found!", "\n".join(f"- {p}" for p in pts), "missed-deadline")
            send_email(f"🔔 10:30 PM — Day {nxt} missing!", "⏰ Video + PQ Deadline", pts, "#ef4444")
        elif not nb_size_ok(nxt):
            pts = ["Day notebook exists but looks thin",
                   "Mark all videos as [x] when done",
                   "Answer all 5 PQ with real code",
                   "Push to GitHub — scoring runs at 5 PM IST tomorrow",
                   "HW is due tomorrow by 5 PM IST"]
            post_issue(f"🔔 10:30 PM — Day {nxt} looks incomplete", "\n".join(f"- {p}" for p in pts), "deadline-reminder")
            send_email(f"🔔 10:30 PM Reminder — Day {nxt}", "⏰ Tonight's Deadline", pts, "#f59e0b")
        else:
            print(f"Day {nxt} notebook looks good — no reminder needed")

    # ── 5:00 PM IST check (11:30 UTC) — score if complete ────────
    elif 11 <= hour < 13:
        nb_path = Path(f"{NOTEBOOKS_DIR}/day_{latest}/day_{latest}.ipynb")
        if not nb_path.exists():
            pts = [f"Expected: notebooks/day_{latest}/day_{latest}.ipynb",
                   "Push your notebook now — even partial",
                   "Bot will score whatever is there"]
            post_issue(f"⚠️ 5 PM — Day {latest} notebook missing!", "\n".join(f"- {p}" for p in pts), "missed-deadline")
            send_email(f"⚠️ 5 PM — Day {latest} missing!", "⏰ HW Deadline", pts, "#ef4444")
        elif not nb_size_ok(latest):
            pts = [f"Day {latest} notebook looks thin",
                   "Make sure all 5 HW questions have real code answers",
                   "Add SQL if it's a SQL day",
                   "Log your time_spent",
                   "Push now — scoring will run automatically"]
            post_issue(f"⚠️ 5 PM — Day {latest} HW looks incomplete!", "\n".join(f"- {p}" for p in pts), "deadline-reminder")
            send_email(f"⚠️ 5 PM HW Deadline — Day {latest}", "⏰ HW Deadline", pts, "#ef4444")
        else:
            print(f"Day {latest} looks complete — triggering scorer...")
            os.execv(sys.executable, [sys.executable, "scripts/analyse_notebook.py", str(latest)])
    else:
        print(f"No action at hour {hour}")

if __name__ == "__main__":
    main()
