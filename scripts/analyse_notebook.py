"""
analyse_notebook.py
-------------------
Analyses a submitted day_X.ipynb notebook and:
1. Checks completeness (videos, PQ, HW, time logged)
2. Scores each PQ and HW using Claude API
3. Updates the Month1_Final_Checklist.md with scores + feedback
4. Injects next day's questions into the MD file
5. Creates a GitHub Issue as a reminder/summary
"""

import json
import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
import urllib.request
import urllib.parse

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
CHECKLIST_PATH = "Month1_Final_Checklist.md"
NOTEBOOKS_DIR = "notebooks"
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
GITHUB_REPO = os.environ.get("GITHUB_REPOSITORY", "")  # e.g. username/repo

# Deadlines (24h format)
DEADLINE_VIDEOS = "22:30"   # 10:30 PM same day
DEADLINE_HW = "17:00"       # 5:00 PM next day

# Weekend config
WEEKEND_PQ_COUNT = 3        # Only 3 PQ on weekends
WEEKEND_HW_COUNT = 2        # Only 2 HW on weekends
WEEKEND_SQL_COUNT = 1       # Only 1 SQL on weekends

# ─────────────────────────────────────────────
# DAILY QUESTIONS BANK
# ─────────────────────────────────────────────
DAILY_QUESTIONS = {
    2: {
        "videos": ["#29 Python Filter Function (9min)", "#30 Import Modules And Packages (17min)", "#31 Standard Library Overview (18min)"],
        "pq": [
            "You have `[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]`. Use `filter()` with a lambda to return only numbers divisible by 3.",
            "What is the difference between `filter()` and a list comprehension? Rewrite `nums = [10,25,3,47,8,99,2]` — keep numbers > 10 — using both.",
            "What is the difference between `import math` and `from math import sqrt`? When would you use each?",
            "What does `__init__.py` do inside a folder? What happens if it's missing?",
            "Explain what this does step by step: `result = list(filter(lambda x: x % 2 == 0, [random.randint(1,100) for _ in range(10)]))`"
        ],
        "hw": [
            "From `words = ['apple','hi','banana','ok','strawberry','cat','watermelon','go']` — use `filter()` to keep words with >4 chars, then `map()` to uppercase them. Chain in one line.",
            "Create a package `data_tools` with `cleaner.py` (remove_nulls) and `formatter.py` (to_uppercase). Import and use both in `main.py`.",
            "Using only `os` and `datetime` standard library — print: current directory, today's date in DD-MM-YYYY, list of all .py files in current dir.",
            "Fix your Day 1 HW3 pipeline bug: `a = i(data)` → `a = i(a)`. Test by printing result after each step.",
            "🔀 Mixed: Generate 1000 random numbers, filter those above 500, map a doubling transformation on only those. Print: total records, filtered count, processed count."
        ],
        "sql_topic": "SELECT, WHERE, ORDER BY, LIMIT",
        "sql": [
            "Table `students(id, name, age, marks, city)`. Write a query: names and marks of students from 'Mumbai' who scored > 75, ordered by marks DESC, top 5 only.",
            "Are these two queries the same? Explain why or why not:\n```sql\nSELECT * FROM students WHERE age = 20 ORDER BY marks DESC;\nSELECT * FROM students ORDER BY marks DESC WHERE age = 20;\n```"
        ]
    },
    3: {
        "videos": ["#32 File Operation In Python (17min)", "#33 Working With File Paths (9min)", "#34 Exception Handling In Python (25min)"],
        "pq": [
            "What is the difference between `open(file, 'r')`, `'w'`, `'a'`, and `'rb'`? When do you use each?",
            "What does `with open(...) as f` do? Why is it better than manually calling `f.close()`?",
            "What is the difference between `pathlib.Path` and `os.path`? Which is more modern and why?",
            "What is the purpose of `try/except/finally`? Write a skeleton showing all three blocks.",
            "When would you use `except ValueError` instead of `except Exception`? Why is catching all exceptions bad practice?"
        ],
        "hw": [
            "Write a word frequency counter: read any `.txt` file → count each word → write top 10 most frequent words to a new file.",
            "Write a safe file reader function that handles `FileNotFoundError` and `PermissionError` separately with clear, different error messages.",
            "Use `pathlib` to: check if a path exists, get the filename without extension, get the parent directory, list all `.csv` files recursively.",
            "Write a script that reads a file, processes each line, and if any line causes an error — logs the line number and error to a separate `errors.log` file and continues.",
            "🔀 Mixed: In distributed systems like HDFS, file operations can fail mid-way. Write a Python function `safe_write(filepath, data)` that: writes data, verifies the file was written correctly by reading it back, raises a custom `WriteVerificationError` if the content doesn't match."
        ],
        "sql_topic": "GROUP BY, HAVING, Aggregate Functions",
        "sql": [
            "Table `orders(order_id, customer_id, amount, city)`. Write a query to find cities where the total order amount exceeds 10000, showing city name and total amount, ordered by total DESC.",
            "What is the difference between `WHERE` and `HAVING`? Rewrite this broken query correctly:\n```sql\nSELECT department, COUNT(*) FROM employees HAVING COUNT(*) > 5 WHERE salary > 50000;\n```"
        ]
    },
    4: {
        "videos": ["#35 OOPS In Python (23min)", "#36 Inheritance In Python (19min)"],
        "pq": [
            "What are the 4 pillars of OOP? Define each in one sentence.",
            "What is `self` in a Python class? Why do you always pass it as the first argument?",
            "What is the difference between a class attribute and an instance attribute? Show with code.",
            "What does `super()` do in inheritance? When and why do you use it?",
            "What is MRO (Method Resolution Order)? What does Python do when two parent classes have the same method?"
        ],
        "hw": [
            "Create a `BankAccount` class with `deposit()`, `withdraw()`, `get_balance()`. Prevent negative balance — raise a custom `InsufficientFundsError`.",
            "Create a `SavingsAccount` that inherits `BankAccount` and adds `interest_rate` attribute and `apply_interest()` method.",
            "Create a `DataPipeline` base class with `extract()`, `transform()`, `load()` methods. Create `CSVPipeline` and `JSONPipeline` subclasses that override each method differently.",
            "Demonstrate MRO with a diamond inheritance example — A → B, A → C, B+C → D. Show which method gets called and why.",
            "🔀 Mixed: Model a Big Data cluster using OOP — classes for `Cluster`, `Node`, `NameNode(Node)`, `DataNode(Node)`. Each node has `node_id`, `status`, `ip_address`. Cluster has `add_node()`, `get_active_nodes()`, `simulate_failure(node_id)`."
        ],
        "sql_topic": "No SQL today — Python OOP focus day",
        "sql": []
    },
    5: {
        "videos": ["#37 Polymorphism In Python (19min)", "#38 Encapsulation In Python (22min)", "#39 Abstraction In Python (9min)"],
        "pq": [
            "What is polymorphism? Give a real example with two classes that have the same method name but different behaviour.",
            "What is the difference between `_single_underscore` and `__double_underscore` in Python? What does name mangling do?",
            "How does `@property` work? Write a class where setting an attribute validates the value.",
            "What is the difference between an abstract class and a regular class? What happens if you try to instantiate an abstract class?",
            "What does `ABC` from the `abc` module do? Write a minimal example."
        ],
        "hw": [
            "Build a `Shape` hierarchy: base class `Shape` with abstract method `area()`. Implement `Circle`, `Rectangle`, `Triangle`. Call `area()` on a list of mixed shapes using polymorphism.",
            "Create a `DataRecord` class with `@property` for `age` (must be > 0 and < 150) and `email` (must contain @). Raise `ValueError` with clear messages on invalid input.",
            "Write a `Singleton` pattern for a `DatabaseConnection` class — no matter how many times you call it, only one instance should ever exist.",
            "Create abstract class `Connector` with abstract methods `connect()`, `query(sql)`, `close()`. Implement `SQLConnector` and a fake `HDFSConnector`.",
            "🔀 Mixed: Why is encapsulation critical in microservices and distributed systems? Write a `ClusterConfig` class that hides internal connection details but exposes only safe public methods."
        ],
        "sql_topic": "No SQL today — Python OOP focus day",
        "sql": []
    },
    6: {
        "videos": ["#40 Magic Methods In Python (8min)", "#41 Custom Exception In Python (7min)", "#42 Operator Overloading In Python (9min)"],
        "pq": [
            "Name 5 dunder/magic methods and what each controls. Which one is called when you do `len(obj)`?",
            "What is the difference between `__str__` and `__repr__`? When does Python use each automatically?",
            "How do you create a custom exception? Why would you create one instead of using `ValueError`?",
            "Which arithmetic operators can be overloaded in Python? What method name does `+` map to?",
            "What do `__enter__` and `__exit__` do? What Python statement uses them?"
        ],
        "hw": [
            "Build a `Matrix` class that supports `+`, `-`, `*` (element-wise) via operator overloading. Implement `__str__` to print it nicely.",
            "Create a context manager class `Timer` using `__enter__` and `__exit__` that prints how long a code block took to run.",
            "Create a custom exception hierarchy: `PipelineError` as base, then `ExtractionError`, `TransformationError`, `LoadError` as children. Simulate a pipeline that raises and catches each.",
            "Implement `__len__`, `__getitem__`, `__contains__` on a custom `DataSet` class wrapping a list.",
            "🔀 Mixed: How would Python magic methods help when building a DataFrame-like API? Implement a mini `DataFrame` class that supports `df['column']` (getitem), `len(df)` (len), and `str(df)` (str) for a dict of columns."
        ],
        "sql_topic": "No SQL today — Python OOP focus day",
        "sql": []
    },
    7: {
        "videos": ["#43 Iterators In Python (6min)", "#44 Generators In Python (11min)"],
        "pq": [
            "What are the two methods that make an object an iterator? Write a class-based iterator for even numbers.",
            "What is the difference between `return` and `yield`? What type does a generator function return?",
            "What is lazy evaluation? Why does it save memory compared to returning a full list?",
            "What does `yield from` do? How is it different from a regular `yield`?",
            "What happens when a generator is exhausted? What error do you get if you call `next()` on it?"
        ],
        "hw": [
            "Write a generator function that yields Fibonacci numbers up to N — never stores the full sequence in memory.",
            "Compare memory: create a list of 10 million numbers vs a generator for the same. Use `sys.getsizeof` to show the difference.",
            "Build a data pipeline using only generators: `read_lines(file)` → `filter_empty(lines)` → `parse_csv(lines)` — chain them together.",
            "Write an infinite counter generator `counter(start, step)` that yields numbers forever from `start` with a given `step`.",
            "🔀 Mixed: Spark uses lazy evaluation — transformations aren't executed until an action is called. Simulate this in Python: create a `LazyPipeline` class where you can chain `.map()` and `.filter()` operations, and they only execute when you call `.collect()`."
        ],
        "sql_topic": "No SQL today — Week 1 review day",
        "sql": []
    },
    8: {
        "videos": ["#45 Decorators In Python (21min)", "#46 Working With Numpy In Python (28min)"],
        "pq": [
            "What is a decorator and what problem does it solve? Why use `functools.wraps` inside one?",
            "What is the difference between a decorator with arguments and one without? Show the structure of each.",
            "What is a NumPy array? How is it different from a Python list? Name 3 advantages.",
            "What is broadcasting in NumPy? Show an example where you add a scalar to an array and where you add two different-shaped arrays.",
            "What is the difference between `np.dot()` and element-wise `*` multiplication?"
        ],
        "hw": [
            "Write a `@timer` decorator that prints the function name and how long it took to run.",
            "Write a `@retry(n)` decorator that retries the function up to `n` times if it raises an exception, then re-raises the last exception.",
            "Write a `@validate_args` decorator that checks all arguments to a function are positive numbers — raises `ValueError` if not.",
            "Create a 5×5 NumPy matrix of random integers. Compute: transpose, row sums, column means, and find the index of the max value.",
            "🔀 Mixed: NumPy vectorized operations run in parallel under the hood — similar to how Spark distributes computations. Generate two arrays of 1M random floats, multiply them element-wise using NumPy, and compare timing vs a Python loop."
        ],
        "sql_topic": "No SQL today — Python focus day",
        "sql": []
    }
}


# ─────────────────────────────────────────────
# NOTEBOOK PARSER
# ─────────────────────────────────────────────
def load_notebook(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_cells(nb: dict) -> list[dict]:
    """Extract all cells with their type and source."""
    cells = []
    for cell in nb.get("cells", []):
        cells.append({
            "type": cell.get("cell_type", ""),
            "source": "".join(cell.get("source", [])),
            "outputs": cell.get("outputs", [])
        })
    return cells


def extract_notebook_content(nb_path: str) -> dict:
    """Parse notebook and extract structured content."""
    nb = load_notebook(nb_path)
    cells = extract_cells(nb)

    content = {
        "videos_marked": [],
        "pq_answers": {},
        "hw_answers": {},
        "sql_answers": {},
        "notes": "",
        "time_spent": None,
        "raw_cells": cells
    }

    current_section = None

    for cell in cells:
        src = cell["source"].strip()
        src_lower = src.lower()

        # Detect sections
        if "# videos" in src_lower or "## videos" in src_lower:
            current_section = "videos"
        elif "# practice questions" in src_lower or "# pq" in src_lower or "## pq" in src_lower:
            current_section = "pq"
        elif "# homework" in src_lower or "# hw" in src_lower or "## hw" in src_lower:
            current_section = "hw"
        elif "# sql" in src_lower or "## sql" in src_lower:
            current_section = "sql"
        elif "# notes" in src_lower or "## notes" in src_lower:
            current_section = "notes"
        elif "time spent" in src_lower or "time:" in src_lower:
            # Extract time
            match = re.search(r"(\d+)\s*min", src, re.IGNORECASE)
            if match:
                content["time_spent"] = int(match.group(1))

        # Collect content by section
        if current_section == "videos" and "[x]" in src_lower:
            content["videos_marked"].append(src)

        elif current_section == "pq":
            # Match PQ1, PQ2 etc.
            match = re.search(r"pq\s*(\d+)[:\.]?\s*(.*)", src, re.IGNORECASE | re.DOTALL)
            if match:
                num = int(match.group(1))
                answer = match.group(2).strip()
                content["pq_answers"][num] = answer

        elif current_section == "hw":
            match = re.search(r"hw\s*(\d+)[:\.]?\s*(.*)", src, re.IGNORECASE | re.DOTALL)
            if match:
                num = int(match.group(1))
                answer = match.group(2).strip()
                content["hw_answers"][num] = answer

        elif current_section == "sql":
            match = re.search(r"sql\s*(\d+)[:\.]?\s*(.*)", src, re.IGNORECASE | re.DOTALL)
            if match:
                num = int(match.group(1))
                answer = match.group(2).strip()
                content["sql_answers"][num] = answer

        elif current_section == "notes":
            content["notes"] += src + "\n"

    return content


# ─────────────────────────────────────────────
# CLAUDE API SCORER
# ─────────────────────────────────────────────
def call_claude(prompt: str) -> str:
    """Call Claude API and return response text."""
    if not ANTHROPIC_API_KEY:
        return "API key not set"

    payload = json.dumps({
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 1000,
        "messages": [{"role": "user", "content": prompt}]
    }).encode("utf-8")

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

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["content"][0]["text"]
    except Exception as e:
        return f"API error: {str(e)}"


def score_answer(question: str, answer: str, q_type: str) -> dict:
    """Score a single PQ or HW answer using Claude."""
    if not answer or len(answer.strip()) < 5:
        return {"score": 0, "max": 2, "feedback": "No answer provided"}

    prompt = f"""You are reviewing a Big Data Engineering student's answer.
Question type: {q_type}
Question: {question}
Student's answer: {answer}

Score this answer out of 2:
- 2 = Correct and complete
- 1 = Partially correct or missing key details
- 0 = Wrong or missing

Reply in this exact JSON format only, no other text:
{{"score": X, "feedback": "one sentence feedback"}}"""

    response = call_claude(prompt)

    try:
        # Strip any markdown fences
        clean = re.sub(r"```json|```", "", response).strip()
        result = json.loads(clean)
        return {"score": result.get("score", 0), "max": 2, "feedback": result.get("feedback", "")}
    except Exception:
        return {"score": 0, "max": 2, "feedback": f"Could not parse score: {response[:100]}"}


def score_all_answers(day: int, content: dict) -> dict:
    """Score all PQ, HW, SQL answers for the day."""
    scores = {"pq": {}, "hw": {}, "sql": {}, "total": 0, "max_total": 0}
    day_data = DAILY_QUESTIONS.get(day, {})

    print(f"  Scoring PQ answers...")
    for i, question in enumerate(day_data.get("pq", []), 1):
        answer = content["pq_answers"].get(i, "")
        result = score_answer(question, answer, "Practice Question")
        scores["pq"][i] = result
        scores["total"] += result["score"]
        scores["max_total"] += 2

    print(f"  Scoring HW answers...")
    for i, question in enumerate(day_data.get("hw", []), 1):
        answer = content["hw_answers"].get(i, "")
        result = score_answer(question, answer, "Homework")
        scores["hw"][i] = result
        scores["total"] += result["score"]
        scores["max_total"] += 2

    print(f"  Scoring SQL answers...")
    for i, question in enumerate(day_data.get("sql", []), 1):
        answer = content["sql_answers"].get(i, "")
        result = score_answer(question, answer, "SQL Question")
        scores["sql"][i] = result
        scores["total"] += result["score"]
        scores["max_total"] += 2

    return scores


# ─────────────────────────────────────────────
# CHECKLIST UPDATER
# ─────────────────────────────────────────────
def build_score_block(day: int, scores: dict, content: dict) -> str:
    """Build the score summary block to inject into MD."""
    day_data = DAILY_QUESTIONS.get(day, {})
    lines = [f"\n#### 📊 Day {day} Results\n"]

    # PQ scores
    if scores["pq"]:
        lines.append("**💡 Practice Questions:**")
        for i, q in enumerate(day_data.get("pq", []), 1):
            s = scores["pq"].get(i, {"score": 0, "feedback": ""})
            emoji = "✅" if s["score"] == 2 else "⚠️" if s["score"] == 1 else "❌"
            lines.append(f"- {emoji} PQ{i}: {s['score']}/2 — {s['feedback']}")

    # HW scores
    if scores["hw"]:
        lines.append("\n**📝 Homework:**")
        for i, q in enumerate(day_data.get("hw", []), 1):
            s = scores["hw"].get(i, {"score": 0, "feedback": ""})
            emoji = "✅" if s["score"] == 2 else "⚠️" if s["score"] == 1 else "❌"
            lines.append(f"- {emoji} HW{i}: {s['score']}/2 — {s['feedback']}")

    # SQL scores
    if scores["sql"]:
        lines.append("\n**🗄️ SQL:**")
        for i in range(1, len(day_data.get("sql", [])) + 1):
            s = scores["sql"].get(i, {"score": 0, "feedback": ""})
            emoji = "✅" if s["score"] == 2 else "⚠️" if s["score"] == 1 else "❌"
            lines.append(f"- {emoji} SQL{i}: {s['score']}/2 — {s['feedback']}")

    # Total
    pct = round((scores["total"] / scores["max_total"]) * 100) if scores["max_total"] > 0 else 0
    lines.append(f"\n**🎯 Total: {scores['total']}/{scores['max_total']} ({pct}%)**")

    if content.get("time_spent"):
        lines.append(f"**⏱️ Time Spent: {content['time_spent']} mins**")

    # Grade
    if pct >= 80:
        lines.append("**🏆 Grade: Excellent — keep it up!**")
    elif pct >= 60:
        lines.append("**👍 Grade: Good — review the ❌ items**")
    else:
        lines.append("**⚠️ Grade: Needs improvement — revisit today's topics**")

    return "\n".join(lines)


def build_next_day_questions(next_day: int) -> str:
    """Build the question block for the next day."""
    day_data = DAILY_QUESTIONS.get(next_day)
    if not day_data:
        return f"\n> ℹ️ Day {next_day} questions will be added when available.\n"

    lines = [f"\n#### 📬 Day {next_day} Questions (Auto-generated)\n"]

    lines.append("**💡 Practice Questions (5)**")
    for i, q in enumerate(day_data.get("pq", []), 1):
        lines.append(f"- [ ] **PQ{i}:** {q}")

    lines.append("\n**📝 Homework (5)**")
    for i, q in enumerate(day_data.get("hw", []), 1):
        lines.append(f"- [ ] **HW{i}:** {q}")

    sql_qs = day_data.get("sql", [])
    if sql_qs:
        topic = day_data.get("sql_topic", "SQL")
        lines.append(f"\n**🗄️ SQL Questions (2) — {topic}**")
        for i, q in enumerate(sql_qs, 1):
            lines.append(f"- [ ] **SQL{i}:** {q}")

    return "\n".join(lines)


def update_checklist(day: int, scores: dict, content: dict):
    """Update the MD checklist with scores and next day questions."""
    md_path = Path(CHECKLIST_PATH)
    if not md_path.exists():
        print(f"  ⚠️  Checklist not found at {CHECKLIST_PATH}")
        return

    md_text = md_path.read_text(encoding="utf-8")

    # 1. Mark day videos as complete
    for video in content.get("videos_marked", []):
        clean = re.sub(r"\[.\]", "[x]", video[:50])

    # 2. Insert score block after the day's section
    score_block = build_score_block(day, scores, content)
    day_pattern = rf"(## ✅ Day {day}\b.*?)(\n---|\n## ✅ Day {day+1})"
    replacement = r"\1" + "\n" + score_block + r"\2"
    new_md = re.sub(day_pattern, replacement, md_text, flags=re.DOTALL)

    # 3. Inject next day questions
    next_day = day + 1
    next_day_pattern = rf"(## ✅ Day {next_day}\b.*?)(- \[ \] PQ1:.*?)(\n\n|\Z)"

    next_q_block = build_next_day_questions(next_day)

    # Replace placeholder PQ lines with actual questions
    new_md = re.sub(
        rf"(## ✅ Day {next_day}.*?💡 Practice Questions.*?\n)((?:- \[ \] PQ\d:\n)+)",
        lambda m: m.group(1) + next_q_block + "\n",
        new_md,
        flags=re.DOTALL
    )

    # 4. Update progress tracker — mark day as done
    emoji = "✅" if scores["total"] / max(scores["max_total"], 1) >= 0.6 else "⚠️"
    new_md = new_md.replace(
        f"| Week", f"| Week"  # no-op placeholder for future tracker updates
    )

    md_path.write_text(new_md, encoding="utf-8")
    print(f"  ✅ Checklist updated for Day {day}")


# ─────────────────────────────────────────────
# GITHUB ISSUE CREATOR
# ─────────────────────────────────────────────
def create_github_issue(day: int, scores: dict, missed_deadlines: list):
    """Create a GitHub Issue as a reminder/summary."""
    if not GITHUB_TOKEN or not GITHUB_REPO:
        print("  ⚠️  GitHub token or repo not set — skipping issue creation")
        return

    pct = round((scores["total"] / scores["max_total"]) * 100) if scores["max_total"] > 0 else 0

    if missed_deadlines:
        title = f"⚠️ Day {day} — Missed deadline(s): {', '.join(missed_deadlines)}"
        label = "missed-deadline"
    elif pct >= 80:
        title = f"✅ Day {day} Complete — {scores['total']}/{scores['max_total']} ({pct}%)"
        label = "completed"
    else:
        title = f"⚠️ Day {day} — Needs review — {pct}% score"
        label = "needs-review"

    body_lines = [
        f"## Day {day} Summary",
        f"**Score:** {scores['total']}/{scores['max_total']} ({pct}%)",
        "",
        "### PQ Results"
    ]
    for i, s in scores["pq"].items():
        emoji = "✅" if s["score"] == 2 else "⚠️" if s["score"] == 1 else "❌"
        body_lines.append(f"- {emoji} PQ{i}: {s['score']}/2 — {s['feedback']}")

    body_lines.append("\n### HW Results")
    for i, s in scores["hw"].items():
        emoji = "✅" if s["score"] == 2 else "⚠️" if s["score"] == 1 else "❌"
        body_lines.append(f"- {emoji} HW{i}: {s['score']}/2 — {s['feedback']}")

    if scores["sql"]:
        body_lines.append("\n### SQL Results")
        for i, s in scores["sql"].items():
            emoji = "✅" if s["score"] == 2 else "⚠️" if s["score"] == 1 else "❌"
            body_lines.append(f"- {emoji} SQL{i}: {s['score']}/2 — {s['feedback']}")

    if missed_deadlines:
        body_lines.append(f"\n### ⚠️ Missed Deadlines")
        for d in missed_deadlines:
            body_lines.append(f"- {d}")
        body_lines.append("\nPlease catch up and push your notebook ASAP!")

    body_lines.append(f"\n### 📅 Next Up: Day {day + 1}")
    body_lines.append("Questions have been auto-injected into your checklist MD file.")

    payload = json.dumps({
        "title": title,
        "body": "\n".join(body_lines),
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
            print(f"  ✅ GitHub Issue created: {issue.get('html_url', '')}")
    except Exception as e:
        print(f"  ⚠️  Failed to create GitHub Issue: {e}")


# ─────────────────────────────────────────────
# DEADLINE CHECKER
# ─────────────────────────────────────────────
def check_deadlines(nb_path: str, content: dict) -> list:
    """Check if deadlines were missed based on file timestamps."""
    missed = []
    nb_file = Path(nb_path)

    if not nb_file.exists():
        return ["Notebook not found"]

    modified_time = datetime.fromtimestamp(nb_file.stat().st_mtime)
    now = datetime.now()

    # Check if videos section exists (proxy for 10:30 PM deadline)
    if not content["videos_marked"]:
        missed.append("Videos not marked complete by 10:30 PM")

    # Check HW completion (5 PM next day)
    hw_complete = len(content["hw_answers"]) >= 3  # at least 3 HW done
    if not hw_complete:
        missed.append("HW not complete by 5:00 PM next day")

    return missed


# ─────────────────────────────────────────────
# WEEKEND HANDLER
# ─────────────────────────────────────────────
def is_weekend() -> bool:
    return datetime.now().weekday() >= 5  # 5=Sat, 6=Sun


def get_weekend_message() -> str:
    day = datetime.now().strftime("%A")
    return f"🌅 It's {day}! Weekend mode — lighter workload today. Focus on {WEEKEND_PQ_COUNT} PQ + {WEEKEND_HW_COUNT} HW. Take breaks!"


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
def main():
    if len(sys.argv) < 2:
        print("Usage: python analyse_notebook.py <day_number>")
        sys.exit(1)

    day = int(sys.argv[1])
    nb_path = f"{NOTEBOOKS_DIR}/day_{day}/day_{day}.ipynb"

    print(f"\n{'='*50}")
    print(f"  📓 Analysing Day {day} notebook")
    print(f"{'='*50}\n")

    # Weekend check
    if is_weekend():
        print(get_weekend_message())

    # Check notebook exists
    if not Path(nb_path).exists():
        print(f"  ❌ Notebook not found: {nb_path}")
        print(f"  Expected path: {nb_path}")
        create_github_issue(day, {"pq": {}, "hw": {}, "sql": {}, "total": 0, "max_total": 10},
                          ["Notebook not submitted"])
        sys.exit(1)

    # Extract content
    print(f"  📖 Extracting notebook content...")
    content = extract_notebook_content(nb_path)
    print(f"  Found: {len(content['pq_answers'])} PQ, {len(content['hw_answers'])} HW, {len(content['sql_answers'])} SQL answers")

    # Check deadlines
    print(f"  ⏰ Checking deadlines...")
    missed = check_deadlines(nb_path, content)
    if missed:
        print(f"  ⚠️  Missed: {missed}")
    else:
        print(f"  ✅ All deadlines met")

    # Score answers
    print(f"  🤖 Scoring answers with Claude API...")
    scores = score_all_answers(day, content)
    print(f"  Score: {scores['total']}/{scores['max_total']}")

    # Update checklist
    print(f"  📝 Updating checklist MD...")
    update_checklist(day, scores, content)

    # Create GitHub Issue
    print(f"  🐙 Creating GitHub Issue...")
    create_github_issue(day, scores, missed)

    print(f"\n{'='*50}")
    print(f"  ✅ Day {day} analysis complete!")
    print(f"  Score: {scores['total']}/{scores['max_total']}")
    print(f"  Next day questions injected into checklist")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()

