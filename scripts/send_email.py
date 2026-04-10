"""
send_email.py (v4 - DEBUGGED)

Sends email via Gmail SMTP using an App Password.

Required GitHub Secrets:
GMAIL_USER     — your Gmail address (e.g. sahuchandrasekhar4@gmail.com)
GMAIL_APP_PASS — 16-char App Password from myaccount.google.com/apppasswords
NOTIFY_EMAIL   — recipient email
"""

import os
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

GMAIL_USER  = os.environ.get("GMAIL_USER", "")
GMAIL_PASS  = os.environ.get("GMAIL_APP_PASS", "")
NOTIFY_TO   = os.environ.get("NOTIFY_EMAIL", "sahuchandrasekhar4@gmail.com")

def send_email(subject: str, body_html: str, body_text: str = "") -> bool:
    """
    Send an email via Gmail SMTP.
    Returns True on success, False on failure.
    """
    if not GMAIL_USER or not GMAIL_PASS:
        print(f"  ⚠️  Gmail credentials not set — skipping email")
        print(f"  Subject: {subject}")
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"]    = f"Study Bot <{GMAIL_USER}>"
    msg["To"]      = NOTIFY_TO

    # Plain text fallback
    if not body_text:
        body_text = re.sub(r"<[^>]+>", "", body_html)
        body_text = body_text.replace("&nbsp;", " ").strip()

    msg.attach(MIMEText(body_text, "plain"))
    msg.attach(MIMEText(body_html, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_USER, GMAIL_PASS)
            server.sendmail(GMAIL_USER, NOTIFY_TO, msg.as_string())
        print(f"  ✅ Email sent: {subject}")
        return True
    except Exception as e:
        print(f"  ❌ Email failed: {e}")
        return False

def email_day_result(day: int, scores: dict, content: dict, passed: bool, next_day_created: bool):
    """Send Day X result email with score + next day info."""
    pct = round((scores["total"] / scores["max_total"]) * 100) if scores["max_total"] > 0 else 0
    next_day = day + 1

    status_color  = "#22c55e" if passed else "#ef4444"
    status_text   = "PASSED ✅" if passed else "NOT PASSED ❌"
    grade_emoji   = "🏆" if pct >= 80 else "👍" if pct >= 70 else "⚠️"

    # Build per-question rows
    def rows(section_dict, label):
        html = ""
        for i, s in section_dict.items():
            e = "✅" if s["score"] == 2 else "⚠️" if s["score"] == 1 else "❌"
            html += f"<tr><td style='padding:4px 8px'>{e} {label}{i}</td><td style='padding:4px 8px;text-align:center'><b>{s['score']}/2</b></td><td style='padding:4px 8px;color:#555'>{s['feedback']}</td></tr>"
        return html

    pq_rows  = rows(scores["pq"],  "PQ")
    hw_rows  = rows(scores["hw"],  "HW")
    sql_rows = rows(scores["sql"], "SQL") if scores["sql"] else ""

    sql_section = f"""
<h3 style='color:#6366f1'>🗄️ SQL</h3>
<table style='border-collapse:collapse;width:100%'>
  <tr style='background:#f1f5f9'><th style='padding:4px 8px;text-align:left'>Question</th><th style='padding:4px 8px'>Score</th><th style='padding:4px 8px;text-align:left'>Feedback</th></tr>
  {sql_rows}
</table>""" if sql_rows else ""

    next_day_block = ""
    if passed and next_day_created:
        next_day_block = f"""
<div style='background:#f0fdf4;border-left:4px solid #22c55e;padding:12px 16px;margin-top:16px;border-radius:4px'>
  <b>🎉 Day {next_day} notebook is ready in your repo!</b><br>
  Open <code>notebooks/day_{next_day}/day_{next_day}.ipynb</code> and start today.
  <br><br>
  <b>⏰ Deadlines for Day {next_day}:</b><br>
  Videos + PQ → tonight by <b>10:30 PM</b><br>
  HW → tomorrow by <b>5:00 PM</b>
</div>"""
    elif not passed:
        next_day_block = f"""
<div style='background:#fef2f2;border-left:4px solid #ef4444;padding:12px 16px;margin-top:16px;border-radius:4px'>
  <b>❌ Day {next_day} is locked.</b><br>
  You need ≥70% AND all HW answered to unlock it.<br><br>
  <b>What to do:</b>
  <ol>
    <li>Fix the ❌ answers in your notebook</li>
    <li>Make sure all HW cells have real code</li>
    <li>Push to GitHub — bot re-scores at 5 PM IST</li>
  </ol>
</div>"""

    time_row = f"<tr><td>⏱️ Time Spent</td><td><b>{content.get('time_spent', '—')} mins</b></td></tr>" if content.get("time_spent") else ""

    body_html = f"""<!DOCTYPE html>
<html>
<body style='font-family:sans-serif;max-width:640px;margin:0 auto;color:#1e293b'>
  <div style='background:#1e293b;color:white;padding:20px 24px;border-radius:8px 8px 0 0'>
    <h2 style='margin:0'>📓 Day {day} Results — Big Data Engineering</h2>
    <p style='margin:4px 0 0;opacity:0.7'>Auto-scored at 5 PM IST</p>
  </div>

  <div style='padding:20px 24px;border:1px solid #e2e8f0;border-top:none'>

<table style='width:100%;margin-bottom:16px'>
  <tr><td>📊 Score</td><td><b style='font-size:1.2em'>{scores["total"]}/{scores["max_total"]} ({pct}%)</b></td></tr>
  <tr><td>🏁 Status</td><td><b style='color:{status_color}'>{status_text}</b></td></tr>
  {time_row}
  <tr><td>{grade_emoji} Grade</td><td>{"Excellent" if pct >= 80 else "Good — review ❌ items" if pct >= 70 else "Needs improvement"}</td></tr>
</table>

<h3 style='color:#3b82f6'>💡 Practice Questions</h3>
<table style='border-collapse:collapse;width:100%'>
  <tr style='background:#f1f5f9'><th style='padding:4px 8px;text-align:left'>Question</th><th style='padding:4px 8px'>Score</th><th style='padding:4px 8px;text-align:left'>Feedback</th></tr>
  {pq_rows}
</table>

<h3 style='color:#f59e0b'>📝 Homework</h3>
<table style='border-collapse:collapse;width:100%'>
  <tr style='background:#f1f5f9'><th style='padding:4px 8px;text-align:left'>Question</th><th style='padding:4px 8px'>Score</th><th style='padding:4px 8px;text-align:left'>Feedback</th></tr>
  {hw_rows}
</table>

{sql_section}
{next_day_block}

  </div>

  <div style='background:#f8fafc;padding:12px 24px;border:1px solid #e2e8f0;border-top:none;border-radius:0 0 8px 8px;font-size:0.85em;color:#64748b'>
    🤖 Sent by Study-Bot · Big Data Engineering Tracker
  </div>
</body>
</html>"""

    subject = f"{'✅' if passed else '❌'} Day {day} — {scores['total']}/{scores['max_total']} ({pct}%) | {'Day ' + str(next_day) + ' ready!' if passed else 'Fix and re-push'}"
    send_email(subject, body_html)

def email_reminder(subject: str, heading: str, body_points: list, color: str = "#3b82f6"):
    """Send a generic reminder email."""
    items_html = "".join(f"<li style='margin:6px 0'>{p}</li>" for p in body_points)
    body_html = f"""<!DOCTYPE html>
<html>
<body style='font-family:sans-serif;max-width:640px;margin:0 auto;color:#1e293b'>
  <div style='background:{color};color:white;padding:20px 24px;border-radius:8px 8px 0 0'>
    <h2 style='margin:0'>{heading}</h2>
  </div>
  <div style='padding:20px 24px;border:1px solid #e2e8f0;border-top:none'>
    <ul style='padding-left:20px'>
      {items_html}
    </ul>
  </div>
  <div style='background:#f8fafc;padding:12px 24px;border:1px solid #e2e8f0;border-top:none;border-radius:0 0 8px 8px;font-size:0.85em;color:#64748b'>
    🤖 Sent by Study-Bot · Big Data Engineering Tracker
  </div>
</body>
</html>"""
    send_email(subject, body_html)

def email_test_warning(test_day: int, prev_day: int):
    """Send test day advance warning."""
    body_html = f"""<!DOCTYPE html>
<html>
<body style='font-family:sans-serif;max-width:640px;margin:0 auto;color:#1e293b'>
  <div style='background:#7c3aed;color:white;padding:20px 24px;border-radius:8px 8px 0 0'>
    <h2 style='margin:0'>🧪 Day {test_day} is a TEST DAY tomorrow!</h2>
  </div>
  <div style='padding:20px 24px;border:1px solid #e2e8f0;border-top:none'>
    <p><b>Rules:</b></p>
    <ul>
      <li>No notes allowed during the test</li>
      <li>45–75 minutes max</li>
      <li>Need ≥ 60% to move on</li>
    </ul>
    <p><b>What to review tonight:</b></p>
    <ul>
      <li>All PQ answers from Day {max(1, test_day - 10)} to Day {prev_day}</li>
      <li>Any ❌ items from your GitHub Issues or previous emails</li>
      <li>SQL topics covered so far</li>
    </ul>
    <div style='background:#faf5ff;border-left:4px solid #7c3aed;padding:12px 16px;border-radius:4px;margin-top:16px'>
      Open your checklist, make sure all items are ticked. Good luck! 🎯
    </div>
  </div>
  <div style='background:#f8fafc;padding:12px 24px;border:1px solid #e2e8f0;border-top:none;border-radius:0 0 8px 8px;font-size:0.85em;color:#64748b'>
    🤖 Sent by Study-Bot · Big Data Engineering Tracker
  </div>
</body>
</html>"""
    send_email(f"🧪 HEADS UP — Day {test_day} Test Day tomorrow! Review tonight", body_html)
