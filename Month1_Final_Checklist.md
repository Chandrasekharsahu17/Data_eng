# 📅 Month 1 — Big Data Engineering Daily Checklist

> **Goal:** Complete Python (remaining) + Big Data Fundamentals + Hadoop + HDFS + MapReduce + YARN
> **Daily Time:** 2–3 hours
> **Started:** Completed Python up to #25 Functions In Python + #58 What is Big Data (1 video)
> **Python Practice:** Daily Days 1–14 → 3x/week Days 15–30
> **SQL Practice:** On no-Python days throughout the month (2 questions/day)
> **Tests:** Day 10, Day 20, Day 30 (mix of coding + theory)

-----

## 📊 Month 1 Progress Tracker

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

## ✅ Day 1 — Videos Watched ✅

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

**📓 Notes & Code:** See `notebooks/day_1/day_1.ipynb`

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

**📓 Notes & Code:** See `notebooks/day_2/day_2.ipynb`

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

- [ ] **PQ1:** What is the difference between open(file, ‘r’), ‘w’, ‘a’, and ‘rb’? When do you use each?
- [ ] **PQ2:** What does `with open(...) as f` do? Why is it better than manually calling f.close()?
- [ ] **PQ3:** What is the difference between pathlib.Path and os.path? Which is more modern?
- [ ] **PQ4:** What is the purpose of try/except/finally? Write a skeleton showing all three blocks.
- [ ] **PQ5:** When would you use `except ValueError` instead of `except Exception`? Why is catching all exceptions bad practice?

**📝 Homework (5)**

- [ ] **HW1:** Write a word frequency counter: read any .txt file, count each word, write top 10 most frequent to a new file.
- [ ] **HW2:** Write a safe file reader that handles FileNotFoundError and PermissionError separately with clear different messages.
- [ ] **HW3:** Use pathlib to: check if path exists, get filename without extension, get parent directory, list all .csv files recursively.
- [ ] **HW4:** Script that reads a file line by line — if any line causes error, log the line number and error to errors.log and continue.
- [ ] **HW5 — 🔀 Mixed:** Write safe_write(filepath, data) that writes data, reads it back to verify, raises custom WriteVerificationError if content doesn’t match.

**🗄️ SQL Questions (2) — GROUP BY, HAVING, Aggregates**

- [ ] **SQL1:** Table orders(order_id, customer_id, amount, city). Find cities where total order amount exceeds 10000, ordered by total DESC.
- [ ] **SQL2:** What is the difference between WHERE and HAVING? Fix this broken query: `SELECT department, COUNT(*) FROM employees HAVING COUNT(*) > 5 WHERE salary > 50000`

**📓 Notes & Code:** See `notebooks/day_3/day_3.ipynb`

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 4

> **Theme:** OOP + Inheritance
> **🐍 Python today**

**📹 Videos**

- [ ] #35 OOPS In Python (23min)
- [ ] #36 Inheritance In Python (19min)

**💡 Practice Questions (5)**

- [ ] **PQ1:** What are the 4 pillars of OOP? Define each in one sentence.
- [ ] **PQ2:** What is self in a Python class? Why do you always pass it as the first argument?
- [ ] **PQ3:** What is the difference between a class attribute and an instance attribute? Show with code.
- [ ] **PQ4:** What does super() do in inheritance? When and why do you use it?
- [ ] **PQ5:** What is MRO (Method Resolution Order)? What does Python do when two parent classes have the same method?

**📝 Homework (5)**

- [ ] **HW1:** Create BankAccount class with deposit(), withdraw(), get_balance(). Prevent negative balance with custom InsufficientFundsError.
- [ ] **HW2:** Create SavingsAccount that inherits BankAccount and adds interest_rate and apply_interest() method.
- [ ] **HW3:** Create DataPipeline base class with extract(), transform(), load(). Create CSVPipeline and JSONPipeline subclasses.
- [ ] **HW4:** Demonstrate MRO with diamond inheritance: A→B, A→C, B+C→D. Show which method gets called and why.
- [ ] **HW5 — 🔀 Mixed:** Model a Big Data cluster with OOP: Cluster, Node, NameNode(Node), DataNode(Node). Cluster has add_node(), get_active_nodes(), simulate_failure(node_id).

**📓 Notes & Code:** See `notebooks/day_4/day_4.ipynb`

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

- [ ] **PQ1:** What is polymorphism? Give a real example with two classes that have the same method name but different behaviour.
- [ ] **PQ2:** What is the difference between _single_underscore and __double_underscore in Python? What does name mangling do?
- [ ] **PQ3:** How does @property work? Write a class where setting an attribute validates the value.
- [ ] **PQ4:** What is the difference between an abstract class and a regular class? What happens if you instantiate an abstract class?
- [ ] **PQ5:** What does ABC from the abc module do? Write a minimal example.

**📝 Homework (5)**

- [ ] **HW1:** Build Shape hierarchy: abstract base with area(). Implement Circle, Rectangle, Triangle. Call area() on a mixed list.
- [ ] **HW2:** Create DataRecord class with @property for age (must be 0-150) and email (must contain @). Raise ValueError on invalid input.
- [ ] **HW3:** Write a Singleton pattern for DatabaseConnection — only one instance should ever exist no matter how many times called.
- [ ] **HW4:** Create abstract Connector class with connect(), query(sql), close(). Implement SQLConnector and a fake HDFSConnector.
- [ ] **HW5 — 🔀 Mixed:** Why is encapsulation critical in distributed systems? Write ClusterConfig class that hides internal connection details.

**📓 Notes & Code:** See `notebooks/day_5/day_5.ipynb`

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

- [ ] **PQ1:** Name 5 dunder/magic methods and what each controls. Which one is called when you do len(obj)?
- [ ] **PQ2:** What is the difference between **str** and **repr**? When does Python use each automatically?
- [ ] **PQ3:** How do you create a custom exception? Why create one instead of using ValueError?
- [ ] **PQ4:** Which arithmetic operators can be overloaded in Python? What method name does + map to?
- [ ] **PQ5:** What do **enter** and **exit** do? What Python statement uses them?

**📝 Homework (5)**

- [ ] **HW1:** Build Matrix class that supports +, -, * (element-wise) via operator overloading. Implement **str** to print it nicely.
- [ ] **HW2:** Create context manager class Timer using **enter** and **exit** that prints how long a code block took.
- [ ] **HW3:** Create custom exception hierarchy: PipelineError as base, then ExtractionError, TransformationError, LoadError as children.
- [ ] **HW4:** Implement **len**, **getitem**, **contains** on a custom DataSet class wrapping a list.
- [ ] **HW5 — 🔀 Mixed:** Implement a mini DataFrame class supporting df[‘column’] (getitem), len(df) (len), and str(df) (str) for a dict of columns.

**📓 Notes & Code:** See `notebooks/day_6/day_6.ipynb`

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 7

> **Theme:** Iterators + Generators + Week 1 Review
> **🐍 Python today**

**📹 Videos**

- [ ] #43 Iterators In Python (6min)
- [ ] #44 Generators In Python (11min)

**💡 Practice Questions (5)**

- [ ] **PQ1:** What are the two methods that make an object an iterator? Write a class-based iterator for even numbers.
- [ ] **PQ2:** What is the difference between return and yield? What type does a generator function return?
- [ ] **PQ3:** What is lazy evaluation? Why does it save memory compared to returning a full list?
- [ ] **PQ4:** What does yield from do? How is it different from a regular yield?
- [ ] **PQ5:** What happens when a generator is exhausted? What error do you get if you call next() on it?

**📝 Homework (5)**

- [ ] **HW1:** Write a generator that yields Fibonacci numbers up to N — never stores the full sequence in memory.
- [ ] **HW2:** Compare memory: list of 10 million numbers vs a generator. Use sys.getsizeof to show the difference.
- [ ] **HW3:** Build a data pipeline using only generators: read_lines(file) → filter_empty(lines) → parse_csv(lines). Chain them.
- [ ] **HW4:** Write an infinite counter generator counter(start, step) that yields numbers forever.
- [ ] **HW5 — 🔀 Mixed:** Simulate Spark lazy evaluation: LazyPipeline class where .map() and .filter() only execute when .collect() is called.

**📓 Notes & Code:** See `notebooks/day_7/day_7.ipynb`

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

- [ ] **PQ1:** What is a decorator and what problem does it solve? Why use functools.wraps inside one?
- [ ] **PQ2:** What is the difference between a decorator with arguments and one without? Show the structure of each.
- [ ] **PQ3:** What is a NumPy array? How is it different from a Python list? Name 3 advantages.
- [ ] **PQ4:** What is broadcasting in NumPy? Show an example adding a scalar to an array and two different-shaped arrays.
- [ ] **PQ5:** What is the difference between np.dot() and element-wise * multiplication?

**📝 Homework (5)**

- [ ] **HW1:** Write @timer decorator that prints the function name and how long it took to run.
- [ ] **HW2:** Write @retry(n) decorator that retries the function up to n times on exception, then re-raises.
- [ ] **HW3:** Write @validate_args decorator that checks all arguments are positive numbers — raises ValueError if not.
- [ ] **HW4:** Create a 5x5 NumPy matrix of random integers. Compute: transpose, row sums, column means, index of max value.
- [ ] **HW5 — 🔀 Mixed:** Generate two arrays of 1M random floats, multiply element-wise using NumPy, compare timing vs Python loop.

**📓 Notes & Code:** See `notebooks/day_8/day_8.ipynb`

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

**📓 Notes & Code:** See `notebooks/day_9/day_9.ipynb`

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 10 — 🧪 TEST DAY

> **Theme:** Data Sources + SQLite + Logging + TEST
> **🐍 Python today**

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

**📓 Notes & Code:** See `notebooks/day_10/day_10.ipynb`

**⏱️ Time Spent:** `___` mins

### 🧪 DAY 10 TEST — Python Foundations

> No notes. 45 minutes max.

**Theory (5)**

- [ ] **T1:** What is the difference between **str** and **repr**? When does Python use each automatically?
- [ ] **T2:** Explain lazy evaluation. Give one Python example and one Big Data example.
- [ ] **T3:** What is the difference between an iterator and a generator? Which is more memory efficient and why?
- [ ] **T4:** What does @property do? Why use it instead of a regular method?
- [ ] **T5:** What is the difference between try/except/else and try/except/finally? When does the else block run?

**Coding (5)**

- [ ] **C1:** Write a @retry(n) decorator that retries a function n times on exception before finally raising
- [ ] **C2:** Write a generator that yields only prime numbers up to N
- [ ] **C3:** Create a class Stack with push, pop, peek, is_empty — implement **len** and **str**
- [ ] **C4:** Use map() + filter() + lambda in one pipeline: from a list of numbers, keep only odds → square them → keep only those > 50
- [ ] **C5:** Write a context manager class FileHandler using **enter** and **exit** that safely opens and closes a file

**🎯 Test Score:** `___/10`
**📋 Feedback:** *(paste here)*

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

- [ ] **SQL1:** *(sent daily)*
- [ ] **SQL2:** *(sent daily)*

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

- [ ] **SQL1:** *(sent daily)*
- [ ] **SQL2:** *(sent daily)*

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

- [ ] **SQL1:** *(sent daily)*
- [ ] **SQL2:** *(sent daily)*

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

- [ ] **SQL1:** *(sent daily)*
- [ ] **SQL2:** *(sent daily)*

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 20 — 🧪 TEST DAY

> **Theme:** Exploring Cluster + GCP Best Practices + Linux Commands 1 + TEST

**📹 Videos**

- [ ] #87 Exploring our Hadoop Cluster (24min)
- [ ] #88 GCP Cluster Best Practices (4min)
- [ ] #89 Linux Commands -1 (32min)

### 🧪 DAY 20 TEST

**Theory (5)**

- [ ] **T1:** What is the ACTUAL role of the Secondary NameNode?
- [ ] **T2:** Walk through the HDFS write process step by step — minimum 6 steps
- [ ] **T3:** What are the 5 V’s of Big Data? Give a real-world example for each
- [ ] **T4:** What is the difference between ETL and ELT? When would a company choose ELT?
- [ ] **T5:** What is rack awareness in HDFS and why does it exist?

**Coding (5)**

- [ ] **C1:** Write Python class HDFSSimulator with write_file(name, size_mb), get_blocks(name), get_replicas(block_id)
- [ ] **C2:** Write a Python generator that reads a large file in chunks of N bytes and yields each chunk
- [ ] **C3:** Write a decorator @log_execution that logs function name, arguments, return value, and time taken to a .log file
- [ ] **C4:** Build a mini ETL: read CSV → filter rows where numeric column > 100 → write cleaned output → log every step
- [ ] **C5:** Write a function that takes a directory path and returns {filename: size_in_kb} for all files recursively using pathlib

**🗄️ SQL (2)**

- [ ] **SQL1:** Write a query using a window function to rank employees by salary within each department
- [ ] **SQL2:** Find all customers who placed more than 3 orders — use a subquery AND rewrite using a CTE

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

- [ ] **SQL1:** *(sent daily)*
- [ ] **SQL2:** *(sent daily)*

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

- [ ] **SQL1:** *(sent daily)*
- [ ] **SQL2:** *(sent daily)*

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

- [ ] **SQL1:** *(sent daily)*
- [ ] **SQL2:** *(sent daily)*

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

- [ ] **SQL1:** *(sent daily)*
- [ ] **SQL2:** *(sent daily)*

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 29

> **Theme:** Month 1 Mini Project
> **🐍 Full Python day**

Build a Python data pipeline that:

- [ ] Reads a CSV file using Pandas
- [ ] Cleans the data (drop nulls, fix types, rename columns)
- [ ] Transforms it (filter rows, group by, aggregate)
- [ ] Writes output to a new CSV
- [ ] Every stage decorated with @timer and @retry(3)
- [ ] Full logging: each step logs to both console and a .log file
- [ ] Built using a class Pipeline with proper OOP structure
- [ ] Has a README.md explaining what the pipeline does

**📓 GitHub Link:** `___`

**⏱️ Time Spent:** `___` mins

-----

## ✅ Day 30 — 🧪 FINAL TEST DAY

### 🧪 DAY 30 TEST — Full Month 1 Graduation

> No notes. 75 minutes max. Need 7/10 to move to Month 2.

**Theory (5)**

- [ ] **T1:** Explain the full YARN job submission process step by step — minimum 8 steps
- [ ] **T2:** What is the difference between a Combiner and a Reducer? When should you NOT use a Combiner?
- [ ] **T3:** What is the difference between repartition and coalesce in Spark?
- [ ] **T4:** Walk through what happens when a DataNode permanently fails — what does the NameNode do step by step?
- [ ] **T5:** What is the Medallion Architecture (Bronze/Silver/Gold)? Explain with an example.

**Coding (5)**

- [ ] **C1:** Write a complete Python OOP-based ETL class: extract() reads CSV, transform() filters + renames, load() writes output — add @timer to each method
- [ ] **C2:** Write a generator function log_reader(filepath) that reads a log file line by line, yields only ERROR lines, skips blank lines
- [ ] **C3:** Implement PriorityQueue class using heapq with push(priority, item) and pop() — explain how this simulates YARN job scheduler
- [ ] **C4:** Write simulate_mapreduce(text): map phase (word → (word,1)), shuffle phase (group by word), reduce phase (sum counts)
- [ ] **C5:** Write a script that finds all .csv files recursively, reads each with Pandas, combines into one DataFrame, saves to combined_output.csv with full logging

**SQL (2)**

- [ ] **SQL1:** orders(order_id, customer_id, amount, order_date). Show each customer’s total spend, number of orders, average order value, and rank by total spend — all in one query
- [ ] **SQL2:** Find customers who placed an order in January but NOT in February — use both subquery and LEFT JOIN approaches

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

*📌 Come back every day. Bring your code. Claude reviews and keeps you on track.*
*🧪 Tests on Day 10, 20, 30 — no skipping.*
*💪 Strong logic + daily consistency = you will crush this.*
