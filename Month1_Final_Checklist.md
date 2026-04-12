# 📅 Month 1 — Big Data Engineering Daily Checklist

> **Goal:** Complete Python (remaining) + Big Data Fundamentals + Hadoop + HDFS + MapReduce + YARN
> **Daily Time:** 2–3 hours
> **Tests:** Day 10, Day 20, Day 30

-----

## ✅ Day 1 — DONE ✅

> **Theme:** Function Examples + Lambda + Map | **Score: Full marks** | **⏱️ 90 mins**

- [x] All 3 videos watched
- [x] All 5 PQs done
- [x] All 5 HWs done

### 📖 Day 1 Quick Revision — Lambda + Map + Functions

- `*args` — packs any number of positional arguments into a tuple inside the function
- `**kwargs` — packs keyword arguments into a dict (e.g. `func(name="Ravi")`)
- Lambda syntax: `lambda args: single_expression` — can only have ONE expression, no statements
- Use regular `def` when: multiple lines of logic, loops, try/except, or need a docstring
- Use `lambda` when: short one-liner, passed inline to another function like `map()` or `sorted()`
- `map(func, iterable)` — applies function to every element, returns a **map object** (lazy)
- Always wrap in `list()` to see results: `list(map(lambda x: x**2, [1,2,3]))`
- `map()` with two lists: `list(map(lambda x,y: x+y, a, b))` — zips and applies
- `sorted(lst, key=lambda x: x[-1])` — sorts by last character of each string
- Default argument in lambda: `lambda x, y=10: x + y` — y uses 10 if not passed
- `pipeline(data, *funcs)` — the fix: use `data = func(data)` not `data = func(original)` in loop
- Returning multiple values from a function returns a **tuple**: `return a, b` → `(a, b)`
- `map()` is like a for loop but functional — no mutation, returns a new iterable
- In MapReduce, Python’s `map()` mirrors the Mapper — each element processed independently
- Clean code habit: always call your function with edge cases (empty list, zero, None)

-----

## ✅ Day 2 — DONE ✅

> **Theme:** Filter + Modules + Standard Library | **Score: 37/60** | **⏱️ 40 mins**

- [x] All 3 videos watched
- [x] PQ1 [5/5] PQ2 [3/5] PQ3 [4/5] PQ4 [5/5] PQ5 [0/5]
- [x] HW1 [3/5] HW2 [5/5] HW3 [0/5] HW4 [5/5] HW5 [0/5]
- [x] SQL1 [2/5] SQL2 [5/5]

### 📖 Day 2 Quick Revision — Filter + Modules + Standard Library

- `filter(func, iterable)` — keeps elements where func returns True, returns a **filter object** (lazy)
- Wrap in `list()`: `list(filter(lambda x: x > 0, nums))`
- `filter(None, lst)` — removes all falsy values: `0, "", None, [], False` in one shot
- `filter()` = WHERE clause in SQL — removes what you don’t need before processing
- `import math` → use as `math.sqrt(16)` — loads entire module, access via dot notation
- `from math import sqrt` → use as `sqrt(16)` — imports only that function, no prefix needed
- Prefer `import math` when using many math functions; prefer `from math import x` for just one
- `random.choice(lst)` — picks one random element
- `random.shuffle(lst)` — shuffles list **in place** (modifies original, returns None)
- `random.randint(a, b)` — random integer inclusive of both ends
- `os.path.join("folder", "file.txt")` → `folder/file.txt` on Mac, `folder\file.txt` on Windows
- String concatenation `"folder" + "/" + "file.txt"` breaks on Windows — always use os.path.join
- `collections.Counter(lst)` — counts frequency of each element, returns dict-like object
- `collections.defaultdict(list)` — dict that auto-creates empty list for new keys, no KeyError
- One-liner pipeline: `list(map(lambda x: x**2, filter(lambda x: x%2!=0, lst)))`
- SQL: `WHERE` filters rows before aggregation; `HAVING` filters groups after aggregation
- SQL: Always include the department filter AND the salary condition — read questions twice

-----

## ✅ Day 3 — PARTIAL (fever) ✅

> **Theme:** File Operations + File Paths + Exception Handling | **Score: 23/60** | **⏱️ 90 mins**
> ⚠️ Video #34 + pending HWs carried to Day 4

- [x] #32 ✅ #33 ✅ #34 ❌ carry to Day 4
- [x] PQ1 [5/5] PQ2 [2/5] PQ3 [2/5] PQ4 [0/5 pending] PQ5 [0/5 pending]
- [x] HW1 [4/5] HW2-HW5 [pending]
- [x] SQL1 [5/5] SQL2 [5/5] ← PERFECT SQL DAY 🌟

### 📖 Day 3 Quick Revision — Files + Paths + Exceptions

- `open(file, 'r')` — read only, error if file missing
- `open(file, 'w')` — write, **overwrites entire file** if it exists
- `open(file, 'a')` — append, adds to end without deleting existing content
- `open(file, 'rb')` — read binary (images, PDFs, non-text files)
- Always use `with open(...) as f:` — auto-closes file even if error occurs mid-way
- Without `with`, if exception occurs before `f.close()`, file stays open (resource leak)
- `f.read()` — reads entire file as one string
- `f.readlines()` — reads all lines into a list
- `for line in f:` — reads line by line (memory efficient for large files)
- `pathlib.Path("folder/file.txt")` — modern cross-platform path (preferred over os.path)
- `Path("data/sales.csv").stem` → `"sales"` (filename without extension)
- `Path("data/sales.csv").parent` → `"data"` (parent directory)
- `Path("folder").exists()` — True/False if path exists
- `Path("folder").rglob("*.csv")` — finds all .csv files recursively in all subfolders
- `try` → runs code that might fail
- `except FileNotFoundError` → catches only that specific error (best practice)
- `except Exception` → catches everything — BAD, hides real bugs
- `else` → runs ONLY if no exception occurred in try
- `finally` → ALWAYS runs, error or not — use for cleanup (close connections, log status)
- Custom exception: `class MyError(Exception): pass` — then `raise MyError("message")`
- SQL: `GROUP BY city` + `HAVING SUM(amount) > 10000` — filter happens AFTER grouping
- SQL: `COUNT(id)` counts rows; `AVG(salary)` averages; always pair with GROUP BY

-----

## ✅ Day 4 — CURRENT

> **Theme:** Finish Day 3 + OOP + Inheritance
> **🐍 Python today**

**📹 Videos**

- [ ] #34 Exception Handling In Python (25min) ← finish Day 3 first
- [ ] #35 OOPS In Python (23min)
- [ ] #36 Inheritance In Python (19min)

**🔁 Day 3 Pending — do these first**

- [ ] PQ4: try/except/else/finally skeleton with comments on when each runs
- [ ] PQ5: Fix the bad `except Exception` code and explain why
- [ ] HW2: safe_read(filepath) — FileNotFoundError and PermissionError handled separately
- [ ] HW3: collections.Counter + defaultdict
- [ ] HW5: read_errors_only(filepath) using filter() + exception handling

**💡 Day 4 Practice Questions (5)**

- [ ] **PQ1:** What are the 4 pillars of OOP? Define each in one sentence.
- [ ] **PQ2:** What is self? Why pass it as first argument? What happens if you forget it?
- [ ] **PQ3:** Class attribute vs instance attribute — write Employee class showing both.
- [ ] **PQ4:** What does super() do? Write Manager inheriting from Employee using super().
- [ ] **PQ5:** What is MRO? Write D(B,C) example and print D.**mro** to prove it.

**📝 Day 4 Homework (5)**

- [ ] **HW1:** BankAccount class with deposit(), withdraw(), get_balance(). Custom InsufficientFundsError.
- [ ] **HW2:** SavingsAccount inheriting BankAccount. Add interest_rate and apply_interest().
- [ ] **HW3:** DataPipeline base class. CSVPipeline and JSONPipeline override extract/transform/load.
- [ ] **HW4:** MRO diamond — A, B(A), C(A), D(B,C). Prove which hello() gets called.
- [ ] **HW5 — 🔀 Mixed:** OOP cluster — Node, NameNode(Node), DataNode(Node), Cluster class.

**📓 Notebook:** notebooks/day_4/day_4.ipynb
**⏱️ Time Spent:** ___ mins

-----

## ✅ Day 5

> **Theme:** Polymorphism + Encapsulation + Abstraction

**📹 Videos**

- [ ] #37 Polymorphism In Python (19min)
- [ ] #38 Encapsulation In Python (22min)
- [ ] #39 Abstraction In Python (9min)

**💡 PQs (5)** — [ ] PQ1: [ ] PQ2: [ ] PQ3: [ ] PQ4: [ ] PQ5:
**📝 HWs (5)** — [ ] HW1: [ ] HW2: [ ] HW3: [ ] HW4: [ ] HW5:
**⏱️ Time Spent:** ___ mins

-----

## ✅ Day 6

> **Theme:** Magic Methods + Custom Exceptions + Operator Overloading

**📹 Videos**

- [ ] #40 Magic Methods In Python (8min)
- [ ] #41 Custom Exception In Python (7min)
- [ ] #42 Operator Overloading In Python (9min)

**💡 PQs (5)** — [ ] PQ1: [ ] PQ2: [ ] PQ3: [ ] PQ4: [ ] PQ5:
**📝 HWs (5)** — [ ] HW1: [ ] HW2: [ ] HW3: [ ] HW4: [ ] HW5:
**⏱️ Time Spent:** ___ mins

-----

## ✅ Day 7

> **Theme:** Iterators + Generators + Week 1 Review

**📹 Videos**

- [ ] #43 Iterators In Python (6min)
- [ ] #44 Generators In Python (11min)

**💡 PQs (5)** — [ ] PQ1: [ ] PQ2: [ ] PQ3: [ ] PQ4: [ ] PQ5:
**📝 HWs (5)** — [ ] HW1: [ ] HW2: [ ] HW3: [ ] HW4: [ ] HW5:
**⏱️ Time Spent:** ___ mins

**🏁 Week 1 Self-Check**

- [ ] Can I write a class with inheritance without help?
- [ ] Can I use map / filter / lambda confidently?
- [ ] Can I handle exceptions and file I/O cleanly?
- [ ] Do I understand the difference between iterator and generator?
- [ ] Can I write basic SQL SELECT, WHERE, GROUP BY, HAVING queries?

-----

# WEEK 2

## ✅ Day 8 — Decorators + NumPy

**📹** [ ] #45 (21min) [ ] #46 (28min) | **💡 PQs** [ ]x5 | **📝 HWs** [ ]x5 | **⏱️** ___ mins

## ✅ Day 9 — Pandas DataFrame + Data Manipulation

**📹** [ ] #47 (29min) [ ] #48 (25min) | **💡 PQs** [ ]x5 | **📝 HWs** [ ]x5 | **⏱️** ___ mins

## ✅ Day 10 — 🧪 TEST DAY

**📹** [ ] #49 [ ] #50 [ ] #51 | **💡 PQs** [ ]x5 | **📝 HWs** [ ]x5
**🧪 TEST — Questions given on Day 10** | **🎯 Score:** ___/10 | **⏱️** ___ mins

## ✅ Day 11 — Logging + Big Data Intro

**📹** [ ] #52 [ ] #53 [ ] #54 [ ] #57 [ ] #58 ✅already | **💡 PQs** [ ]x5 | **📝 HWs** [ ]x5 | **⏱️** ___ mins

## ✅ Day 12 — 5 Vs + Distributed Systems (No Python | SQL — JOINs)

**📹** [ ] #59 [ ] #60 [ ] #61 | **💡 PQs** [ ]x5 | **📝 HWs** [ ]x5 | **🗄️ SQL** [ ]x2 | **⏱️** ___ mins

## ✅ Day 13 — On-Prem vs Cloud + DB vs DW vs Lake

**📹** [ ] #62 [ ] #63 | **💡 PQs** [ ]x5 | **📝 HWs** [ ]x5 | **⏱️** ___ mins

## ✅ Day 14 — ETL vs ELT + Hadoop Intro

**📹** [ ] #64 [ ] #65 [ ] #66 [ ] #67 | **💡 PQs** [ ]x5 | **📝 HWs** [ ]x5 | **⏱️** ___ mins

**🏁 Week 2 Self-Check**

- [ ] Can I write a decorator without help?
- [ ] Can I do basic NumPy + Pandas from memory?
- [ ] Can I explain the 5 Vs with real examples?
- [ ] Do I understand ETL vs ELT?
- [ ] Can I write SQL JOINs?

-----

# WEEK 3

## ✅ Day 15 — Hadoop Ecosystem + HDFS Intro (No Python | SQL — Subqueries)

**📹** [ ] #68 [ ] #69 [ ] #70 [ ] #71 | **💡 PQs** [ ]x5 | **📝 HWs** [ ]x5 | **🗄️ SQL** [ ]x2 | **⏱️** ___ mins

## ✅ Day 16 — HDFS Architecture + Blocks + Replication

**📹** [ ] #72 [ ] #73 [ ] #74 [ ] #75 | **💡 PQs** [ ]x5 | **📝 HWs** [ ]x5 | **⏱️** ___ mins

## ✅ Day 17 — Rack Awareness + Node Failure (No Python | SQL — CASE WHEN)

**📹** [ ] #76 [ ] #77 [ ] #78 [ ] #79 | **💡 PQs** [ ]x5 | **📝 HWs** [ ]x5 | **🗄️ SQL** [ ]x2 | **⏱️** ___ mins

## ✅ Day 18 — Permanent Node Failure + HA Architecture

**📹** [ ] #80 [ ] #81 [ ] #82 [ ] #83 | **💡 PQs** [ ]x5 | **📝 HWs** [ ]x5 | **⏱️** ___ mins

## ✅ Day 19 — HDFS Read/Write + GCP Cluster (No Python | SQL — Window Functions)

**📹** [ ] #84 [ ] #85 [ ] #86 | **💡 PQs** [ ]x5 | **📝 HWs** [ ]x5 | **🗄️ SQL** [ ]x2 | **⏱️** ___ mins

## ✅ Day 20 — 🧪 TEST DAY

**📹** [ ] #87 [ ] #88 [ ] #89 | **💡 PQs** [ ]x5 | **📝 HWs** [ ]x5
**🧪 TEST — Questions given on Day 20** | **🎯 Score:** ___/12 | **⏱️** ___ mins

## ✅ Day 21 — Linux Commands + HDFS Commands

**📹** [ ] #90 [ ] #91 [ ] #92 | **💡 PQs** [ ]x5 | **📝 HWs** [ ]x5 | **⏱️** ___ mins

**🏁 Week 3 Self-Check**

- [ ] Can I explain HDFS architecture end-to-end?
- [ ] Do I understand Secondary NameNode vs Standby NameNode?
- [ ] Am I comfortable with Linux + HDFS commands?
- [ ] Do I understand HDFS read/write flow?
- [ ] Can I write SQL window functions?

-----

# WEEK 4

## ✅ Day 22 — MapReduce Concepts (No Python | SQL — CTEs)

**📹** [ ] #93 [ ] #94 [ ] #95 [ ] #96 | **💡 PQs** [ ]x5 | **📝 HWs** [ ]x5 | **🗄️ SQL** [ ]x2 | **⏱️** ___ mins

## ✅ Day 23 — MapReduce Practicals

**📹** [ ] #97 [ ] #98 | **💡 PQs** [ ]x5 | **📝 HWs** [ ]x5 | **⏱️** ___ mins

## ✅ Day 24 — MR Reducers (No Python | SQL — String + Date)

**📹** [ ] #99 [ ] #100 | **💡 PQs** [ ]x5 | **📝 HWs** [ ]x5 | **🗄️ SQL** [ ]x2 | **⏱️** ___ mins

## ✅ Day 25 — Combiner + Zero Reducer + Big Log File

**📹** [ ] #101 [ ] #102 [ ] #103 | **💡 PQs** [ ]x5 | **📝 HWs** [ ]x5 | **⏱️** ___ mins

## ✅ Day 26 — Input Splits + YARN (No Python | SQL — Query Optimization)

**📹** [ ] #104 [ ] #105 [ ] #106 [ ] #107 [ ] #108 | **💡 PQs** [ ]x5 | **📝 HWs** [ ]x5 | **🗄️ SQL** [ ]x2 | **⏱️** ___ mins

## ✅ Day 27 — YARN Analogy + Step by Step

**📹** [ ] #109 [ ] #110 | **💡 PQs** [ ]x5 | **📝 HWs** [ ]x5 | **⏱️** ___ mins

## ✅ Day 28 — Buffer / Catch-Up

- [ ] Re-watch weak videos
- [ ] Redo hardest HW from any previous day
- [ ] Write Month 1 concept summary
- **🗄️ SQL Mixed** [ ]x2 | **⏱️** ___ mins

## ✅ Day 29 — Month 1 Mini Project

- [ ] Reads CSV using Pandas
- [ ] Cleans data (nulls, types, rename)
- [ ] Transforms (filter, group by, aggregate)
- [ ] Writes to new CSV
- [ ] @timer and @retry(3) on each stage
- [ ] Full logging to console + .log file
- [ ] Class Pipeline with OOP structure
- [ ] README.md
- **📓 GitHub Link:** ___ | **⏱️** ___ mins

## ✅ Day 30 — 🧪 FINAL TEST DAY

**🧪 TEST — Questions given on Day 30** | **🎯 Score:** ___/12

-----

## 🏁 Month 1 Final Self-Assessment

|Topic                              |Rating (1–5)|Need More Work?|
|-----------------------------------|------------|---------------|
|Lambda / Map / Filter / Reduce     |            |               |
|File I/O + Exception Handling      |            |               |
|OOP — Classes + Inheritance        |            |               |
|OOP — Magic Methods + Encapsulation|            |               |
|Iterators + Generators             |            |               |
|Decorators                         |            |               |
|NumPy + Pandas basics              |            |               |
|Logging                            |            |               |
|Big Data 5 Vs                      |            |               |
|ETL vs ELT / DB vs DW vs Lake      |            |               |
|Hadoop Ecosystem                   |            |               |
|HDFS Architecture + Read/Write     |            |               |
|NameNode HA                        |            |               |
|MapReduce End-to-End               |            |               |
|YARN Components + Job Flow         |            |               |
|Linux + HDFS Commands              |            |               |
|SQL SELECT / WHERE / GROUP BY      |            |               |
|SQL JOINs                          |            |               |
|SQL Window Functions + CTEs        |            |               |

**Ready for Month 2 when:**

- [ ] Day 30 score >= 7/10
- [ ] SQL done on all SQL days
- [ ] Mini project pushed with README
- [ ] All 110 videos checked
- [ ] No topic rated below 3

-----

*Get well soon. Come back strong for Day 4.*