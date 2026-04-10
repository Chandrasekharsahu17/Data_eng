# 📅 Month 1 — Big Data Engineering Daily Checklist

> **Goal:** Complete Python (remaining) + Big Data Fundamentals + Hadoop + HDFS + MapReduce + YARN
> **Daily Time:** 2–3 hours
> **Python Practice:** Daily Days 1–14 → 3x/week Days 15–30
> **SQL Practice:** On no-Python days (2 questions/day)
> **Tests:** Day 10, Day 20, Day 30

-----

## 📊 Progress Tracker

|Week               |Python Focus                         |Big Data Focus  |SQL            |
|-------------------|-------------------------------------|----------------|---------------|
|Week 1 (Days 1–7)  |Functional + Modules + File I/O + OOP|—               |Days 2, 3      |
|Week 2 (Days 8–14) |Decorators + NumPy + Pandas + Logging|Big Data Intro  |Day 12         |
|Week 3 (Days 15–21)|3x/week                              |Hadoop + HDFS   |Days 15, 17, 19|
|Week 4 (Days 22–30)|3x/week                              |MapReduce + YARN|Days 22, 24, 26|

-----

## 🗓️ SQL Schedule

|Day   |SQL Topic                                      |
|------|-----------------------------------------------|
|Day 2 |SELECT, WHERE, ORDER BY, LIMIT                 |
|Day 3 |GROUP BY, HAVING, aggregate functions          |
|Day 12|JOINs — INNER, LEFT, RIGHT, FULL               |
|Day 15|Subqueries + nested SELECT                     |
|Day 17|CASE WHEN + NULL handling                      |
|Day 19|Window functions — ROW_NUMBER, RANK, DENSE_RANK|
|Day 22|CTEs (WITH clause)                             |
|Day 24|String functions + Date functions              |
|Day 26|Indexes + Query optimization basics            |
|Day 28|SQL revision + mixed practice                  |

-----

# 🗓️ WEEK 1 — Python: Functional Programming + OOP Foundations

-----

## ✅ Day 1 — DONE ✅

> **Theme:** Function Examples + Lambda + Map
> **🐍 Python today**

**📹 Videos**

- [x] #26 Python Function Examples (28min)
- [x] #27 Lambda Functions In Python (10min)
- [x] #28 Map Functions In Python (11min)

**💡 Practice Questions (5)**

- [x] **PQ1:** Write a function using *args that returns the sum of all arguments. Call it with 3 different input combinations.
- [x] **PQ2:** What is the difference between a regular function and a lambda? Write multiply two numbers as both. When would you NOT use a lambda?
- [x] **PQ3:** Use map() with a lambda to cube every number in [1,2,3,4,5,6,7,8,9,10].
- [x] **PQ4:** Sort [Alice, Bob, Charlie, Dan, Eve] by the last character of each name using a lambda inside sorted().
- [x] **PQ5:** What does this output and why? `f = lambda x, y=10: x + y` → `print(f(5))` → `print(f(5, 20))`

**📝 Homework (5)**

- [x] **HW1:** Write apply_operation(lst, func) that applies any function to every element. Test with 3 different lambdas.
- [x] **HW2:** Use map() + lambda to give every employee a 10% salary raise — return full updated dicts.
- [x] **HW3:** Write pipeline(data, *funcs) that chains functions — output of one becomes input of next. Test with 3 lambdas.
- [x] **HW4:** Use map() to convert Celsius [0, 20, 37, 100, -40] to Fahrenheit. Formula: F = (C x 9/5) + 32.
- [x] **HW5 — 🔀 Mixed:** Given a list of sentences, use map() to split each into words. Explain in 3 lines how this connects to Hadoop Mapper.

**📓 Notebook:** `notebooks/day_1/day_1.ipynb`
**⏱️ Time Spent:** `90` mins

-----

## ✅ Day 2

> **Theme:** Filter + Modules + Standard Library
> **🐍 Python today | 🗄️ SQL today**

**📹 Videos**

- [ ] #29 Python Filter Function (9min)
- [ ] #30 Import Modules And Packages (17min)
- [ ] #31 Standard Library Overview (18min)

**💡 Practice Questions (5)**

- [ ] **PQ1:** What does filter() return in Python 3? Write a one-liner using filter() + lambda to keep only even numbers from [1..10].
- [ ] **PQ2:** What is the difference between `import math` and `from math import sqrt`? When would you prefer one over the other?
- [ ] **PQ3:** Use filter() to remove all empty strings from: `["hello", "", "world", "", "python", ""]`
- [ ] **PQ4:** What does random.choice(), random.shuffle(), and random.randint() do? Write one example using each.
- [ ] **PQ5:** What is the difference between os.path.join() and string concatenation for file paths? Why does it matter?

**📝 Homework (5)**

- [ ] **HW1:** Write filter_by_condition(lst, condition_func) — test with 3 lambdas: one for numbers, one for strings, one for dicts.
- [ ] **HW2:** filter() + map() pipeline in one line: [1..10] keep only odds → square them → return as list.
- [ ] **HW3:** Use collections.Counter to count word frequency in: “the cat sat on the mat the cat”. Then defaultdict to group words by first letter.
- [ ] **HW4:** Use datetime module: (a) print today’s date, (b) days since Jan 1 2026, (c) add 30 days to today.
- [ ] **HW5 — 🔀 Mixed:** Given log lines, use filter() to keep only lines with “ERROR”. Explain in 3 lines how this maps to Hadoop pipeline before reduce phase.

**🗄️ SQL Questions (2) — SELECT, WHERE, ORDER BY, LIMIT**

- [ ] **SQL1:** Table employees(id, name, department, salary). Get all in ‘Engineering’ with salary > 60000, ordered by salary DESC, top 5 only.
- [ ] **SQL2:** Find employees whose name starts with ‘A’ OR who earn more than 90000. Use WHERE with LIKE and OR.

**📓 Notebook:** `notebooks/day_2/day_2.ipynb`
**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 3

> **Theme:** File Operations + File Paths + Exception Handling
> **🐍 Python today | 🗄️ SQL today**

**📹 Videos**

- [ ] #32 File Operation In Python (17min)
- [ ] #33 Working With File Paths (9min)
- [ ] #34 Exception Handling In Python (25min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**🗄️ SQL Questions (2) — GROUP BY, HAVING, Aggregates**

- [ ] SQL1:
- [ ] SQL2:

**📓 Notebook:** `notebooks/day_3/day_3.ipynb`
**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 4

> **Theme:** OOP + Inheritance
> **🐍 Python today**

**📹 Videos**

- [ ] #35 OOPS In Python (23min)
- [ ] #36 Inheritance In Python (19min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**📓 Notebook:** `notebooks/day_4/day_4.ipynb`
**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 5

> **Theme:** Polymorphism + Encapsulation + Abstraction
> **🐍 Python today**

**📹 Videos**

- [ ] #37 Polymorphism In Python (19min)
- [ ] #38 Encapsulation In Python (22min)
- [ ] #39 Abstraction In Python (9min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**📓 Notebook:** `notebooks/day_5/day_5.ipynb`
**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 6

> **Theme:** Magic Methods + Custom Exceptions + Operator Overloading
> **🐍 Python today**

**📹 Videos**

- [ ] #40 Magic Methods In Python (8min)
- [ ] #41 Custom Exception In Python (7min)
- [ ] #42 Operator Overloading In Python (9min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**📓 Notebook:** `notebooks/day_6/day_6.ipynb`
**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 7

> **Theme:** Iterators + Generators + Week 1 Review
> **🐍 Python today**

**📹 Videos**

- [ ] #43 Iterators In Python (6min)
- [ ] #44 Generators In Python (11min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**📓 Notebook:** `notebooks/day_7/day_7.ipynb`
**⏱️ Time Spent:** `___` mins

**🏁 Week 1 Self-Check**

- [ ] Can I write a class with inheritance without help?
- [ ] Can I use map / filter / lambda confidently?
- [ ] Can I handle exceptions and file I/O cleanly?
- [ ] Do I understand the difference between iterator and generator?
- [ ] Can I write basic SQL SELECT, WHERE, GROUP BY, HAVING queries?

-----

# 🗓️ WEEK 2 — Python: Advanced + NumPy + Pandas + Logging

-----

## ✅ Day 8

> **Theme:** Decorators + NumPy
> **🐍 Python today**

**📹 Videos**

- [ ] #45 Decorators In Python (21min)
- [ ] #46 Working With Numpy In Python (28min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**📓 Notebook:** `notebooks/day_8/day_8.ipynb`
**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 9

> **Theme:** Pandas DataFrame + Data Manipulation
> **🐍 Python today**

**📹 Videos**

- [ ] #47 Pandas DataFrame And Series (29min)
- [ ] #48 Data Manipulation And Analysis (25min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**📓 Notebook:** `notebooks/day_9/day_9.ipynb`
**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 10 — 🧪 TEST DAY

> **Theme:** Data Sources + SQLite + Logging + TEST

**📹 Videos**

- [ ] #49 Data Source Reading (15min)
- [ ] #50 Python With SQLite (17min)
- [ ] #51 Logging In Python (15min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**🧪 TEST — Questions will be given on Day 10**

**🎯 Test Score:** `___/10`
**📋 Feedback:** *(paste here)*

**📓 Notebook:** `notebooks/day_10/day_10.ipynb`
**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 11

> **Theme:** Logging Deep Dive + Big Data Intro
> **🐍 Python today (3x/week)**

**📹 Videos**

- [ ] #52 Logging With Multiple Loggers (5min)
- [ ] #53 Logging In a Real World Example (8min)
- [ ] #54 Python Outro (1min)
- [ ] #57 Big Data Section Intro (1min)
- [ ] #58 What is Big Data - A Practical Example (18min) ✅ Already watched

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 12

> **Theme:** 5 V’s of Big Data + Distributed Systems + Big Data System Design
> **🐍 No Python today | 🗄️ SQL today**

**📹 Videos**

- [ ] #59 5 V’s of Big Data (22min)
- [ ] #60 Big Data and Distributed Systems (18min)
- [ ] #61 Designing a Good Big Data System (11min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**🗄️ SQL Questions (2) — JOINs**

- [ ] SQL1:
- [ ] SQL2:

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 13

> **Theme:** On-Prem vs Cloud + DB vs DW vs Data Lake
> **🐍 Python today (3x/week)**

**📹 Videos**

- [ ] #62 On-Premise Infra vs Cloud Solutions (20min)
- [ ] #63 Database vs Data Warehouse vs Data Lake (29min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 14

> **Theme:** ETL vs ELT + Data Engineer Role + Hadoop Intro
> **🐍 Python today (3x/week)**

**📹 Videos**

- [ ] #64 ETL vs ELT (22min)
- [ ] #65 What does a Data Engineer do (18min)
- [ ] #66 Hadoop Section Intro (3min)
- [ ] #67 Introduction To Hadoop (6min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**⏱️ Time Spent:** `___` mins

**🏁 Week 2 Self-Check**

- [ ] Can I write a decorator without help?
- [ ] Can I do basic NumPy + Pandas operations from memory?
- [ ] Can I explain the 5 V’s with real examples?
- [ ] Do I understand ETL vs ELT and when to use each?
- [ ] Can I write SQL JOINs confidently?

-----

# 🗓️ WEEK 3 — Hadoop + HDFS Deep Dive

-----

## ✅ Day 15

> **Theme:** Hadoop Ecosystem + HDFS Intro
> **🐍 No Python today | 🗄️ SQL today**

**📹 Videos**

- [ ] #68 Properties of Hadoop (10min)
- [ ] #69 Hadoop Ecosystem - Main Components (9min)
- [ ] #70 Hadoop Ecosystem - Components (29min)
- [ ] #71 Intro to HDFS and Common Terminology (23min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**🗄️ SQL Questions (2) — Subqueries**

- [ ] SQL1:
- [ ] SQL2:

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 16

> **Theme:** HDFS Architecture + Blocks + Replication Factor
> **🐍 Python today (3x/week)**

**📹 Videos**

- [ ] #72 Why HDFS (4min)
- [ ] #73 HDFS Architecture (16min)
- [ ] #74 Blocks In HDFS (12min)
- [ ] #75 Replication Factor in HDFS (10min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 17

> **Theme:** Rack Awareness + Node Failure + GCP Account
> **🐍 No Python today | 🗄️ SQL today**

**📹 Videos**

- [ ] #76 Rack Awareness in HDFS (8min)
- [ ] #77 Node Failure (1min)
- [ ] #78 Create GCP Account (24min)
- [ ] #79 Data Node Failure - Temporary (12min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**🗄️ SQL Questions (2) — CASE WHEN + NULL handling**

- [ ] SQL1:
- [ ] SQL2:

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 18

> **Theme:** Permanent Node Failure + NameNode HA Architecture
> **🐍 Python today (3x/week)**

**📹 Videos**

- [ ] #80 Data Node Failure - Permanent (14min)
- [ ] #81 Secondary Name Node (17min)
- [ ] #82 Standby Name Node (11min)
- [ ] #83 Hadoop HA Architecture (20min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 19

> **Theme:** HDFS Read/Write + GCP Cluster Creation
> **🐍 No Python today | 🗄️ SQL today**

**📹 Videos**

- [ ] #84 Data Write in HDFS (23min)
- [ ] #85 Read Request in HDFS (11min)
- [ ] #86 GCP Hadoop Cluster Creation (29min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**🗄️ SQL Questions (2) — Window Functions**

- [ ] SQL1:
- [ ] SQL2:

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 20 — 🧪 TEST DAY

> **Theme:** Exploring Cluster + GCP Best Practices + Linux Commands 1 + TEST

**📹 Videos**

- [ ] #87 Exploring our Hadoop Cluster (24min)
- [ ] #88 GCP Cluster Best Practices (4min)
- [ ] #89 Linux Commands -1 (32min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**🧪 TEST — Questions will be given on Day 20**

**🎯 Test Score:** `___/12`
**📋 Feedback:** *(paste here)*

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 21

> **Theme:** Linux Commands 2 + HDFS Commands + Hadoop Outro
> **🐍 Python today (3x/week)**

**📹 Videos**

- [ ] #90 Linux Commands -2 (28min)
- [ ] #91 HDFS Commands (30min)
- [ ] #92 Hadoop Outro (2min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**⏱️ Time Spent:** `___` mins

**🏁 Week 3 Self-Check**

- [ ] Can I explain HDFS architecture end-to-end from memory?
- [ ] Do I understand Secondary NameNode vs Standby NameNode clearly?
- [ ] Can I draw the HA architecture with all components?
- [ ] Am I comfortable with basic Linux + HDFS commands?
- [ ] Do I understand HDFS read/write flow step by step?
- [ ] Can I write SQL window functions?

-----

# 🗓️ WEEK 4 — MapReduce + YARN + Final Review

-----

## ✅ Day 22

> **Theme:** MapReduce Concepts + Distributed Processing
> **🐍 No Python today | 🗄️ SQL today**

**📹 Videos**

- [ ] #93 Map Reduce Intro (2min)
- [ ] #94 Intro To Distributed Processing (12min)
- [ ] #95 Map Reduce Introduction (17min)
- [ ] #96 Map Reduce & Cluster (12min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**🗄️ SQL Questions (2) — CTEs**

- [ ] SQL1:
- [ ] SQL2:

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 23

> **Theme:** MapReduce Practicals 1 & 2
> **🐍 Python today (3x/week)**

**📹 Videos**

- [ ] #97 Map Reduce Practical Part 1 (17min)
- [ ] #98 MR Example Part 2 (22min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 24

> **Theme:** MR with 1 Reducer + 2 Reducers
> **🐍 No Python today | 🗄️ SQL today**

**📹 Videos**

- [ ] #99 MR Practical with 1 Reducer (40min)
- [ ] #100 MR with 2 Reducer Practical (29min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**🗄️ SQL Questions (2) — String + Date Functions**

- [ ] SQL1:
- [ ] SQL2:

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 25

> **Theme:** Combiner + Zero Reducer + Big Log File
> **🐍 Python today (3x/week)**

**📹 Videos**

- [ ] #101 Combiner in MR (13min)
- [ ] #102 Map Reduce with 0 Reducer (16min)
- [ ] #103 MR on Big Log File (21min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 26

> **Theme:** Input Splits + YARN Introduction + Components
> **🐍 No Python today | 🗄️ SQL today**

**📹 Videos**

- [ ] #104 Input Split in MR (7min)
- [ ] #105 Map Reduce Outro (2min)
- [ ] #106 YARN Section Intro (1min)
- [ ] #107 YARN Introduction (6min)
- [ ] #108 Components of YARN (22min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**🗄️ SQL Questions (2) — Query Optimization + Indexes**

- [ ] SQL1:
- [ ] SQL2:

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 27

> **Theme:** YARN Analogy + YARN Process Step by Step
> **🐍 Python today (3x/week)**

**📹 Videos**

- [ ] #109 YARN Analogy (6min)
- [ ] #110 YARN Process Step by step (28min)

**💡 Practice Questions (5)**

- [ ] PQ1:
- [ ] PQ2:
- [ ] PQ3:
- [ ] PQ4:
- [ ] PQ5:

**📝 Homework (5)**

- [ ] HW1:
- [ ] HW2:
- [ ] HW3:
- [ ] HW4:
- [ ] HW5:

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 28

> **Theme:** Buffer / Catch-Up / Weak Areas
> **🐍 Python today | 🗄️ SQL revision today**

- [ ] Re-watch any video you rated below 3/5
- [ ] Redo the hardest homework problem from any previous day
- [ ] Write your Month 1 concept summary (one paragraph each)

**🗄️ SQL Questions (2) — Mixed Revision**

- [ ] SQL1:
- [ ] SQL2:

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 29

> **Theme:** Month 1 Mini Project
> **🐍 Full Python day**

- [ ] Reads a CSV file using Pandas
- [ ] Cleans the data (drop nulls, fix types, rename columns)
- [ ] Transforms it (filter rows, group by, aggregate)
- [ ] Writes output to a new CSV
- [ ] Every stage decorated with @timer and @retry(3)
- [ ] Full logging to both console and a .log file
- [ ] Built using a class Pipeline with proper OOP structure
- [ ] Has a README.md

**📓 GitHub Link:** `___`
**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 30 — 🧪 FINAL TEST DAY

**🧪 TEST — Questions will be given on Day 30**

**🎯 Test Score:** `___/12`
**📋 Feedback:** *(paste here)*

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
|Big Data 5 V’s                     |            |               |
|ETL vs ELT / DB vs DW vs Lake      |            |               |
|Hadoop Ecosystem                   |            |               |
|HDFS Architecture + Read/Write     |            |               |
|NameNode HA                        |            |               |
|MapReduce End-to-End               |            |               |
|YARN Components + Job Flow         |            |               |
|Linux + HDFS Commands              |            |               |
|SQL — SELECT / WHERE / GROUP BY    |            |               |
|SQL — JOINs                        |            |               |
|SQL — Window Functions + CTEs      |            |               |

**✅ Ready for Month 2 when:**

- [ ] Day 30 test score ≥ 7/10
- [ ] SQL questions attempted on all SQL days
- [ ] Mini project pushed to GitHub with README
- [ ] All 110 videos checked off
- [ ] No topic rated below 3

-----

*📌 Come back every day. Bring your notebook. I review, score, and give you the next day.*
*🧪 Tests on Day 10, 20, 30 — no skipping.*
*💪 You’ve got this — Day 1 done, 29 to go!*