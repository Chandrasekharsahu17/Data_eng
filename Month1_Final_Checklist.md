# Month 1 - Big Data Engineering Daily Checklist

Goal: Complete Python (remaining) + Big Data Fundamentals + Hadoop + HDFS + MapReduce + YARN
Daily Time: 2-3 hours
Tests: Day 10, Day 20, Day 30

---

## Progress Tracker

Week 1 (Days 1-7)   | Python: Functional + Modules + File IO + OOP | SQL: Days 2, 3
Week 2 (Days 8-14)  | Python: Decorators + NumPy + Pandas + Logging | Big Data Intro | SQL: Day 12
Week 3 (Days 15-21) | Python: 3x/week | Hadoop + HDFS | SQL: Days 15, 17, 19
Week 4 (Days 22-30) | Python: 3x/week | MapReduce + YARN | SQL: Days 22, 24, 26

SQL Schedule:
Day 2  - SELECT, WHERE, ORDER BY, LIMIT
Day 3  - GROUP BY, HAVING, aggregate functions
Day 12 - JOINs
Day 15 - Subqueries
Day 17 - CASE WHEN + NULL handling
Day 19 - Window functions
Day 22 - CTEs
Day 24 - String + Date functions
Day 26 - Indexes + Query optimization
Day 28 - SQL revision

---

## WEEK 1

---

## Day 1 - DONE
Theme: Function Examples + Lambda + Map | Score: Full marks | Time: 90 mins

Videos:
- [x] #26 Python Function Examples (28min)
- [x] #27 Lambda Functions In Python (10min)
- [x] #28 Map Functions In Python (11min)

PQs: [x] All 5 done
HWs: [x] All 5 done

### Day 1 Revision Notes

- *args packs positional arguments into a tuple. **kwargs packs keyword arguments into a dict
- The name args or kwargs does not matter. The * and ** are what matter
- Lambda syntax: lambda args: expression. Only ONE expression allowed, no multiple lines
- Use regular def when: multiple lines, loops, try/except, docstring needed
- Use lambda when: short one-liner passed directly to map() sorted() filter()
- map(func, iterable) applies function to every element and returns a map object (lazy)
- Always wrap in list() to see results: list(map(lambda x: x**2, [1,2,3]))
- map() with two lists: list(map(lambda x,y: x+y, a, b)) zips and applies together
- sorted(lst, key=lambda x: x[-1]) sorts by last character of each string
- Default argument in lambda: lambda x, y=10: x+y uses 10 if second arg not passed
- pipeline() bug fix: use data = func(data) not data = func(original) inside loop
- Returning multiple values returns a tuple. Unpack with: a, b = func(x)
- A function that only prints returns None. If you try to chain it, the next step gets None

---

## Day 2 - DONE
Theme: Filter + Modules + Standard Library | Score: 37/60 | Time: 40 mins

Videos:
- [x] #29 Python Filter Function (9min)
- [x] #30 Import Modules And Packages (17min)
- [x] #31 Standard Library Overview (18min)

PQs:
- [x] PQ1 [5/5] filter() returns filter object, wrapped in list() correctly
- [x] PQ2 [3/5] correct concept, missed when to prefer each
- [x] PQ3 [4/5] works, tip: filter(None, lst) removes all falsy values in one shot
- [x] PQ4 [5/5] correct definitions and examples
- [ ] PQ5 [0/5] not answered - os.path.join() is cross-platform safe, string concat breaks on Windows

HWs:
- [x] HW1 [3/5] function correct, only tested 1 lambda instead of 3
- [x] HW2 [5/5] perfect one-liner
- [ ] HW3 [0/5] skipped - collections Counter and defaultdict
- [x] HW4 [5/5] perfect datetime usage
- [ ] HW5 [0/5] skipped (Hadoop not learned yet)

SQL:
- [x] SQL1 [2/5] missing department filter, salary was 6000 not 60000
- [x] SQL2 [5/5] excellent, used lower() for case-insensitive match

### Day 2 Revision Notes

- filter(func, iterable) keeps elements where func returns True, returns filter object (lazy)
- filter(None, lst) removes all falsy values: 0, empty string, None, False, empty list
- import math loads full library, access with math.sqrt(). Use when you need many functions
- from math import sqrt imports only that function. Use when you need just one thing
- random.choice(lst) picks one random element
- random.shuffle(lst) shuffles list IN PLACE, returns None not a new list
- random.randint(a, b) returns random integer inclusive of both ends
- os.path.join() is cross-platform safe. String concatenation with / breaks on Windows
- Counter(lst) counts frequency of each element automatically
- defaultdict(list) creates empty list automatically for new keys, no KeyError ever
- One-liner: list(map(lambda x: x**2, filter(lambda x: x%2==0, lst)))
- SQL: WHERE filters rows before grouping. HAVING filters groups after grouping
- SQL: Always read the full question before writing. Check every condition required

---

## Day 3 - PARTIAL (had fever)
Theme: File Operations + File Paths + Exception Handling | Score: 23/60 | Time: 90 mins
Note: Video #34 not watched, exception handling pending carried to Day 4

Videos:
- [x] #32 File Operation In Python (17min)
- [x] #33 Working With File Paths (9min)
- [ ] #34 Exception Handling In Python (25min) - carried to Day 4

PQs:
- [x] PQ1 [5/5] proved all 4 file modes with working code
- [x] PQ2 [2/5] basic idea correct, missed the file handle leak danger
- [x] PQ3 [2/5] created Path object, missed .stem and .parent
- [ ] PQ4 [0/5] pending - exception video not watched
- [ ] PQ5 [0/5] pending

HWs:
- [x] HW1 [4/5] correct, tip: use enumerate() not manual counter
- [ ] HW2 [0/5] pending
- [ ] HW3 [0/5] pending
- [ ] HW4 [0/5] pending
- [ ] HW5 [0/5] pending

SQL:
- [x] SQL1 [5/5] GROUP BY + HAVING perfect
- [x] SQL2 [5/5] AVG + COUNT + HAVING perfect - perfect SQL day

### Day 3 Revision Notes

- open(file, 'r') read only. open(file, 'w') write and overwrite. open(file, 'a') append. open(file, 'rb') binary
- Always use with open() as f. It auto-closes the file even if an error crashes the program
- Without with open: if error occurs before f.close(), the file handle stays open in memory forever
- File handle leak in a pipeline processing 10000 files fills OS limit and crashes the entire job
- f.read() loads entire file as one string. Bad for large files
- f.readlines() loads ALL lines into a list in memory at once. Also bad for large files
- for line in f reads ONE line at a time. Good for large files. Use this for 10GB log files
- pathlib.Path is the modern way. Path("data/sales.csv").stem gives sales (no extension)
- Path("data/sales.csv").parent gives data (parent folder)
- Path("folder").exists() returns True or False
- Path("folder").glob("*.csv") lists all csv files in that folder
- Path("folder").rglob("*.csv") lists all csv files recursively in all subfolders
- try runs code that might fail. except catches specific error. else runs only if no error. finally always runs
- Always catch specific exceptions like FileNotFoundError not just Exception
- Catching Exception hides real bugs because it catches everything including things you did not expect
- SQL: GROUP BY groups rows. Aggregate functions work on those groups. HAVING filters the groups

---

## Day 4 - DONE
Theme: Exception Handling (finish Day 3) + OOP + Inheritance | Score: 28/55 | Time: 150 mins

Videos:
- [x] #34 Exception Handling In Python (25min)
- [x] #35 OOPS In Python (23min)
- [x] #36 Inheritance In Python (19min)

PQs: [x] PQ4 [4/5] [x] PQ5 [3/5] - OOP PQ1-PQ5 not attempted
HWs: [ ] HW1 [3/5] [ ] HW2 [5/5] [ ] HW3 [4/5] [ ] HW4 [0/5] [ ] HW5 [0/5]

### Day 4 Revision Notes

- try/except/else/finally: try runs first, except catches specific errors, else runs only if NO error, finally ALWAYS runs
- Order matters: catch specific exceptions before general ones. ValueError before Exception
- If you put Exception first it catches everything and the specific handler below never runs
- Custom exception: class MyError(Exception): pass then raise MyError("message")
- raise actually stops the program and throws the error. print just shows text and continues
- BankAccount bug: condition was amount < self.balance, should be amount > self.balance
- Class is a blueprint. Object is the real thing created from the blueprint
- self means: the specific object calling this method right now
- __init__ runs automatically the moment you create an object. It sets up the object
- Class attribute is shared by ALL objects. Instance attribute belongs to ONE object
- Inheritance: child class gets all methods and attributes of parent automatically
- super().__init__() calls the parent class setup before adding the child's own attributes
- MRO means Method Resolution Order. Python uses left to right depth first when multiple parents
- D(B, C) means Python checks D first, then B, then A, then C. Print D.__mro__ to see the order
- In Data Engineering OOP is everywhere. Every pipeline, connector, and config is a class

---

## Day 5 - CURRENT
Theme: Polymorphism + Encapsulation + Abstraction

Videos:
- [x] #37 Polymorphism In Python (19min)
- [x] #38 Encapsulation In Python (22min)
- [x] #39 Abstraction In Python (9min)

Corrections from Day 4 submission:
- [ ] Fix 1: Q1 function call without unpacking, remove print(z)
- [ ] Fix 2: Q11 explain actual file handle leak danger
- [ ] Fix 3: Q12 readlines vs loop - loop is memory efficient not readlines
- [ ] Fix 4: Q13 enumerate in correct order without reversed()
- [ ] Fix 5: Q14 pathlib only, no os.path

Practice Questions (5):
- [ ] PQ1: Polymorphism in one sentence real life example. Three classes Dog Cat Cow with sound(). Call in loop.
- [ ] PQ2: Difference between _x and __x. Write class with both. Show what happens accessing from outside.
- [ ] PQ3: @property with Temperature class. fahrenheit property converts from celsius. No parentheses when calling.
- [ ] PQ4: Abstract class Shape with area(). Circle and Rectangle implement it. Show TypeError when creating Shape directly.
- [ ] PQ5: Difference between Encapsulation and Abstraction as comments with real life examples.

Homework (5):
- [ ] HW1: Payment system polymorphism. UPIPayment CreditCardPayment CashPayment. checkout() function.
- [ ] HW2: Employee class encapsulation. Private name salary department. give_raise() with validation.
- [ ] HW3: Abstract DataConnector. MySQLConnector and HDFSConnector. run_pipeline() function.
- [ ] HW4: Rectangle class with @property, @setter with validation, area and perimeter properties.
- [ ] HW5: Mini pipeline using all three pillars. Abstract Pipeline. SalesPipeline and LogPipeline. run() with timestamps.

Notebook: notebooks/day_5/day_5.ipynb
Time Spent: ___ mins

---

## Day 6
Theme: Magic Methods + Custom Exceptions + Operator Overloading

Videos:
- [ ] #40 Magic Methods In Python (8min)
- [ ] #41 Custom Exception In Python (7min)
- [ ] #42 Operator Overloading In Python (9min)

PQs: [ ] PQ1: [ ] PQ2: [ ] PQ3: [ ] PQ4: [ ] PQ5:
HWs: [ ] HW1: [ ] HW2: [ ] HW3: [ ] HW4: [ ] HW5:
Time Spent: ___ mins

---

## Day 7
Theme: Iterators + Generators + Week 1 Review

Videos:
- [ ] #43 Iterators In Python (6min)
- [ ] #44 Generators In Python (11min)

PQs: [ ] PQ1: [ ] PQ2: [ ] PQ3: [ ] PQ4: [ ] PQ5:
HWs: [ ] HW1: [ ] HW2: [ ] HW3: [ ] HW4: [ ] HW5:
Time Spent: ___ mins

Week 1 Self-Check:
- [ ] Can I write a class with inheritance without help?
- [ ] Can I use map, filter, lambda confidently?
- [ ] Can I handle exceptions and file IO cleanly?
- [ ] Do I understand the difference between iterator and generator?
- [ ] Can I write basic SQL SELECT WHERE GROUP BY HAVING queries?

---

## WEEK 2

## Day 8 - Decorators + NumPy
Videos: [ ] #45 (21min) [ ] #46 (28min)
PQs: [ ] x5 | HWs: [ ] x5 | Time: ___ mins

## Day 9 - Pandas DataFrame + Data Manipulation
Videos: [ ] #47 (29min) [ ] #48 (25min)
PQs: [ ] x5 | HWs: [ ] x5 | Time: ___ mins

## Day 10 - TEST DAY
Videos: [ ] #49 [ ] #50 [ ] #51
PQs: [ ] x5 | HWs: [ ] x5
TEST - Questions given on Day 10
Score: ___/10 | Time: ___ mins

## Day 11 - Logging + Big Data Intro
Videos: [ ] #52 [ ] #53 [ ] #54 [ ] #57 [ ] #58 already watched
PQs: [ ] x5 | HWs: [ ] x5 | Time: ___ mins

## Day 12 - 5 Vs + Distributed Systems (No Python, SQL day - JOINs)
Videos: [ ] #59 [ ] #60 [ ] #61
PQs: [ ] x5 | HWs: [ ] x5 | SQL: [ ] x2 | Time: ___ mins

## Day 13 - On-Prem vs Cloud + DB vs DW vs Lake
Videos: [ ] #62 [ ] #63
PQs: [ ] x5 | HWs: [ ] x5 | Time: ___ mins

## Day 14 - ETL vs ELT + Hadoop Intro
Videos: [ ] #64 [ ] #65 [ ] #66 [ ] #67
PQs: [ ] x5 | HWs: [ ] x5 | Time: ___ mins

Week 2 Self-Check:
- [ ] Can I write a decorator without help?
- [ ] Can I do basic NumPy and Pandas from memory?
- [ ] Can I explain the 5 Vs with real examples?
- [ ] Do I understand ETL vs ELT?
- [ ] Can I write SQL JOINs?

---

## WEEK 3

## Day 15 - Hadoop Ecosystem + HDFS Intro (No Python, SQL - Subqueries)
Videos: [ ] #68 [ ] #69 [ ] #70 [ ] #71
PQs: [ ] x5 | HWs: [ ] x5 | SQL: [ ] x2 | Time: ___ mins

## Day 16 - HDFS Architecture + Blocks + Replication
Videos: [ ] #72 [ ] #73 [ ] #74 [ ] #75
PQs: [ ] x5 | HWs: [ ] x5 | Time: ___ mins

## Day 17 - Rack Awareness + Node Failure (No Python, SQL - CASE WHEN)
Videos: [ ] #76 [ ] #77 [ ] #78 [ ] #79
PQs: [ ] x5 | HWs: [ ] x5 | SQL: [ ] x2 | Time: ___ mins

## Day 18 - Permanent Node Failure + HA Architecture
Videos: [ ] #80 [ ] #81 [ ] #82 [ ] #83
PQs: [ ] x5 | HWs: [ ] x5 | Time: ___ mins

## Day 19 - HDFS Read Write + GCP Cluster (No Python, SQL - Window Functions)
Videos: [ ] #84 [ ] #85 [ ] #86
PQs: [ ] x5 | HWs: [ ] x5 | SQL: [ ] x2 | Time: ___ mins

## Day 20 - TEST DAY
Videos: [ ] #87 [ ] #88 [ ] #89
PQs: [ ] x5 | HWs: [ ] x5
TEST - Questions given on Day 20
Score: ___/12 | Time: ___ mins

## Day 21 - Linux Commands + HDFS Commands
Videos: [ ] #90 [ ] #91 [ ] #92
PQs: [ ] x5 | HWs: [ ] x5 | Time: ___ mins

Week 3 Self-Check:
- [ ] Can I explain HDFS architecture end to end?
- [ ] Do I understand Secondary NameNode vs Standby NameNode?
- [ ] Am I comfortable with Linux and HDFS commands?
- [ ] Do I understand HDFS read write flow?
- [ ] Can I write SQL window functions?

---

## WEEK 4

## Day 22 - MapReduce Concepts (No Python, SQL - CTEs)
Videos: [ ] #93 [ ] #94 [ ] #95 [ ] #96
PQs: [ ] x5 | HWs: [ ] x5 | SQL: [ ] x2 | Time: ___ mins

## Day 23 - MapReduce Practicals
Videos: [ ] #97 [ ] #98
PQs: [ ] x5 | HWs: [ ] x5 | Time: ___ mins

## Day 24 - MR Reducers (No Python, SQL - String and Date)
Videos: [ ] #99 [ ] #100
PQs: [ ] x5 | HWs: [ ] x5 | SQL: [ ] x2 | Time: ___ mins

## Day 25 - Combiner + Zero Reducer + Big Log File
Videos: [ ] #101 [ ] #102 [ ] #103
PQs: [ ] x5 | HWs: [ ] x5 | Time: ___ mins

## Day 26 - Input Splits + YARN (No Python, SQL - Query Optimization)
Videos: [ ] #104 [ ] #105 [ ] #106 [ ] #107 [ ] #108
PQs: [ ] x5 | HWs: [ ] x5 | SQL: [ ] x2 | Time: ___ mins

## Day 27 - YARN Analogy + Step by Step
Videos: [ ] #109 [ ] #110
PQs: [ ] x5 | HWs: [ ] x5 | Time: ___ mins

## Day 28 - Buffer and Catch-Up
- [ ] Re-watch weak videos
- [ ] Redo hardest HW from any previous day
- [ ] Write Month 1 concept summary
SQL Mixed: [ ] x2 | Time: ___ mins

## Day 29 - Month 1 Mini Project
- [ ] Reads CSV using Pandas
- [ ] Cleans data (nulls, types, rename)
- [ ] Transforms (filter, group by, aggregate)
- [ ] Writes to new CSV
- [ ] @timer and @retry(3) on each stage
- [ ] Full logging to console and log file
- [ ] Class Pipeline with OOP structure
- [ ] README.md
GitHub Link: ___ | Time: ___ mins

## Day 30 - FINAL TEST DAY
TEST - Questions given on Day 30
Score: ___/12

---

## Month 1 Final Self-Assessment

Topic                            | Rating 1-5 | Need More Work
Lambda Map Filter Reduce         |            |
File IO + Exception Handling     |            |
OOP Classes + Inheritance        |            |
OOP Magic Methods + Encapsulation|            |
Iterators + Generators           |            |
Decorators                       |            |
NumPy + Pandas basics            |            |
Logging                          |            |
Big Data 5 Vs                    |            |
ETL vs ELT DB vs DW vs Lake      |            |
Hadoop Ecosystem                 |            |
HDFS Architecture + Read Write   |            |
NameNode HA                      |            |
MapReduce End to End             |            |
YARN Components + Job Flow       |            |
Linux + HDFS Commands            |            |
SQL SELECT WHERE GROUP BY        |            |
SQL JOINs                        |            |
SQL Window Functions + CTEs      |            |

Ready for Month 2 when:
- [ ] Day 30 score 7 out of 10 or above
- [ ] SQL done on all SQL days
- [ ] Mini project pushed with README
- [ ] All 110 videos checked
- [ ] No topic rated below 3

---

Send completed notebook each day. Claude reviews, scores, sends next notebook and updated checklist.
Tests on Day 10, 20, 30. No skipping.
5 days done. Keep the consistency going.
"""

