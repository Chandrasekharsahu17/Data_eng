## “””
create_day_notebook.py  (v3)

Manual fallback only. Auto-creation is handled by analyse_notebook.py.
Use this ONLY if you need to regenerate or create a notebook manually.

Usage: python scripts/create_day_notebook.py <day_number>
“””

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(**file**).parent))
from analyse_notebook import DAILY_QUESTIONS, NOTEBOOKS_DIR, mk_md, mk_code

def create_notebook(day: int):
out = Path(NOTEBOOKS_DIR) / f”day_{day}”
nb  = out / f”day_{day}.ipynb”

```
if nb.exists():
    print(f"⚠️  {nb} already exists. Delete it first to regenerate.")
    return

out.mkdir(parents=True, exist_ok=True)
d = DAILY_QUESTIONS.get(day, {})
cells = []

cells.append(mk_md(f"# 📓 Day {day} — Big Data Engineering\n> **Date:** <!-- fill -->\n> **Time Started:** <!-- fill -->\n"))
vids = "\n".join(f"- [ ] {v}" for v in d.get("videos", [])) or "- [ ] <!-- video -->"
cells.append(mk_md(f"## Videos\nMark each `[x]` when done.\n\n{vids}"))
cells.append(mk_code("# Video notes\n"))

cells.append(mk_md("## Practice Questions (PQ)\nAnswer in the code cell below each question."))
for i, q in enumerate(d.get("pq", []), 1):
    cells.append(mk_md(f"### PQ{i}\n{q}"))
    cells.append(mk_code(f"# PQ{i} answer\n"))

cells.append(mk_md("## Homework (HW)\nComplete by 5 PM next day."))
for i, q in enumerate(d.get("hw", []), 1):
    cells.append(mk_md(f"### HW{i}\n{q}"))
    cells.append(mk_code(f"# HW{i} answer\n"))

if d.get("sql"):
    cells.append(mk_md(f"## SQL\nTopic: {d.get('sql_topic','')}"))
    for i, q in enumerate(d["sql"], 1):
        cells.append(mk_md(f"### SQL{i}\n{q}"))
        cells.append(mk_code(f'sql_answer_{i} = """\n-- SQL{i} answer\n"""\nprint(sql_answer_{i})'))

cells.append(mk_md("## Notes")); cells.append(mk_code("# notes\n"))
cells.append(mk_md("## ⏱️ Time Tracking"))
cells.append(mk_code("time_spent = 0  # minutes\nprint(f'Time spent: {time_spent} mins')\n"))
sql_line = "- [ ] SQL done\n" if d.get("sql") else ""
cells.append(mk_md(
    f"## ✅ Day {day} Wrap-up\n- [ ] Videos watched\n- [ ] PQ answered\n"
    f"- [ ] HW done by 5 PM\n{sql_line}- [ ] Notebook pushed\n"
))

with open(nb, "w", encoding="utf-8") as f:
    json.dump({
        "nbformat": 4, "nbformat_minor": 5,
        "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                     "language_info": {"name": "python", "version": "3.11.0"}},
        "cells": cells
    }, f, indent=2)

print(f"✅ Created: {nb}")
print("   Open in Jupyter / VS Code and start!")
```

if **name** == “**main**”:
if len(sys.argv) < 2:
print(“Usage: python scripts/create_day_notebook.py <day_number>”)
sys.exit(1)
create_notebook(int(sys.argv[1]))