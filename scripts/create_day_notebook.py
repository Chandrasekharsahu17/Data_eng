"""
create_day_notebook.py
----------------------
Run this script to auto-generate a fresh notebook for any day.
Usage: python scripts/create_day_notebook.py 2

It creates: notebooks/day_2/day_2.ipynb
Pre-filled with the day's structure, video list, and question placeholders.
"""

import json
import sys
import os
from pathlib import Path

# Import questions bank from analyser
sys.path.insert(0, str(Path(__file__).parent))
from analyse_notebook import DAILY_QUESTIONS


def make_markdown_cell(source: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": source
    }


def make_code_cell(source: str = "") -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source
    }


def create_notebook(day: int) -> dict:
    day_data = DAILY_QUESTIONS.get(day, {})
    videos = day_data.get("videos", [])
    pq_questions = day_data.get("pq", [])
    hw_questions = day_data.get("hw", [])
    sql_questions = day_data.get("sql", [])
    sql_topic = day_data.get("sql_topic", "")

    cells = []

    # ── Title ─────────────────────────────────────────
    cells.append(make_markdown_cell(
        f"# 📓 Day {day} — Big Data Engineering\n"
        f"> **Date:** <!-- fill in date -->\n"
        f"> **Time Started:** <!-- fill in -->\n"
    ))

    # ── Videos ────────────────────────────────────────
    video_list = "\n".join([f"- [ ] {v}" for v in videos]) if videos else "- [ ] <!-- video name -->"
    cells.append(make_markdown_cell(
        f"## 📹 Videos\n"
        f"Mark each video as `[x]` when done.\n\n"
        f"{video_list}"
    ))

    cells.append(make_code_cell(
        f"# Video notes — write key concepts here as you watch\n"
        f"# Example:\n"
        f"# filter() - like WHERE in SQL, keeps elements matching a condition\n"
    ))

    # ── Practice Questions ────────────────────────────
    cells.append(make_markdown_cell("## 💡 Practice Questions (PQ)\nAnswer each question below its cell."))

    for i, q in enumerate(pq_questions, 1):
        cells.append(make_markdown_cell(f"### PQ{i}\n{q}"))
        cells.append(make_code_cell(f"# PQ{i} answer\n"))

    # ── Homework ──────────────────────────────────────
    cells.append(make_markdown_cell("## 📝 Homework (HW)\nComplete by 5 PM next day."))

    for i, q in enumerate(hw_questions, 1):
        cells.append(make_markdown_cell(f"### HW{i}\n{q}"))
        cells.append(make_code_cell(f"# HW{i} answer\n"))

    # ── SQL ───────────────────────────────────────────
    if sql_questions:
        cells.append(make_markdown_cell(f"## 🗄️ SQL — {sql_topic}"))
        for i, q in enumerate(sql_questions, 1):
            cells.append(make_markdown_cell(f"### SQL{i}\n{q}"))
            cells.append(make_code_cell(
                f"# SQL{i} answer\n"
                f"# Write your SQL query as a string or use %%sql magic if available\n\n"
                f'sql_answer_{i} = """\n'
                f"-- Your SQL here\n"
                f'"""\n'
                f"print(sql_answer_{i})"
            ))

    # ── Notes ─────────────────────────────────────────
    cells.append(make_markdown_cell("## 📓 Notes\nWrite anything you want to remember from today."))
    cells.append(make_code_cell(
        "# notes = \"\"\"\n"
        "# Key concepts from today:\n"
        "# 1. \n"
        "# 2. \n"
        "# 3. \n"
        "# \"\"\"\n"
    ))

    # ── Time tracking ─────────────────────────────────
    cells.append(make_markdown_cell("## ⏱️ Time Tracking"))
    cells.append(make_code_cell(
        f"# Time spent today (update this when done)\n"
        f"time_spent = 0  # in minutes\n"
        f"print(f'Time spent: {{time_spent}} mins')\n"
    ))

    # ── Daily wrap-up ─────────────────────────────────
    cells.append(make_markdown_cell(
        f"## ✅ Day {day} Wrap-up\n"
        f"- [ ] All videos watched\n"
        f"- [ ] All PQ answered\n"
        f"- [ ] HW submitted by 5 PM\n"
        f"- [ ] SQL done (if SQL day)\n"
        f"- [ ] Notebook pushed to GitHub\n"
    ))

    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.11.0"
            }
        },
        "cells": cells
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/create_day_notebook.py <day_number>")
        sys.exit(1)

    day = int(sys.argv[1])
    output_dir = Path(f"notebooks/day_{day}")
    output_dir.mkdir(parents=True, exist_ok=True)

    nb_path = output_dir / f"day_{day}.ipynb"
    nb = create_notebook(day)

    with open(nb_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2)

    print(f"✅ Created: {nb_path}")
    print(f"   Open it in Jupyter or VS Code and start working!")


if __name__ == "__main__":
    main()
