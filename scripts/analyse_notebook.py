"""
analyse_notebook.py (v5 - FULLY FIXED)

Triggered by schedule at 5 PM IST (11:30 UTC) OR workflow_dispatch.

Logic:
1. Find the latest day's notebook (or use arg)
2. Score PQ + HW + SQL with Claude API
3. PASS gate: score >= 70% AND all HW questions answered
4. If PASS  → tick checklist + create next day notebook + email + GitHub Issue
5. If FAIL  → email failure report + GitHub Issue (no next day created)
"""

import json
import os
import re
import sys
import time
from pathlib import Path
import urllib.request
import urllib.error

CHECKLIST_PATH    = "Month1_Final_Checklist.md"
NOTEBOOKS_DIR     = "notebooks"
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
GITHUB_TOKEN      = os.environ.get("GITHUB_TOKEN", "")
GITHUB_REPO       = os.environ.get("GITHUB_REPOSITORY", "")
PASS_SCORE_PCT    = 70
TEST_DAYS         = {10, 20, 30}

# ✅ FIXED: Using correct Claude model name
CLAUDE_MODEL = os.environ.get("CLAUDE_MODEL", "claude-3-haiku-20240307")

DAILY_QUESTIONS = {
    1: {
        "videos": ["#26 Python Function Examples (28min)", "#27 Lambda Functions In Python (10min)", "#28 Map Functions In Python (11min)"],
        "pq": [
            "Write a function using *args that returns the sum of all arguments. Call it with 3 different input combinations.",
            "What is the difference between a regular function and a lambda? Write multiply two numbers as both. When would you NOT use a lambda?",
            "Use map() with a lambda to cube every number in [1,2,3,4,5,6,7,8,9,10].",
            "Sort ['Alice','Bob','Charlie','Dan','Eve'] by the last character of each name using a lambda inside sorted().",
            "What does this output and why? `f = lambda x, y=10: x + y` -> print(f(5)) -> print(f(5, 20))"
        ],
        "hw": [
            "Write apply_operation(lst, func) that applies any function to every element. Test with 3 different lambdas.",
            "Use map() + lambda to give every employee a 10% salary raise — return full updated dicts.",
            "Write pipeline(data, *funcs) that chains functions — output of one becomes input of next. Test with 3 lambdas.",
            "Use map() to convert Celsius [0, 20, 37, 100, -40] to Fahrenheit. Formula: F = (C x 9/5) + 32.",
            "Mixed: Given a list of sentences, use map() to split each into words. Explain in 3 lines how this connects to Hadoop Mapper."
        ],
        "sql_topic": "", "sql": []
    },
    2: {
        "videos": ["#29 Python Filter Function (9min)", "#30 Import Modules And Packages (17min)", "#31 Standard Library Overview (18min)"],
        "pq": [
            "You have [1..15]. Use filter() with a lambda to return only numbers divisible by 3.",
            "Difference between filter() and a list comprehension? Rewrite: keep nums > 10 using both.",
            "Difference between `import math` and `from math import sqrt`? When would you use each?",
            "What does __init__.py do inside a folder? What happens if it's missing?",
            "Explain step by step: result = list(filter(lambda x: x % 2 == 0, [random.randint(1,100) for _ in range(10)]))"
        ],
        "hw": [
            "From words list — use filter() to keep words >4 chars, then map() to uppercase them. Chain in one line.",
            "Create a package data_tools with cleaner.py (remove_nulls) and formatter.py (to_uppercase). Import and use both in main.py.",
            "Using only os and datetime — print: current directory, today's date in DD-MM-YYYY, list of all .py files in current dir.",
            "Fix your Day 1 HW3 pipeline bug: a = i(data) -> a = i(a). Test by printing result after each step.",
            "Mixed: Generate 1000 random numbers, filter those above 500, map a doubling transformation. Print total, filtered count, processed count."
        ],
        "sql_topic": "SELECT, WHERE, ORDER BY, LIMIT",
        "sql": [
            "Table students(id, name, age, marks, city). Names and marks of students from Mumbai who scored >75, ordered by marks DESC, top 5 only.",
            "Are these two queries the same? SELECT * FROM students WHERE age=20 ORDER BY marks DESC; vs SELECT * FROM students ORDER BY marks DESC WHERE age=20;"
        ]
    },
    3: {
        "videos": ["#32 File Operation In Python (17min)", "#33 Working With File Paths (9min)", "#34 Exception Handling In Python (25min)"],
        "pq": [
            "Difference between open(file,'r'), 'w', 'a', and 'rb'? When do you use each?",
            "What does `with open(...) as f` do? Why is it better than manually calling f.close()?",
            "Difference between pathlib.Path and os.path? Which is more modern and why?",
            "Purpose of try/except/finally? Write a skeleton showing all three blocks.",
            "When would you use `except ValueError` instead of `except Exception`? Why is catching all exceptions bad practice?"
        ],
        "hw": [
            "Write a word frequency counter: read any .txt file, count each word, write top 10 most frequent to a new file.",
            "Write a safe file reader that handles FileNotFoundError and PermissionError separately with clear different messages.",
            "Use pathlib to: check if path exists, get filename without extension, get parent directory, list all .csv files recursively.",
            "Script that reads a file line by line — if any line causes error, log line number and error to errors.log and continue.",
            "Mixed: Write safe_write(filepath, data) that writes data, reads back to verify, raises custom WriteVerificationError if content doesn't match."
        ],
        "sql_topic": "GROUP BY, HAVING, Aggregate Functions",
        "sql": [
            "Table orders(order_id, customer_id, amount, city). Find cities where total order amount exceeds 10000, ordered by total DESC.",
            "Difference between WHERE and HAVING? Fix: SELECT department, COUNT(*) FROM employees HAVING COUNT(*) > 5 WHERE salary > 50000;"
        ]
    },
    4: {
        "videos": ["#35 OOPS In Python (23min)", "#36 Inheritance In Python (19min)"],
        "pq": [
            "What are the 4 pillars of OOP? Define each in one sentence.",
            "What is self in a Python class? Why do you always pass it as the first argument?",
            "Difference between a class attribute and an instance attribute? Show with code.",
            "What does super() do in inheritance? When and why do you use it?",
            "What is MRO (Method Resolution Order)? What does Python do when two parent classes have the same method?"
        ],
        "hw": [
            "Create BankAccount class with deposit(), withdraw(), get_balance(). Prevent negative balance with custom InsufficientFundsError.",
            "Create SavingsAccount that inherits BankAccount and adds interest_rate and apply_interest() method.",
            "Create DataPipeline base class with extract(), transform(), load(). Create CSVPipeline and JSONPipeline subclasses.",
            "Demonstrate MRO with diamond inheritance: A->B, A->C, B+C->D. Show which method gets called and why.",
            "Mixed: Model a Big Data cluster using OOP — Cluster, Node, NameNode(Node), DataNode(Node) with add_node(), get_active_nodes(), simulate_failure(node_id)."
        ],
        "sql_topic": "No SQL today", "sql": []
    },
    5: {
        "videos": ["#37 Polymorphism In Python (19min)", "#38 Encapsulation In Python (22min)", "#39 Abstraction In Python (9min)"],
        "pq": [
            "What is polymorphism? Give a real example with two classes that have the same method name but different behaviour.",
            "Difference between _single_underscore and __double_underscore in Python? What does name mangling do?",
            "How does @property work? Write a class where setting an attribute validates the value.",
            "Difference between an abstract class and a regular class? What happens if you instantiate an abstract class?",
            "What does ABC from the abc module do? Write a minimal example."
        ],
        "hw": [
            "Build Shape hierarchy: abstract base with area(). Implement Circle, Rectangle, Triangle. Call area() on a mixed list.",
            "Create DataRecord class with @property for age (must be 0-150) and email (must contain @). Raise ValueError on invalid input.",
            "Write a Singleton pattern for DatabaseConnection — only one instance should ever exist.",
            "Create abstract Connector class with connect(), query(sql), close(). Implement SQLConnector and a fake HDFSConnector.",
            "Mixed: Write ClusterConfig class that hides internal connection details and exposes only safe public methods."
        ],
        "sql_topic": "No SQL today", "sql": []
    },
    6: {
        "videos": ["#40 Magic Methods In Python (8min)", "#41 Custom Exception In Python (7min)", "#42 Operator Overloading In Python (9min)"],
        "pq": [
            "Name 5 dunder/magic methods and what each controls. Which one is called when you do len(obj)?",
            "Difference between __str__ and __repr__? When does Python use each automatically?",
            "How do you create a custom exception? Why create one instead of using ValueError?",
            "Which arithmetic operators can be overloaded in Python? What method name does + map to?",
            "What do __enter__ and __exit__ do? What Python statement uses them?"
        ],
        "hw": [
            "Build Matrix class that supports +, -, * (element-wise) via operator overloading. Implement __str__ to print it nicely.",
            "Create context manager class Timer using __enter__ and __exit__ that prints how long a code block took.",
            "Create custom exception hierarchy: PipelineError as base, then ExtractionError, TransformationError, LoadError as children.",
            "Implement __len__, __getitem__, __contains__ on a custom DataSet class wrapping a list.",
            "Mixed: Implement a mini DataFrame class that supports df['column'] (getitem), len(df) (len), and str(df) (str)."
        ],
        "sql_topic": "No SQL today", "sql": []
    },
    7: {
        "videos": ["#43 Iterators In Python (6min)", "#44 Generators In Python (11min)"],
        "pq": [
            "What are the two methods that make an object an iterator? Write a class-based iterator for even numbers.",
            "Difference between return and yield? What type does a generator function return?",
            "What is lazy evaluation? Why does it save memory compared to returning a full list?",
            "What does yield from do? How is it different from a regular yield?",
            "What happens when a generator is exhausted? What error do you get if you call next() on it?"
        ],
        "hw": [
            "Write a generator function that yields Fibonacci numbers up to N — never stores the full sequence in memory.",
            "Compare memory: list of 10 million numbers vs a generator. Use sys.getsizeof to show the difference.",
            "Build a data pipeline using only generators: read_lines(file) -> filter_empty(lines) -> parse_csv(lines). Chain them.",
            "Write an infinite counter generator counter(start, step) that yields numbers forever.",
            "Mixed: Simulate Spark lazy evaluation — LazyPipeline class where .map() and .filter() only execute when .collect() is called."
        ],
        "sql_topic": "No SQL today", "sql": []
    },
    8: {
        "videos": ["#45 Decorators In Python (21min)", "#46 Working With Numpy In Python (28min)"],
        "pq": [
            "What is a decorator and what problem does it solve? Why use functools.wraps inside one?",
            "Difference between a decorator with arguments and one without? Show the structure of each.",
            "What is a NumPy array? How is it different from a Python list? Name 3 advantages.",
            "What is broadcasting in NumPy? Show an example adding a scalar to an array and two different-shaped arrays.",
            "Difference between np.dot() and element-wise * multiplication?"
        ],
        "hw": [
            "Write a @timer decorator that prints the function name and how long it took to run.",
            "Write a @retry(n) decorator that retries the function up to n times if it raises an exception, then re-raises.",
            "Write a @validate_args decorator that checks all arguments are positive numbers — raises ValueError if not.",
            "Create a 5x5 NumPy matrix of random integers. Compute: transpose, row sums, column means, index of max value.",
            "Mixed: Generate two arrays of 1M random floats, multiply element-wise using NumPy, compare timing vs Python loop."
        ],
        "sql_topic": "No SQL today", "sql": []
    }
}

# ── Helpers ─────────────────────────────────────────────────────────────

def get_latest_day() -> int:
    """Find the latest day folder that exists."""
    nb_dir = Path(NOTEBOOKS_DIR)
    if not nb_dir.exists():
        return 0
    max_day = 0
    for folder in nb_dir.iterdir():
        if folder.is_dir() and folder.name.startswith("day_"):
            try:
                n = int(folder.name.split("_")[1])
                if (folder / f"day_{n}.ipynb").exists():
                    max_day = max(max_day, n)
            except (ValueError, IndexError):
                pass
    return max_day

# ── Notebook Parser ───────────────────────────────────────���────────────────

def extract_content(nb_path: str) -> dict:
    """Extract answers from Jupyter notebook."""
    with open(nb_path, encoding="utf-8") as f:
        nb = json.load(f)

    content = {"videos_marked": [], "pq_answers": {}, "hw_answers": {}, "sql_answers": {}, "notes": "", "time_spent": None}
    cur = None   # current section tag  e.g. "pq", "hw", "pq_2"

    for cell in nb.get("cells", []):
        src = "".join(cell.get("source", [])).strip()
        sl  = src.lower()
        ctype = cell.get("cell_type", "")

        if ctype == "markdown":
            # Section headers
            if re.search(r"^#+\s*videos?\b", sl, re.M):       cur = "videos"
            elif re.search(r"^#+\s*(practice questions?|pq)\b", sl, re.M): cur = "pq"
            elif re.search(r"^#+\s*(homework|hw)\b", sl, re.M):            cur = "hw"
            elif re.search(r"^#+\s*sql\b", sl, re.M):                      cur = "sql"
            elif re.search(r"^#+\s*notes?\b", sl, re.M):                   cur = "notes"

            # Item headers like ### PQ1  ### HW3  ### SQL2
            for pat, pfx in [(r"^#+\s*pq\s*(\d+)", "pq_"), (r"^#+\s*hw\s*(\d+)", "hw_"), (r"^#+\s*sql\s*(\d+)", "sql_")]:
                m = re.match(pat, sl)
                if m:
                    cur = pfx + m.group(1)
                    break

            # Videos checked
            if cur == "videos" and "[x]" in sl:
                content["videos_marked"].append(src)

        elif ctype == "code":
            # Time spent
            tm = re.search(r"time[_\s]*spent\s*=\s*(\d+)", src, re.I) or re.search(r"(\d+)\s*min", src, re.I)
            if tm:
                content["time_spent"] = int(tm.group(1))

            # Answer collection
            if cur:
                for pfx, store in [("pq_", "pq_answers"), ("hw_", "hw_answers"), ("sql_", "sql_answers")]:
                    if cur.startswith(pfx):
                        num = int(cur[len(pfx):])
                        cleaned = src.strip()
                        if cleaned and len(cleaned) > 5:
                            content[store][num] = cleaned
                        break

    if cur == "notes" and ctype == "markdown":
        content["notes"] += src + "\n"

    return content

def count_hw(day: int, content: dict) -> tuple:
    """Count how many HW questions have real answers (>20 chars)."""
    total    = len(DAILY_QUESTIONS.get(day, {}).get("hw", []))
    answered = sum(1 for i in range(1, total + 1)
                   if len(content["hw_answers"].get(i, "").strip()) > 20)
    return answered, total

# ── Claude Scorer ──────────────────────────────────────────────────────────

def call_claude(prompt: str) -> str:
    def call_claude(prompt: str) -> str:
        print("API KEY LENGTH:", len(ANTHROPIC_API_KEY))
        print("MODEL USED:", CLAUDE_MODEL)
    """Call Claude API to score an answer."""
    if not ANTHROPIC_API_KEY:
        return '{"score": 1, "feedback": "API key not set"}'
    
    # ✅ FIXED: Using correct API structure and model name
    payload = json.dumps({
        "model": CLAUDE_MODEL,
        "max_tokens": 400,
        "messages": [     {         "role": "user",         "content": [             {"type": "text", "text": prompt}         ]     } ]
    }).encode()
    
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "x-api-key": ANTHROPIC_API_KEY,
            "anthropic-version": "2023-06-01"
        },
        method="POST"
    )
    
    for attempt in range(2):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                response = json.loads(r.read().decode("utf-8"))

                content = response.get("content", [])
                texts = [c.get("text", "") for c in content if c.get("type") == "text"]

                return "\n".join(texts).strip()

        except urllib.error.HTTPError as e:
            
            error_body = e.read().decode("utf-8") if e.fp else ""

            print("\n================ CLAUDE ERROR ================")
            print("STATUS CODE:", e.code)
            print("RESPONSE BODY:")
            print(error_body)
            print("=============================================\n")

        except Exception as e:
            print(f"\n❌ Claude Error: {str(e)}")

        time.sleep(2)

    return '{"score": 0, "feedback": "API failed after retry"}'

def score_one(question: str, answer: str, qtype: str) -> dict:
    """Score a single answer."""
    if not answer or len(answer.strip()) < 10:
        return {"score": 0, "max": 2, "feedback": "No answer provided"}
    
    prompt = f"""You are reviewing a Big Data Engineering student's answer.
Question type: {qtype}
Question: {question}
Student answer: {answer}

Score out of 2 — 2=correct+complete, 1=partial, 0=wrong/missing.
Reply ONLY as JSON, no other text: {{"score": X, "feedback": "one sentence"}}"""
    
    resp = call_claude(prompt)
    try:
        # ✅ FIXED: Better JSON parsing
        cleaned = re.sub(r"```json|```", "", resp).strip()
        r = json.loads(cleaned)
        return {
            "score": int(r.get("score", 0)),
            "max": 2,
            "feedback": r.get("feedback", "")[:100]  # Limit feedback length
        }
    except json.JSONDecodeError:
        return {"score": 0, "max": 2, "feedback": f"Parse error"}
    except Exception as e:
        return {"score": 0, "max": 2, "feedback": f"Scoring error"}

def score_all(day: int, content: dict) -> dict:
    """Score all PQ, HW, SQL for a day."""
    scores = {"pq": {}, "hw": {}, "sql": {}, "total": 0, "max_total": 0}
    d = DAILY_QUESTIONS.get(day, {})
    
    for i, q in enumerate(d.get("pq", []), 1):
        r = score_one(q, content["pq_answers"].get(i, ""), "Practice Question")
        scores["pq"][i] = r
        scores["total"] += r["score"]
        scores["max_total"] += 2
    
    for i, q in enumerate(d.get("hw", []), 1):
        r = score_one(q, content["hw_answers"].get(i, ""), "Homework")
        scores["hw"][i] = r
        scores["total"] += r["score"]
        scores["max_total"] += 2
    
    for i, q in enumerate(d.get("sql", []), 1):
        r = score_one(q, content["sql_answers"].get(i, ""), "SQL")
        scores["sql"][i] = r
        scores["total"] += r["score"]
        scores["max_total"] += 2
    
    return scores

# ── Checklist Updater ──────────────────────────────────────────────────────

def tick_checklist(day: int, scores: dict, content: dict):
    """Update checklist with scores."""
    md_path = Path(CHECKLIST_PATH)
    if not md_path.exists():
        print(f"  ⚠️  Checklist not found: '{CHECKLIST_PATH}'")
        return

    pct = round(scores["total"] / scores["max_total"] * 100) if scores["max_total"] else 0
    md  = md_path.read_text(encoding="utf-8")

    # Tick PQ/HW/SQL boxes in day's section
    pat = rf"(## ✅ Day {day}\b.*?)(\n---|\n## ✅ Day {day+1}|\Z)"
    
    def tick(m):
        s = re.sub(r"- \[ \] \*\*(PQ|HW|SQL)\d+", lambda x: x.group(0).replace("[ ]", "[x]"), m.group(1))
        return s + (m.group(2) or "")
    
    md = re.sub(pat, tick, md, count=1, flags=re.DOTALL)

    # Build score block
    d = DAILY_QUESTIONS.get(day, {})
    
    def rows(section, items, label):
        out = []
        for i in range(1, len(items)+1):
            s = section.get(i, {"score":0, "feedback":"—"})
            e = "✅" if s["score"]==2 else "⚠️" if s["score"]==1 else "❌"
            out.append(f"- {e} **{label}{i}:** {s['score']}/2 — {s['feedback']}")
        return "\n".join(out)

    grade = "🏆 Excellent" if pct>=80 else "👍 Good" if pct>=70 else "⚠️ Needs improvement"
    block = [f"\n#### 📊 Day {day} Auto-Score\n",
             rows(scores["pq"], d.get("pq",[]), "PQ"),
             "\n" + rows(scores["hw"], d.get("hw",[]), "HW")]
    if scores["sql"]:
        block.append("\n" + rows(scores["sql"], d.get("sql",[]), "SQL"))
    block.append(f"\n**🎯 {scores['total']}/{scores['max_total']} ({pct}%) — {grade}**")
    if content.get("time_spent"):
        block.append(f"**⏱️ {content['time_spent']} mins**")

    score_block = "\n".join(block)
    md = re.sub(pat, lambda m: m.group(1) + "\n" + score_block + "\n" + (m.group(2) or ""), md, count=1, flags=re.DOTALL)
    md_path.write_text(md, encoding="utf-8")
    print("  ✅ Checklist ticked and score block added")

# ── Next Day Notebook Creator ──────────────────────────────────────────────

def mk_md(s): 
    return {"cell_type":"markdown","metadata":{},"source":s if isinstance(s, list) else [s]}

def mk_code(s=""): 
    return {"cell_type":"code","execution_count":None,"metadata":{},"outputs":[],"source":[s] if isinstance(s, str) else s}

def create_next_notebook(next_day: int) -> bool:
    """Create next day notebook from DAILY_QUESTIONS."""
    out = Path(NOTEBOOKS_DIR) / f"day_{next_day}"
    nb  = out / f"day_{next_day}.ipynb"
    
    if nb.exists():
        print(f"  ℹ️  day_{next_day}.ipynb already exists")
        return False
    
    out.mkdir(parents=True, exist_ok=True)
    d = DAILY_QUESTIONS.get(next_day, {})
    cells = []
    
    cells.append(mk_md(f"# 📓 Day {next_day} — Big Data Engineering\n> **Date:** <!-- fill in -->\n> **Time Started:** <!-- fill in -->"))
    
    vids = "\n".join(f"- [ ] {v}" for v in d.get("videos",[])) or "- [ ] <!-- video name -->"
    cells.append(mk_md(f"## Videos\nMark each as `[x]` when done.\n\n{vids}"))
    cells.append(mk_code("# Video notes — write key concepts here as you watch\n"))
    
    cells.append(mk_md("## Practice Questions (PQ)\nAnswer each question in the code cell below it."))
    for i, q in enumerate(d.get("pq",[]),1):
        cells.append(mk_md(f"### PQ{i}\n{q}"))
        cells.append(mk_code(f"# PQ{i} answer\n"))
    
    cells.append(mk_md("## Homework (HW)\nComplete by 5 PM next day."))
    for i, q in enumerate(d.get("hw",[]),1):
        cells.append(mk_md(f"### HW{i}\n{q}"))
        cells.append(mk_code(f"# HW{i} answer\n"))
    
    if d.get("sql"):
        cells.append(mk_md(f"## SQL\nTopic: {d.get('sql_topic','')}"))
        for i, q in enumerate(d["sql"],1):
            cells.append(mk_md(f"### SQL{i}\n{q}"))
            cells.append(mk_code(f'sql_answer_{i} = """\n-- SQL{i} answer here\n"""\nprint(sql_answer_{i})'))
    
    cells.append(mk_md("## Notes"))
    cells.append(mk_code("# notes\n"))
    
    cells.append(mk_md("## ⏱️ Time Tracking"))
    cells.append(mk_code("time_spent = 0  # in minutes\nprint(f'Time spent: {time_spent} mins')"))
    
    sql_chk = "- [ ] SQL done\n" if d.get("sql") else ""
    cells.append(mk_md(f"## ✅ Day {next_day} Wrap-up\n- [ ] All videos watched\n- [ ] All PQ answered\n- [ ] HW submitted by 5 PM\n{sql_chk}- [ ] Notebook pushed to GitHub"))
    
    notebook = {
        "nbformat":4,"nbformat_minor":5,
        "metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"python","version":"3.11.0"}},
        "cells":cells
    }
    
    with open(nb, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=2)
    
    print(f"  ✅ Created notebooks/day_{next_day}/day_{next_day}.ipynb")
    return True

# ── GitHub Issue ───────────────────────────────────────────────────────────

def post_issue(title: str, body: str, label: str):
    """Post a GitHub issue."""
    if not GITHUB_TOKEN or not GITHUB_REPO:
        print(f"  ⚠️  GitHub not configured — skipping issue")
        return
    
    payload = json.dumps({"title": title, "body": body, "labels": [label]}).encode()
    req = urllib.request.Request(
        f"https://api.github.com/repos/{GITHUB_REPO}/issues", data=payload,
        headers={"Authorization": f"token {GITHUB_TOKEN}", "Content-Type": "application/json", "Accept": "application/vnd.github.v3+json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req) as r:
            issue = json.loads(r.read())
            print(f"  ✅ Issue: {issue.get('html_url','')}")
    except Exception as e:
        print(f"  ⚠️  Issue failed: {e}")

def create_summary_issue(day: int, scores: dict, content: dict, passed: bool, hw_answered: int, hw_total: int):
    """Create summary issue with scores."""
    pct = round(scores["total"] / scores["max_total"] * 100) if scores["max_total"] else 0
    next_day = day + 1

    def q_rows(sd, label):
        return "\n".join(
            f"- {'✅' if s['score']==2 else '⚠️' if s['score']==1 else '❌'} **{label}{i}:** {s['score']}/2 — {s['feedback']}"
            for i, s in sd.items()
        )

    parts = [
        f"## 📊 Day {day} Score Report\n",
        f"**Score:** {scores['total']}/{scores['max_total']} ({pct}%)",
        f"**HW answered:** {hw_answered}/{hw_total}",
        f"**Status:** {'✅ PASSED — Day ' + str(next_day) + ' unlocked' if passed else '❌ NOT PASSED — fix and re-push'}",
        f"**Time:** {content.get('time_spent','—')} mins\n",
        "### 💡 PQ", q_rows(scores["pq"], "PQ"),
        "\n### 📝 HW", q_rows(scores["hw"], "HW"),
    ]
    
    if scores["sql"]:
        parts += ["\n### 🗄️ SQL", q_rows(scores["sql"], "SQL")]

    if passed:
        nd = DAILY_QUESTIONS.get(next_day, {})
        parts += [f"\n---\n## 📬 Day {next_day} Ready in your repo",
                  "### 📹 Videos", "\n".join(f"- [ ] {v}" for v in nd.get("videos",[])),
                  "\n### 💡 PQ", "\n".join(f"**PQ{i}:** {q}" for i,q in enumerate(nd.get("pq",[]),1)),
                  "\n### 📝 HW", "\n".join(f"**HW{i}:** {q}" for i,q in enumerate(nd.get("hw",[]),1))]
        if nd.get("sql"):
            parts += [f"\n### 🗄️ SQL — {nd.get('sql_topic','')}", "\n".join(f"**SQL{i}:** {q}" for i,q in enumerate(nd["sql"],1))]
        if next_day in TEST_DAYS:
            parts += [f"\n---\n## 🧪 Day {next_day} is a TEST DAY!", f"Review Day 1–{next_day-1}. No notes. 45–75 min."]
        parts += ["\n---\n### ⏰ Deadlines", "- Videos + PQ → **tonight 10:30 PM**", "- HW → **tomorrow 5:00 PM**"]
    else:
        missing = [i for i in range(1, hw_total+1) if len(content["hw_answers"].get(i,"").strip()) <= 20]
        parts += ["\n---\n## ⚠️ What to fix",
                  f"Need: ≥70% score AND all {hw_total} HW answered",
                  f"HW missing answers: {missing if missing else 'none — score too low'}",
                  "\n1. Fix ❌ answers\n2. Make sure all HW cells have real code\n3. Push — bot re-scores at 5 PM IST"]

    title = f"{'✅' if passed else '❌'} Day {day} — {pct}% | {'Day '+str(next_day)+' ready' if passed else 'needs improvement'}"
    post_issue(title, "\n".join(parts), "completed" if passed else "needs-review")

# ── Main ──────────────────────────────────────────────────────────────

def main():
    """Main scoring pipeline."""
    day = int(sys.argv[1]) if len(sys.argv) >= 2 else get_latest_day()
    if not day:
        print("No notebooks found.")
        sys.exit(1)

    nb_path = f"{NOTEBOOKS_DIR}/day_{day}/day_{day}.ipynb"
    print(f"\n{'='*54}")
    print(f"  📓 Scoring Day {day} — gate: ≥70% AND all HW answered")
    print(f"{'='*54}\n")

    if not Path(nb_path).exists():
        print(f"  ❌ Notebook not found: {nb_path}")
        sys.exit(1)

    print("  📖 Parsing notebook...")
    content = extract_content(nb_path)
    hw_answered, hw_total = count_hw(day, content)
    print(f"  PQ:{len(content['pq_answers'])}  HW:{hw_answered}/{hw_total}  SQL:{len(content['sql_answers'])}")

    print("  🤖 Scoring with Claude API...")
    scores = score_all(day, content)
    pct    = round(scores["total"] / scores["max_total"] * 100) if scores["max_total"] else 0
    all_hw = hw_answered >= hw_total
    passed = pct >= PASS_SCORE_PCT and all_hw
    print(f"  Score: {scores['total']}/{scores['max_total']} ({pct}%)  HW: {hw_answered}/{hw_total}")
    print(f"  Gate: {'PASSED ✅' if passed else 'NOT PASSED ❌'}")

    if passed:
        print("  📝 Ticking checklist...")
        tick_checklist(day, scores, content)
        print(f"  📁 Creating Day {day+1} notebook...")
        next_created = create_next_notebook(day + 1)
    else:
        print("  ⛔ Gate not met — checklist not ticked, next day not created")
        next_created = False

    print("  📧 Sending email...")
    try:
        from send_email import email_day_result
        email_day_result(day, scores, content, passed, next_created)
    except Exception as e:
        print(f"  ⚠️  Email error: {e}")

    print("  🐙 Creating GitHub Issue...")
    create_summary_issue(day, scores, content, passed, hw_answered, hw_total)

    print(f"\n{'='*54}")
    print(f"  Done — Day {day} — {pct}% — {'PASSED ✅' if passed else 'NOT PASSED ❌'}")
    print(f"{'='*54}\n")

if __name__ == "__main__":
    main()
