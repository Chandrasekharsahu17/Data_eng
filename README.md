# 🚀 Big Data Engineering — Automated Study Tracker

> Auto-analyses your daily notebooks, scores answers, updates your checklist, and reminds you of deadlines.

---

## ⚙️ How It Works

```
You push day_X.ipynb
        ↓
GitHub Action triggers
        ↓
Analyses your notebook
        ↓
Scores PQ + HW + SQL using Claude API
        ↓
Updates Month1_Final_Checklist.md with scores
        ↓
Injects next day's questions into MD
        ↓
Creates GitHub Issue as summary + reminder
        ↓
Commits updated MD back to your repo
```

**Scheduled reminders:**
- 🔔 **10:30 PM daily** — reminds you to finish videos + PQ
- ⏰ **5:00 PM next day** — reminds you to submit HW
- 🌅 **Saturday 10 AM** — lighter weekend check-in
- ☀️ **Sunday** — rest day reminder

---

## 📁 Repo Structure

```
your-repo/
├── .github/
│   └── workflows/
│       └── analyse_notebook.yml     ← GitHub Actions workflow
├── notebooks/
│   ├── day_1/
│   │   └── day_1.ipynb              ← Your Day 1 notebook
│   ├── day_2/
│   │   └── day_2.ipynb
│   └── ...
├── scripts/
│   ├── analyse_notebook.py          ← Main analyser
│   ├── deadline_reminder.py         ← Scheduled reminder
│   └── create_day_notebook.py       ← Notebook generator
├── Month1_Final_Checklist.md        ← Your tracker (auto-updated)
└── README.md
```

---

## 🛠️ Setup (One Time — 10 minutes)

### Step 1 — Create your GitHub repo
```bash
# Create a new repo on GitHub, then clone it
git clone https://github.com/YOUR_USERNAME/bigdata-study
cd bigdata-study
```

### Step 2 — Copy these files into your repo
Copy the entire folder structure from this project into your repo root.

### Step 3 — Add Secrets to GitHub
Go to your repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

Add these two secrets:

| Secret Name | Value |
|---|---|
| `ANTHROPIC_API_KEY` | Your Anthropic API key from [console.anthropic.com](https://console.anthropic.com) |
| `GITHUB_TOKEN` | Already auto-available in GitHub Actions — no need to add manually |

> **Where to get Anthropic API key:**
> Go to [console.anthropic.com](https://console.anthropic.com) → API Keys → Create Key

### Step 4 — Push your checklist MD
Make sure `Month1_Final_Checklist.md` is in your repo root.
```bash
cp /path/to/Month1_Final_Checklist.md .
git add .
git commit -m "Initial setup"
git push
```

### Step 5 — Create GitHub Issue Labels
Go to your repo → **Issues** → **Labels** → Create these labels:
- `completed` (green)
- `needs-review` (yellow)
- `missed-deadline` (red)
- `reminder` (blue)
- `weekend` (purple)

---

## 📓 Daily Workflow

### Every day:

**1. Generate your notebook (optional but saves time):**
```bash
python scripts/create_day_notebook.py 2
```
This creates `notebooks/day_2/day_2.ipynb` pre-filled with the day's structure.

**2. Watch videos, write code, answer questions in the notebook**

**3. Push to GitHub by 10:30 PM (videos + PQ done):**
```bash
git add notebooks/day_2/
git commit -m "Day 2 - videos and PQ complete"
git push
```

**4. GitHub Action automatically:**
- Detects the new notebook
- Scores your answers
- Updates your checklist MD with scores
- Injects Day 3 questions
- Creates a GitHub Issue with your results

**5. Complete HW by 5 PM next day, then push again:**
```bash
git add notebooks/day_2/
git commit -m "Day 2 - HW complete"
git push
```

---

## 📓 Notebook Structure

Each notebook should follow this structure for the analyser to work:

```
## Videos
- [x] #29 Python Filter Function  ← mark [x] when done

## Practice Questions (PQ)
### PQ1
[your answer here]

### PQ2
[your answer here]

## Homework (HW)
### HW1
[your answer here]

## SQL (if SQL day)
### SQL1
[your SQL answer here]

## Notes
[any notes]

# Time spent: 90 mins  ← include this line
```

---

## 🔧 Manual Trigger

You can manually trigger the analyser for any day:
1. Go to your repo → **Actions** → **Daily Notebook Analyser**
2. Click **Run workflow**
3. Enter the day number
4. Click **Run workflow**

---

## 📊 What Gets Updated Automatically

In `Month1_Final_Checklist.md`:
- ✅ Score block added after the day's section
- 📬 Next day's questions injected
- 🏆 Grade and feedback for each answer

In GitHub Issues:
- Summary of the day's score
- Per-question feedback
- Deadline warnings if missed

---

## ⚠️ Troubleshooting

**Action not triggering?**
- Make sure your notebook is in `notebooks/day_X/day_X.ipynb` exactly
- Check Actions tab for error logs

**Scoring seems wrong?**
- Make sure answers are in separate cells labelled `PQ1`, `HW1`, `SQL1` etc.
- The analyser looks for `PQ`, `HW`, `SQL` section headers

**API key error?**
- Double check the secret name is exactly `ANTHROPIC_API_KEY`
- Make sure the key is active at console.anthropic.com

---

*🤖 Bot commits are made by `Study-Bot` — don't be confused when you see auto-commits in your repo!*
