# Month 1 — Big Data Engineering Daily Checklist

# Version: Final | Course-Aligned | All 85 videos #26-#110 covered

Goal: Complete Python + Big Data Fundamentals + Hadoop + HDFS + MapReduce + YARN
Daily Time: 2-3 hours | Tests: Day 10, Day 20, Day 30

-----

# What Changed From Original Plan and Why

|Day   |Original                       |Updated                                 |Reason                                                   |
|------|-------------------------------|----------------------------------------|---------------------------------------------------------|
|Day 7 |Iterators + Generators + Review|+ Comprehensions theory                 |Critical gap — not in course videos but in every codebase|
|Day 8 |Decorators + NumPy             |Decorators only (#45)                   |21 min video + closures + factories needs a full day     |
|Day 9 |Pandas Part 1                  |NumPy only (#46)                        |NumPy is the engine under Pandas — needs standalone day  |
|Day 10|Test                           |Test + #47 as preview                   |Same                                                     |
|Day 11|Pandas Part 1                  |Pandas both (#47 + #48)                 |Both videos are connected — do together                  |
|Day 12|Pandas Part 2                  |Data Source + SQLite (#49 + #50)        |These were missing entirely from original                |
|Day 13|Big Data Intro                 |Logging complete (#51-#54)              |3 logging videos need their own day                      |
|Day 14|On-Prem + DB/DW                |Big Data Intro + 5Vs (#57-#62)          |Starts Big Data theory cleanly                           |
|Day 15|Hadoop Ecosystem               |DB/DW/Lake + ETL/ELT + DE Role (#63-#65)|Completes theory before Hadoop                           |
|Day 21|Linux only                     |Cluster explore + Linux 1 (#87-#89)     |#90 Linux 2 moved to Day 22 — Day 21 was 116 mins        |
|Day 22|MapReduce intro                |Linux 2 + HDFS CLI + MR intro (#90-#93) |Balanced load after Day 21 fix                           |
|Day 23|MR Practicals                  |MR Concepts + Practicals (#94-#98)      |More MR context before hands-on                          |

Three course videos that were missing entirely: #49 Data Source Reading, #50 Python With SQLite, #54 Python Outro

-----

# Month Overview

Week 1 (Days 1-7)   | Python OOP complete + Iterators + Generators + Comprehensions theory
| SQL: Days 2, 3
Week 2 (Days 8-14)  | Decorators + NumPy + Pandas + SQLite + Logging | Big Data Intro
| SQL: Day 12
Week 3 (Days 15-21) | Big Data Theory complete | Hadoop + HDFS full
| SQL: Days 15, 17, 19
Week 4 (Days 22-30) | HDFS CLI + MapReduce + YARN | Mini Project
| SQL: Days 22, 24, 26, 28

-----

# SQL Schedule

Day 2  [DONE] SELECT, WHERE, ORDER BY, LIMIT
Day 3  [DONE] GROUP BY, HAVING, aggregate functions
Day 12        JOINs — INNER, LEFT, RIGHT
Day 15        Subqueries
Day 17        CASE WHEN + NULL handling
Day 19        Window functions — ROW_NUMBER, RANK, LAG, LEAD
Day 22        CTEs (WITH clause)
Day 24        String + Date functions
Day 26        Indexes + Query optimization
Day 28        Full SQL revision (mixed)

-----

# WEEK 1

-----

## Day 1 — DONE

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
- Lambda: lambda args: expression. Only ONE expression allowed, no statements, no loops
- Use def when: multiple lines, loops, try/except, docstring needed
- Use lambda when: short one-liner passed directly to map(), sorted(), filter()
- map(func, iterable) applies to every element and returns a lazy map object
- Always wrap in list(): list(map(lambda x: x**2, [1,2,3]))
- map() with two lists: list(map(lambda x,y: x+y, a, b)) zips and applies together
- sorted(lst, key=lambda x: x[-1]) sorts by last character of each string
- Default argument: lambda x, y=10: x+y uses 10 if second arg not passed
- pipeline() bug fix: use data = func(data) not data = func(original) inside loop
- Multiple return values return a tuple. Unpack: a, b = func(x)
- A function that only prints returns None. Chaining None into next function breaks everything

-----

## Day 2 — DONE

Theme: Filter + Modules + Standard Library | Score: 37/60 | Time: 40 mins

Videos:

- [x] #29 Python Filter Function (9min)
- [x] #30 Import Modules And Packages (17min)
- [x] #31 Standard Library Overview (18min)

PQs:

- [x] PQ1 [5/5] filter() returns filter object, wrapped in list() correctly
- [x] PQ2 [3/5] correct concept, missed when to prefer each
- [x] PQ3 [4/5] works. Pro tip: filter(None, lst) removes ALL falsy values in one shot
- [x] PQ4 [5/5] correct definitions and examples
- [ ] PQ5 [0/5] not answered. os.path.join() is cross-platform safe — string concat breaks on Windows

HWs:

- [x] HW1 [3/5] function correct, tested 1 lambda instead of 3
- [x] HW2 [5/5] perfect one-liner
- [ ] HW3 [0/5] skipped — collections.Counter and defaultdict
- [x] HW4 [5/5] perfect datetime
- [ ] HW5 [0/5] skipped (Hadoop not learned yet — valid)

SQL:

- [x] SQL1 [2/5] missing department filter, salary typo 6000 instead of 60000
- [x] SQL2 [5/5] excellent — used lower() for case-insensitive match

### Day 2 Revision Notes

- filter(func, iterable) keeps elements where func returns True. Returns lazy filter object
- filter(None, lst) removes all falsy values: 0, empty string, None, False, empty list
- import math loads full library, use as math.sqrt(). Use when you need many functions
- from math import sqrt imports only that one function. Use when you need just one
- random.choice(lst) picks one random element
- random.shuffle(lst) shuffles IN PLACE and returns None — not a new list
- random.randint(a, b) returns random integer inclusive of both ends
- os.path.join() works on all OS. String concat “/” breaks on Windows
- Counter(lst) counts frequency of each element automatically
- defaultdict(list) auto-creates empty list for new keys — never KeyError
- One-liner: list(map(lambda x: x**2, filter(lambda x: x%2==0, lst)))
- SQL WHERE filters rows before grouping. HAVING filters groups after grouping
- Always read every condition in a SQL question before writing the first line

-----

## Day 3 — PARTIAL (had fever)

Theme: File Operations + File Paths + Exception Handling | Score: 23/60 | Time: 90 mins
Note: Video #34 not watched — exception handling carried to Day 4

Videos:

- [x] #32 File Operation In Python (17min)
- [x] #33 Working With File Paths (9min)
- [ ] #34 Exception Handling In Python (25min) — carried to Day 4

PQs:

- [x] PQ1 [5/5] proved all 4 file modes with working code
- [x] PQ2 [2/5] basic idea correct, missed file handle leak danger
- [x] PQ3 [2/5] created Path object, missed .stem and .parent
- [ ] PQ4 [0/5] pending
- [ ] PQ5 [0/5] pending

HWs:

- [x] HW1 [4/5] correct — tip: use enumerate() not manual counter
- [ ] HW2-HW5 pending

SQL:

- [x] SQL1 [5/5] GROUP BY + HAVING perfect
- [x] SQL2 [5/5] AVG + COUNT + HAVING perfect — perfect SQL day

### Day 3 Revision Notes

- open(file, ‘r’) read only. ‘w’ write and overwrite. ‘a’ append. ‘rb’ binary read
- Always use with open() as f — auto-closes even when error crashes the program
- Without with open: error before f.close() means file handle stays open in memory forever
- A pipeline reading 10000 files with leaked handles fills OS limit and crashes everything
- f.read() loads entire file as one string — bad for large files
- f.readlines() loads ALL lines into a list in memory at once — also bad for large files
- for line in f reads ONE line at a time — good for large files, use this for 10GB logs
- pathlib.Path(“data/sales.csv”).stem gives “sales” — filename without extension
- pathlib.Path(“data/sales.csv”).parent gives “data” — parent folder
- Path(“folder”).exists() returns True or False
- Path(“folder”).glob(”*.csv”) finds all csv in that folder
- Path(“folder”).rglob(”*.csv”) finds all csv recursively in all subfolders
- try runs code that might fail. except catches specific error. else runs only if NO error. finally ALWAYS runs
- Always catch specific: FileNotFoundError, ValueError — never bare except Exception
- Catching Exception hides real bugs — it catches things you never expected
- SQL GROUP BY groups rows. Aggregate functions work on those groups. HAVING filters groups

-----

## Day 4 — DONE

Theme: Exception Handling (finish Day 3) + OOP + Inheritance | Score: 28/55 | Time: 150 mins

Videos:

- [x] #34 Exception Handling In Python (25min)
- [x] #35 OOPS In Python (23min)
- [x] #36 Inheritance In Python (19min)

PQs: [x] PQ4 [4/5] [x] PQ5 [3/5] — OOP PQs not attempted
HWs: [x] HW1 [3/5] [x] HW2 [5/5] [x] HW3 [4/5] [ ] HW4 [0/5] [ ] HW5 [0/5]

### Day 4 Revision Notes

- try/except/else/finally: try runs first, except catches specific errors, else runs if NO error, finally ALWAYS runs
- Catch specific before general: ValueError before Exception — reverse order means specific never runs
- Custom exception: class MyError(Exception): pass — then raise MyError(“message”)
- raise stops the program and throws the error. print just shows text and continues
- BankAccount bug: condition was amount < self.balance, should be amount > self.balance
- Class is a blueprint. Object is the actual thing created from that blueprint
- self means: the specific object that called this method right now
- **init** runs automatically the moment you create an object — sets it up
- Class attribute shared by ALL objects. Instance attribute belongs to ONE specific object
- Inheritance: child class gets all parent methods and attributes automatically
- super().**init**() calls parent setup before adding child’s own attributes
- MRO = Method Resolution Order. D(B, C): Python checks D, then B, then C, then A
- Print D.**mro** to see the exact order Python will use
- In Data Engineering: every pipeline, connector, and config object is a class

-----

## Day 5 — CURRENT

Theme: Polymorphism + Encapsulation + Abstraction

Videos:

- [x] #37 Polymorphism In Python (19min)
- [x] #38 Encapsulation In Python (22min)
- [x] #39 Abstraction In Python (9min)

Corrections from previous submission:

- [ ] Fix 1: Q1 function call without unpacking, remove print(z)
- [ ] Fix 2: Q11 explain file handle leak — OS resource limit, not just bad practice
- [ ] Fix 3: Q12 readlines vs loop — loop is memory safe, readlines loads all into RAM
- [ ] Fix 4: Q13 enumerate in correct order, no reversed()
- [ ] Fix 5: Q14 pathlib only, no os.path mixing

Practice Questions (5):

- [ ] PQ1: Polymorphism in one sentence with real life example. Three classes Dog Cat Cow with sound(). Loop and call without if/elif.
- [ ] PQ2: Difference between _x and __x. Write class with both. Show accessing from outside — one works, one raises AttributeError.
- [ ] PQ3: Temperature class. Celsius stored privately. @property fahrenheit converts F = C x 1.8 + 32. Call obj.fahrenheit without parentheses.
- [ ] PQ4: Abstract class Shape with area(). Circle and Rectangle implement it. Show TypeError when creating Shape() directly.
- [ ] PQ5: Encapsulation vs Abstraction as comments. Real Data Engineering example for each.

Homework (5):

- [ ] HW1: Payment polymorphism. UPI, CreditCard, Cash each has process(amount). checkout(payment, amount) works with all without isinstance checks.
- [ ] HW2: Employee encapsulation. Private salary. give_raise(percent) validates: positive AND under 50. Raise ValueError with clear message for each.
- [ ] HW3: Abstract DataConnector. MySQL and HDFS implement connect() and read(query). run_pipeline(connector) works with both. Show TypeError on abstract directly.
- [ ] HW4: Rectangle. Private width and height. Setters validate > 0. area and perimeter as @property with no parentheses.
- [ ] HW5: Mini pipeline using all four pillars. Abstract Pipeline. SalesPipeline and LogPipeline. run() prints timestamps. execute(pipeline) function works with both.

Notebook: notebooks/day_5/day_5.ipynb
Time Spent: ___ mins

-----

## Day 6

Theme: Magic Methods + Custom Exception Hierarchy + Operator Overloading

Theory to know before videos:

- Dunder methods are Python’s hooks into built-in operations. You never call **str**() directly — Python calls it when you do print(obj)
- **repr** rule: if only one is defined, define **repr** — Python falls back to it for both str() and REPL display
- If you define **eq**, Python sets **hash** to None — object becomes unhashable. Define **hash** explicitly if you need sets or dict keys
- Custom exception hierarchy: PipelineError base, then ExtractionError, TransformationError, LoadError as children

Key dunder methods:

- **str** — triggered by print(obj) and str(obj). Human readable.
- **repr** — triggered by REPL and repr(obj). Precise, for developers.
- **len** — triggered by len(obj)
- **eq** — triggered by obj1 == obj2
- **add** — triggered by obj1 + obj2
- **contains** — triggered by x in obj
- **getitem** — triggered by obj[key]

Videos:

- [ ] #40 Magic Methods In Python (8min)
- [ ] #41 Custom Exception In Python (7min)
- [ ] #42 Operator Overloading In Python (9min)

Practice Questions (5):

- [ ] PQ1: DataRecord class wrapping a dict. **str** readable, **repr** precise with all fields, **len** = number of fields. Print vs REPL — show the difference.
- [ ] PQ2: Vector class. **add** component-wise, **mul** scalar, **eq** component equality. Prove v1+v2, v1*3, v1==v2 all work naturally.
- [ ] PQ3: Pipeline exception hierarchy: PipelineError base, then ExtractionError, TransformError, LoadError. Raise TransformError. Catch and print stage + message.
- [ ] PQ4: SchemaValidator. **len** = column count. **contains** = ‘column’ in validator. **eq** = compare two schemas. Use: if ‘id’ not in schema: raise SchemaMismatchError.
- [ ] PQ5: Define **eq** on LogEntry. Add two LogEntry objects to a set — show what breaks. Fix with **hash**.

Homework (5):

- [ ] HW1: DataPipeline. **str** lists stage names. **len** = stage count. **repr** = full config. **add** merges two pipelines.
- [ ] HW2: Matrix. **add** element-wise, **mul** scalar, **eq** compares, **repr** shows grid. Raise ValueError for shape mismatch.
- [ ] HW3: Full pipeline exception hierarchy. Raise CorruptFileError chained from ValueError. Show both in traceback.
- [ ] HW4: LogEntry with **str**, **repr**, **lt** (sort by timestamp), **eq** + **hash**. Prove sorted() and set() both work.
- [ ] HW5: Dataset class wrapping list of dicts. **len**, **getitem**, **contains**, **iter**. Use all four in a processing loop.

Time Spent: ___ mins

-----

## Day 7

Theme: Iterators + Generators + Theory Supplement: Comprehensions + functools.reduce

Theory to know before videos:

- An iterable has **iter**(). An iterator has **next**(). Every for loop calls these internally.
- Lists are iterables but NOT iterators. iter([1,2,3]) creates an iterator from a list.
- An iterator is one-directional and single-use — you cannot rewind it.
- A function with yield returns a generator object, which is an iterator.
- yield suspends execution, saves all local state, returns a value. Next call to next() resumes from that exact line.

Why generators matter for Big Data (read this carefully):

- A list comprehension for 10GB of data crashes — loads everything into RAM
- A generator reads one record at a time, processes it, discards it
- Spark’s lazy evaluation is the same principle at cluster scale
- .filter() and .map() in Spark build a plan and only execute when .collect() is called
- Understanding Python generators = understanding why Spark is designed the way it is

Comprehensions (not in course videos — essential):

- [x for x in lst if condition] — list comprehension, full list in memory
- {k: v for k, v in items} — dict comprehension
- {x for x in lst} — set comprehension, automatic deduplication
- (x for x in lst) — generator expression, lazy, O(1) memory, use with sum() max() any()

functools.reduce (not in course Python section — essential for MapReduce):

- reduce(func, iterable) collapses a sequence into one value
- reduce(lambda acc, x: acc + x, [1,2,3,4]) = ((1+2)+3)+4 = 10
- This IS the Reduce step in MapReduce. Every reducer is doing reduce(agg_func, all_values_for_key)
- Knowing this now makes MapReduce click immediately when you reach it in Week 4

Videos:

- [ ] #43 Iterators In Python (6min)
- [ ] #44 Generators In Python (11min)
- [ ] No video for comprehensions or functools — theory above covers it

Practice Questions (5):

- [ ] PQ1: CountRange(start, end, step) class with **iter** and **next**. for x in CountRange(0, 50, 5) works. Show StopIteration manually.
- [ ] PQ2: read_large_file(filename) generator yields one line at a time. Process 10000 lines. Print total lines and max line length — never load all into a list.
- [ ] PQ3: Generator pipeline: generate_numbers(n) -> square(nums) -> filter_above(nums, threshold). Chain all three. Explain memory advantage in a comment.
- [ ] PQ4: functools.reduce only (no sum, max, join): product of list, maximum of list, string concatenation. Three separate calls.
- [ ] PQ5: Comprehension ETL on transaction dicts. List comp for amount > 1000. Dict comp for {id: amount}. Set comp for unique merchants. Generator expression for total revenue.

Homework (5):

- [ ] HW1: Infinite fibonacci() generator. Use itertools.islice(fibonacci(), 20) for first 20. Explain in comment why list is worse as N grows.
- [ ] HW2: Full log pipeline. read_lines -> parse_log -> filter_by_level -> format_report. Each is a generator. Chain and process 50000 lines.
- [ ] HW3: functools.reduce pipeline. List of transformation functions. Use reduce(lambda data, fn: fn(data), functions, initial_data) to apply in sequence.
- [ ] HW4: List comp vs generator expression benchmark on 1M numbers. Compare memory with tracemalloc, time with perf_counter. Print results.
- [ ] HW5: Sales data comprehensions. Dict comp: {product: total_sales}. Set comp: unique_regions. Nested list comp: top 3 products per region.

Week 1 Self-Check:

- [ ] Can I write a class with all four OOP pillars without notes?
- [ ] Can I use map, filter, lambda, and comprehensions interchangeably?
- [ ] Can I write a generator and explain what yield does to the call stack?
- [ ] Can I explain why generators are critical for large file processing?
- [ ] Can I use functools.reduce to aggregate a sequence?
- [ ] Can I write SQL SELECT, WHERE, GROUP BY, HAVING?

Time Spent: ___ mins

-----

# WEEK 2

-----

## Day 8

Theme: Decorators — Full Day

Theory to know before video:

- A closure is a function that remembers variables from its enclosing scope even after the outer function returns
- Every decorator IS a closure. Understanding closures = understanding where decorator memory lives
- @timer is exactly func = timer(func) — just cleaner syntax
- ALWAYS use @functools.wraps(func) on the wrapper. Without it every function name becomes “wrapper” in logs
- Decorator factory: @retry(3) needs three levels — factory takes arg, decorator takes func, wrapper calls func

Why decorators matter in Data Engineering:

- @timer — identify pipeline bottlenecks
- @retry(3) — handle network and database flakiness
- @log_call — full audit trail for compliance
- @validate_schema — catch schema drift before it corrupts data

Videos:

- [ ] #45 Decorators In Python (21min)

Practice Questions (5):

- [ ] PQ1: @timer with perf_counter(). Must include function name. Use @functools.wraps. Prove func.**name** is correct.
- [ ] PQ2: @retry(n) factory. Prints attempt X of N on each retry. Re-raises after N failures. Test with function that fails first 2 attempts.
- [ ] PQ3: @log_call using logging module (not print). Logs name, args, kwargs, return value, timestamp. Apply to a data processing function.
- [ ] PQ4: Stack @timer and @retry(3) on same function. Draw the wrapping stack in a comment showing what calls what.
- [ ] PQ5: @validate_positive. All positional args must be positive. Raises ValueError with position and value of invalid argument.

Homework (5):

- [ ] HW1: @stage(name) factory. Logs starting on entry and completed + time + records on exit. Function must return a list.
- [ ] HW2: @cache_result. Stores return in dict keyed by args tuple. Logs cache HIT or MISS each call.
- [ ] HW3: @retry(attempts, delay, exceptions) factory. Retries only on specified exception types. Waits delay seconds between retries.
- [ ] HW4: Full pipeline with extract, transform, load each getting @timer, @retry(3), @stage. Show complete execution log.
- [ ] HW5: Explain stacking order in comment. When @A then @B then def f(), which runs first when f() is called? Write a proof.

Time Spent: ___ mins

-----

## Day 9

Theme: NumPy — Full Day

Theory to know before video:

- Python list element = ~56 bytes (Python object overhead). NumPy int64 element = exactly 8 bytes.
- NumPy operations run in compiled C — vectorised. 1M floats: NumPy ~100x faster than Python loop
- Broadcasting: operations on arrays of different compatible shapes. Dimensions compatible if equal OR one is 1
- axis=0 collapses along rows (result has one value per column). axis=1 collapses along columns.
- Parquet and ORC (HDFS file formats in Spark) use same principle: contiguous data per column = fast scans
- Understanding NumPy memory layout = understanding why columnar formats are fast

Videos:

- [ ] #46 Working With NumPy In Python (28min)

Practice Questions (5):

- [ ] PQ1: Create arrays three ways: np.array(), np.zeros((3,4)), np.arange(0,50,5). Slice: first row, last column, every other row, 2x2 sub-matrix from centre.
- [ ] PQ2: Broadcasting. Predict output shape of (4,1) + (1,3) on paper first. Then code and confirm with .shape.
- [ ] PQ3: Boolean indexing. 20 random integers 0-100. Select all above mean. Replace below 10 with 0. Count those in range 40-60.
- [ ] PQ4: Vectorised vs loop. Square root of 1M elements. Time both. Print: “NumPy: Xs | Loop: Ys | Speedup: Zx”.
- [ ] PQ5: Axis operations. Shape (5,4) array. Predict output shape for sum(axis=0) and sum(axis=1) BEFORE running. Verify. Column means, row max, overall min.

Homework (5):

- [ ] HW1: Sales simulation. (1000,5) array. Total per product, total per day, top 3 products, normalise to 0-1. No loops.
- [ ] HW2: Statistics engine. (100,5) exam scores. Per student: mean, highest, passed (>=40 all five). Per exam: mean, std, pass rate.
- [ ] HW3: Boolean masking. Below 0 = invalid. Above 1000 = outlier. Count each. Replace invalids with np.nan, outliers with column median.
- [ ] HW4: Broadcasting revenue matrix. Price array (m,1) x quantity array (1,n) = (m,n) result. No loops. Verify shape.
- [ ] HW5: Matrix operations. Dot product (explain (m,n)@(n,p)=(m,p) in comment). Transpose. Reshape. Meaningful example for each.

Time Spent: ___ mins

-----

## Day 10 — TEST DAY

Scope: Python Days 1-9 — all Python topics

Covers: map/filter/lambda/reduce/comprehensions, modules/stdlib, file IO, exception handling, OOP all four pillars, magic methods, iterators/generators, decorators, NumPy

Before test: Watch #47 Pandas DataFrame as preview — not tested, just orientation
Videos: [ ] #47 (preview only)
TEST — questions given on Day 10
Score: ___/10 | Time: ___ mins

-----

## Day 11

Theme: Pandas — DataFrame + Series + Data Manipulation

Theory to know before videos:

- DataFrame = 2D labelled structure. Each column = a Series = 1D array built on NumPy
- DataFrame is a dict of Series all sharing the same index
- .loc[label] = label-based indexing. .iloc[position] = position-based (always 0,1,2…)
- After filtering, always call .copy() before modifying — filtering returns a view not a copy
- groupby follows split-apply-combine. This IS MapReduce at small scale
- apply() is a Python loop under the hood. Always try vectorised operations first

Videos:

- [ ] #47 Pandas DataFrame And Series (29min)
- [ ] #48 Data Manipulation And Analysis (24min)

Practice Questions (5):

- [ ] PQ1: Read CSV. Check shape, dtypes, null count per column. Show first 5 and last 3 rows. Select only numeric columns.
- [ ] PQ2: .loc vs .iloc on non-default index. Select same row using both. Show difference. Explain when each breaks.
- [ ] PQ3: groupby with multi-agg. Sales data product + region + amount. Mean and sum per product. Filter groups where sum > 5000.
- [ ] PQ4: Copy vs view. Trigger SettingWithCopyWarning on purpose. Fix with .copy(). Confirm original unchanged.
- [ ] PQ5: Boolean indexing + string ops. Filter rows where name contains “Ltd” (case-insensitive). Add column categorising amount as High/Mid/Low.

Homework (5):

- [ ] HW1: Load real CSV. Clean: drop fully null rows, fill numeric nulls with column median, rename to snake_case.
- [ ] HW2: groupby multi-agg. Total revenue per region, average order value per product per region, top 5 products by revenue.
- [ ] HW3: pd.merge INNER LEFT RIGHT. Employees + departments. Find employees with no department using LEFT JOIN + isnull().
- [ ] HW4: Vectorised vs apply benchmark. Time both. Show speedup.
- [ ] HW5: pivot_table. Rows = product, columns = month, values = sum(amount). Comment: how this connects to groupby.

Time Spent: ___ mins

-----

## Day 12

Theme: Data Source Reading + Python With SQLite | SQL: JOINs

Theory to know before videos:

- pd.read_csv(file, chunksize=10000) returns a chunk iterator — reads 10000 rows at a time, never loads full file
- Parquet = columnar binary format. Same memory layout as NumPy. Native format for Spark and HDFS in production
- SQLite = file-based database, no server needed, entire DB is one .db file
- pd.read_sql(“SELECT …”, conn) runs SQL and returns a DataFrame directly
- This same pattern works for MySQL and PostgreSQL — just swap the connection library

Videos:

- [ ] #49 Data Source Reading (15min)
- [ ] #50 Python With SQLite (16min)

Practice Questions (5):

- [ ] PQ1: Read CSV with chunksize=1000. Process each chunk: filter above threshold, sum column. Print running total — never load full file.
- [ ] PQ2: Read JSON into Pandas. Handle nested JSON with pd.json_normalize(). Show before and after.
- [ ] PQ3: SQLite. Create table, insert 10 rows, query with WHERE, update one, delete one. Read full table into DataFrame.
- [ ] PQ4: pd.read_sql. Run GROUP BY directly via SQLite connection. Get result as DataFrame.
- [ ] PQ5: Chunked pipeline. Read large CSV in chunks. Filter, transform, write each chunk to new CSV. Never hold more than one chunk.

Homework (5):

- [ ] HW1: Read 3 different formats (CSV, JSON, one more). Clean each. Write all to Parquet. Reload and verify.
- [ ] HW2: SQLite pipeline. Create sales table. Insert 100 rows with df.to_sql(). Query with JOINs across two tables.
- [ ] HW3: Chunked aggregation. Sum and count per category across all chunks using running dict. No full load.
- [ ] HW4: Parameterised SQL function query_sales(conn, min_amount, region). Use ? placeholders, never string formatting.
- [ ] HW5: Data source comparison. Same dataset from CSV, JSON, SQLite, Parquet. Compare file size, read time, memory.

SQL Day — JOINs:

- [ ] SQL1: INNER JOIN employees with departments. Show name, salary, department name. Filter: Engineering or Data only.
- [ ] SQL2: LEFT JOIN employees to projects. Find employees with NO project (IS NULL after join). Show count per department.

Time Spent: ___ mins

-----

## Day 13

Theme: Logging — Complete (all 4 videos)

Theory to know before videos:

- print() = stdout only, no levels, no timestamps, cannot be turned off
- logging = console AND file simultaneously, 5 levels (DEBUG/INFO/WARNING/ERROR/CRITICAL), timestamps, module name, fully configurable
- In a Hadoop/Spark cluster on 200 machines you cannot print() your way to debugging
- Every production pipeline uses structured logging. The Day 29 mini project requires it.
- logger.error(“msg”, exc_info=True) appends the full traceback automatically

Videos:

- [ ] #51 Logging In Python (14min)
- [ ] #52 Logging With Multiple Loggers (4min)
- [ ] #53 Logging In Real World Examples (7min)
- [ ] #54 Python Outro (1min)

Practice Questions (5):

- [ ] PQ1: Logger with two handlers (console: INFO+, file: DEBUG+). Custom format with timestamp + module + level + message. One message at each of the 5 levels. Check what appears where.
- [ ] PQ2: Module-level logger using logging.getLogger(**name**) in three files. Import all in main script. Each log line shows its source module.
- [ ] PQ3: Retrofit Day 8 @log_call to use logging.debug and logging.info instead of print. Show output difference.
- [ ] PQ4: Logging in exception handling. logger.error(“msg”, exc_info=True) — show full traceback automatically appended.
- [ ] PQ5: Log rotation with RotatingFileHandler(maxBytes=1MB, backupCount=5). Explain why this matters in a daily pipeline running for a year.

Homework (5):

- [ ] HW1: PipelineLogger class. start_stage/end_stage/log_warning/log_error methods. Uses logging internally. Apply to Day 8 pipeline.
- [ ] HW2: extractor.py, transformer.py, loader.py each with **name** logger. Main imports all three. Correct source on every line.
- [ ] HW3: Process 1000 records. Log: start, every 100 records, any warning (null), any error (parse fail), final summary.
- [ ] HW4: Modify @stage(name) from Day 8 HW1 to use logging.getLogger instead of print.
- [ ] HW5: Generate 500 log lines (mix INFO/WARNING/ERROR). Write to file. Read with Pandas. Count per level. Print summary table.

Time Spent: ___ mins

-----

## Day 14

Theme: Big Data Intro + 5 Vs + Distributed Systems + On-Prem vs Cloud + Designing Big Data Systems

Theory foundation (pure theory day — no coding):

Why single machines fail:

- Fixed CPU, fixed RAM, fixed disk. Vertical scaling (bigger machine) is expensive and has a physical limit
- Horizontal scaling (more machines) = how the internet is built = how every Big Data tool works
- Distributed computing: split data, process parts in parallel, combine results

The 5 Vs:

- Volume: petabytes of data. Tool: HDFS, S3
- Velocity: millions of events per second. Tool: Kafka, Spark Streaming
- Variety: CSV + JSON + images + logs. Tool: Data Lake
- Veracity: noisy, inaccurate data. Tool: cleaning pipelines
- Value: actionable insights. Tool: analytics layer

Distributed fundamentals:

- Cluster: group of machines appearing as one system
- Master/Worker: one node coordinates, others execute
- Data Locality: move computation to data, not data to computation. This is the core Hadoop principle.
- Fault Tolerance: assume machines WILL fail. Design for it. Replicate. Retry automatically.

On-Prem vs Cloud:

- On-Prem: your hardware, full control, high upfront cost, fixed capacity
- Cloud: rented hardware, pay per use, instant scale — GCP Dataproc, AWS EMR, Azure HDInsight
- Hadoop era = ETL on-prem. Cloud era = ELT on cloud. You will work with both.

Videos:

- [ ] #57 Section Intro (1min)
- [ ] #58 What is Big Data — A Practical Example (18min)
- [ ] #59 5 Vs of Big Data (22min)
- [ ] #60 Big Data and Distributed Systems (17min)
- [ ] #61 Designing a Good Big Data System (11min)
- [ ] #62 On-Premise Infra vs Cloud Solutions (20min)

Practice Questions (5): [ ] PQ1 [ ] PQ2 [ ] PQ3 [ ] PQ4 [ ] PQ5
Homework (5): [ ] HW1 [ ] HW2 [ ] HW3 [ ] HW4 [ ] HW5
Time Spent: ___ mins

-----

# WEEK 3

-----

## Day 15

Theme: DB vs DW vs Data Lake + ETL vs ELT + What Does a Data Engineer Do | SQL: Subqueries

Theory foundation:

Storage layer architecture:

- Database (OLTP): transactions, schema on write, current structured data. Example: MySQL, PostgreSQL
- Data Warehouse (OLAP): analytics, schema on write, historical structured data. Example: BigQuery, Redshift
- Data Lake: raw storage, schema on read, any format. Example: HDFS, S3
- Lakehouse: combines both. Delta Lake, Apache Iceberg. Where the industry is moving now.

ETL vs ELT:

- ETL = Extract, Transform, Load. Transform first, load clean data. Hadoop era. Good when destination is expensive.
- ELT = Extract, Load, Transform. Load raw, transform inside the lake. Cloud era. Good when storage is cheap.
- Hadoop = ETL. Cloud = ELT. You will work with both.

Videos:

- [ ] #63 Database vs Data Warehouse vs Data Lake (29min)
- [ ] #64 ETL vs ELT (21min)
- [ ] #65 What does a Data Engineer do (18min)

SQL Day — Subqueries:

- [ ] SQL1: Subquery in WHERE. Find employees earning more than the average salary of their own department.
- [ ] SQL2: Subquery in FROM. Dept-level stats as inline view. Filter depts where avg salary above company-wide average.

Practice Questions (5): [ ] PQ1 [ ] PQ2 [ ] PQ3 [ ] PQ4 [ ] PQ5
Homework (5): [ ] HW1 [ ] HW2 [ ] HW3 [ ] HW4 [ ] HW5
Time Spent: ___ mins

-----

## Day 16

Theme: Hadoop Intro + Hadoop Ecosystem

Theory foundation:

- Origin: Google published GFS (2003) and MapReduce (2004) papers. Yahoo built open-source versions. Core insight: commodity hardware is cheap, networks are expensive — store data where it is processed.
- Three core layers: HDFS (storage) + MapReduce (processing) + YARN (resource management)
- Everything else — Hive, Pig, HBase, Spark — sits on top of these three
- Properties: distributed, fault-tolerant, scalable, open-source, commodity hardware, write-once read-many
- Ecosystem: Hive (SQL on Hadoop), HBase (NoSQL), Sqoop (DB to HDFS), Flume (log ingestion), Oozie (scheduler), ZooKeeper (coordination). Spark replaces MapReduce as processing engine.

Videos:

- [ ] #66 Section Intro (2min)
- [ ] #67 Introduction To Hadoop (5min)
- [ ] #68 Properties of Hadoop (9min)
- [ ] #69 Hadoop Ecosystem Main Components (9min)
- [ ] #70 Hadoop Ecosystem Components (29min)

Practice Questions (5): [ ] PQ1 [ ] PQ2 [ ] PQ3 [ ] PQ4 [ ] PQ5
Homework (5): [ ] HW1 [ ] HW2 [ ] HW3 [ ] HW4 [ ] HW5
Time Spent: ___ mins

-----

## Day 17

Theme: HDFS Architecture + Blocks + Replication Factor | SQL: CASE WHEN + NULL handling

Theory foundation:

- HDFS = file system for large files on commodity hardware. Optimised for sequential reads, not random access.
- NameNode: master. Stores ALL metadata in RAM: file names, block locations, DataNode assignments. Single point of failure without HA.
- DataNode: workers. Store actual data blocks. Send heartbeats to NameNode every 3 seconds.
- Default block size: 128MB. A 1GB file = 8 blocks. Large size minimises NameNode RAM usage.
- Replication factor 3: each block on 3 different DataNodes. Provides fault tolerance.
- Rack-aware placement: first replica local, second on different rack, third on same rack as second. Balances durability and network cost.

Videos:

- [ ] #71 Intro to HDFS and Common Terminology (22min)
- [ ] #72 Why HDFS (4min)
- [ ] #73 HDFS Architecture (15min)
- [ ] #74 Blocks In HDFS (12min)
- [ ] #75 Replication Factor in HDFS (9min)

SQL Day — CASE WHEN + NULL handling:

- [ ] SQL1: CASE WHEN salary bands: <30k = Junior, 30k-60k = Mid, >60k = Senior. Count per band.
- [ ] SQL2: COALESCE(column, 0) for nullables. IS NULL and IS NOT NULL in WHERE. NULLIF(a,b) to avoid divide-by-zero.

Practice Questions (5): [ ] PQ1 [ ] PQ2 [ ] PQ3 [ ] PQ4 [ ] PQ5
Homework (5): [ ] HW1 [ ] HW2 [ ] HW3 [ ] HW4 [ ] HW5
Time Spent: ___ mins

-----

## Day 18

Theme: Rack Awareness + Node Failure (temporary + permanent) + GCP Account Setup

Theory foundation:

- Rack awareness: replicas across racks means full rack power failure cannot lose a block
- Temporary DataNode failure: stops heartbeats. After 10 min NameNode marks dead. Under-replicated blocks auto re-replicated. Self-healing.
- Permanent DataNode failure: decommission node. All its blocks re-replicated elsewhere. Admin runs hdfs dfsadmin -decommission.
- GCP: Create your account during #78 if not done. Needed for Day 21 cluster practicals.

Videos:

- [ ] #76 Rack Awareness in HDFS (7min)
- [ ] #77 Node Failure (0min — section title)
- [ ] #78 Create GCP Account (24min) — create account during this video
- [ ] #79 Data Node Failure Temporary (11min)
- [ ] #80 Data Node Failure Permanent (14min)

Practice Questions (5): [ ] PQ1 [ ] PQ2 [ ] PQ3 [ ] PQ4 [ ] PQ5
Homework (5): [ ] HW1 [ ] HW2 [ ] HW3 [ ] HW4 [ ] HW5
Time Spent: ___ mins

-----

## Day 19

Theme: NameNode HA Architecture + HDFS Read/Write Flow | SQL: Window Functions

Theory foundation:

- Secondary NameNode (misleading name): NOT a standby. Periodically merges EditLog with FsImage. Does NOT take over if NameNode dies.
- Standby NameNode (true HA): hot standby. Uses ZooKeeper for leader election. Uses JournalNodes for shared log. Takes over in seconds.
- Fencing: prevents split-brain. Old Active NameNode is killed before Standby is promoted. Without fencing both could accept writes = data corruption.
- HDFS Write flow: Client asks NameNode for DataNode pipeline. Writes to DN1. DN1 pipelines to DN2. DN2 to DN3. ACKs flow back. NameNode is NOT in the data path.
- HDFS Read flow: Client asks NameNode for block locations. Client reads each block directly from nearest DataNode. NameNode never serves data.
- Data locality in reads: same node > same rack > other rack. Minimises network IO.

Videos:

- [ ] #81 Secondary Name Node (17min)
- [ ] #82 Standby Name Node (10min)
- [ ] #83 Hadoop HA Architecture (20min)
- [ ] #84 Data Write in HDFS (22min)
- [ ] #85 Read Request in HDFS (10min)

SQL Day — Window Functions:

- [ ] SQL1: ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) — rank employees within department.
- [ ] SQL2: LAG(salary, 1) OVER (ORDER BY hire_date) — compare each employee to previous hire. SUM(amount) OVER (PARTITION BY month ORDER BY day) — running total.

Practice Questions (5): [ ] PQ1 [ ] PQ2 [ ] PQ3 [ ] PQ4 [ ] PQ5
Homework (5): [ ] HW1 [ ] HW2 [ ] HW3 [ ] HW4 [ ] HW5
Time Spent: ___ mins

-----

## Day 20 — TEST DAY

Scope: Big Data Theory + Hadoop + HDFS (Days 14-19)

Covers: 5 Vs, DB/DW/Lake, ETL/ELT, Hadoop ecosystem, HDFS architecture, blocks, replication, rack awareness, node failure recovery, Secondary vs Standby NameNode, HA architecture, HDFS read/write flow

Before test: Watch #86 GCP Hadoop Cluster Creation as preview
Videos: [ ] #86 (preview only)
TEST — questions given on Day 20
Score: ___/12 | Time: ___ mins

-----

## Day 21

Theme: Cluster Exploration + GCP Best Practices + Linux Commands 1
Note: Linux Commands 2 (#90) moved to Day 22 — Day 21 was 116 mins without this fix

Theory foundation:

- Linux essentials for Big Data: every Hadoop cluster runs on Linux. You SSH into nodes, navigate HDFS, debug jobs via terminal.
- Key commands: grep, awk, cut, sort, uniq -c, wc -l, head, tail, find, chmod, ps aux, top
- Log parsing in bash: cat app.log | grep “ERROR” | cut -d’|’ -f2 | sort | uniq -c | sort -rn | head -10
  This gives top 10 most frequent error messages with no Python needed.

Videos:

- [ ] #87 Exploring our Hadoop Cluster (24min)
- [ ] #88 GCP Cluster Best Practices (4min)
- [ ] #89 Linux Commands 1 (32min)

Practice Questions (5): [ ] PQ1 [ ] PQ2 [ ] PQ3 [ ] PQ4 [ ] PQ5
Homework (5): [ ] HW1 [ ] HW2 [ ] HW3 [ ] HW4 [ ] HW5
Time Spent: ___ mins

Week 3 Self-Check:

- [ ] Can I explain HDFS architecture end to end without notes?
- [ ] Can I clearly state the difference between Secondary NameNode and Standby NameNode?
- [ ] Can I trace a full HDFS read and write flow step by step including ACKs?
- [ ] Do I understand rack-aware replication placement?
- [ ] Can I write SQL window functions: ROW_NUMBER, RANK, LAG, SUM OVER?
- [ ] Have I set up my GCP account?

-----

# WEEK 4

-----

## Day 22

Theme: Linux Commands 2 + HDFS CLI Commands + MapReduce Intro + Core Concepts | SQL: CTEs

Theory foundation:

HDFS CLI commands:

- hdfs dfs -ls /path — list files
- hdfs dfs -mkdir /path — create directory
- hdfs dfs -put local.csv /hdfs/path — upload from local to HDFS
- hdfs dfs -get /hdfs/path local.csv — download from HDFS to local
- hdfs dfs -cat /hdfs/file — print file contents
- hdfs dfs -rm -r /path — delete recursive
- hdfs fsck /path — check HDFS health, find under-replicated blocks
- hdfs dfsadmin -report — cluster health: capacity, live DataNodes, missing blocks

MapReduce core concept:

- Map phase: each mapper processes one input split (~128MB). Emits (key, value) pairs.
- Shuffle and Sort: framework automatically groups all values with the same key. You write nothing for this.
- Reduce phase: each reducer receives all values for one key. Aggregates and emits output.
- Connection to Day 7: the Reduce phase IS functools.reduce(agg_func, all_values_for_this_key)
- Data locality: mappers run on the nodes where the input data blocks live

Videos:

- [ ] #90 Linux Commands 2 (27min)
- [ ] #91 HDFS Commands (30min)
- [ ] #92 Hadoop Outro (2min)
- [ ] #93 Map Reduce Intro (1min)

SQL Day — CTEs:

- [ ] SQL1: WITH dept_avg AS (…) — join back to employees to find those earning above their department average.
- [ ] SQL2: Chain two CTEs — one to clean data, one to aggregate.

Practice Questions (5): [ ] PQ1 [ ] PQ2 [ ] PQ3 [ ] PQ4 [ ] PQ5
Homework (5): [ ] HW1 [ ] HW2 [ ] HW3 [ ] HW4 [ ] HW5
Time Spent: ___ mins

-----

## Day 23

Theme: MapReduce Concepts + Practicals Part 1 and 2

Theory foundation:

- Word Count = Hello World of MapReduce
  Map: for each word emit (word, 1)
  Shuffle: groups (hadoop,1),(hadoop,1),(hadoop,1) into (hadoop,[1,1,1])
  Reduce: sum the values = (hadoop, 3)
- Follow practicals hands-on on your GCP cluster from Day 21

Videos:

- [ ] #94 Intro to Distributed Processing (11min)
- [ ] #95 Map Reduce Introduction (17min)
- [ ] #96 Map Reduce and Cluster (12min)
- [ ] #97 Map Reduce Practical Part 1 (17min)
- [ ] #98 MR Example Part 2 (22min)

Practice Questions (5): [ ] PQ1 [ ] PQ2 [ ] PQ3 [ ] PQ4 [ ] PQ5
Homework (5): [ ] HW1 [ ] HW2 [ ] HW3 [ ] HW4 [ ] HW5
Time Spent: ___ mins

-----

## Day 24

Theme: MapReduce with 1 Reducer + 2 Reducers | SQL: String + Date Functions

Theory foundation:

- 1 reducer: all keys go to one reducer. Simple but bottleneck for large datasets
- 2 reducers: keys partitioned across two. Default: hash(key) % num_reducers
- Custom partitioner: control which key goes to which reducer

Videos:

- [ ] #99 MR Practical with 1 Reducer (39min)
- [ ] #100 MR with 2 Reducers Practical (29min)

SQL Day — String + Date Functions:

- [ ] SQL1: UPPER, LOWER, CONCAT, SUBSTRING, TRIM, LENGTH, REPLACE. Build formatted name from first + last name.
- [ ] SQL2: NOW(), DATE(), DATEDIFF(), DATE_ADD(), YEAR(), MONTH(). Find employees hired in last 90 days. Calculate tenure in years.

Practice Questions (5): [ ] PQ1 [ ] PQ2 [ ] PQ3 [ ] PQ4 [ ] PQ5
Homework (5): [ ] HW1 [ ] HW2 [ ] HW3 [ ] HW4 [ ] HW5
Time Spent: ___ mins

-----

## Day 25

Theme: Combiner + Zero Reducer + Big Log File + Input Splits

Theory foundation:

- Combiner: mini-reducer on mapper output before sending to network. Reduces shuffle data — often the bottleneck.
- Combiner rule: must be commutative and associative. Sum works. Average does NOT — partial averages cannot be combined.
- Zero Reducer: skip reduce entirely. Output = mapper output. Use for filtering and transforming only.
- Input Split: logical division of input. One mapper per split. Split size usually = block size.

Videos:

- [ ] #101 Combiner in MR (13min)
- [ ] #102 Map Reduce with 0 Reducer (15min)
- [ ] #103 MR on Big Log File (20min)
- [ ] #104 Input Split in MR (7min)
- [ ] #105 Map Reduce Outro (2min)

Practice Questions (5): [ ] PQ1 [ ] PQ2 [ ] PQ3 [ ] PQ4 [ ] PQ5
Homework (5): [ ] HW1 [ ] HW2 [ ] HW3 [ ] HW4 [ ] HW5
Time Spent: ___ mins

-----

## Day 26

Theme: YARN Complete | SQL: Indexes + Query Optimization

Theory foundation:

- Why YARN: Hadoop 1.x JobTracker did both resource management and job tracking = bottleneck and single point of failure. YARN splits these.
- ResourceManager: cluster-level. Manages CPU + memory across ALL applications. One per cluster.
- NodeManager: per-node. Manages containers. Reports to ResourceManager.
- ApplicationMaster: per-application. Negotiates resources with RM. Coordinates containers. Itself runs in a container.
- Container: resource allocation unit (e.g. 4GB RAM + 2 cores). All job work happens in containers.

YARN job flow step by step:

1. Client submits job to ResourceManager
1. RM allocates container for ApplicationMaster
1. AM starts, registers with RM
1. AM requests containers from RM for actual work
1. NodeManagers launch containers as instructed
1. AM monitors containers, requests replacements if any fail
1. Job completes, AM deregisters, containers released

Fault tolerance:

- Container fails: AM requests replacement from RM
- AM fails: RM restarts it from checkpoint
- RM fails: HA RM with ZooKeeper (same pattern as HDFS HA)

Videos:

- [ ] #106 YARN Section Intro (1min)
- [ ] #107 YARN Introduction (5min)
- [ ] #108 Components of YARN (22min)
- [ ] #109 YARN Analogy (5min)
- [ ] #110 YARN Process Step by Step (28min)

SQL Day — Indexes + Query Optimization:

- [ ] SQL1: Create index on high-cardinality column. Show EXPLAIN before and after. Compare ALL (full scan) vs ref (index used).
- [ ] SQL2: Rewrite slow query using: correct JOIN type, WHERE before HAVING, no SELECT *, LIMIT early.

Practice Questions (5): [ ] PQ1 [ ] PQ2 [ ] PQ3 [ ] PQ4 [ ] PQ5
Homework (5): [ ] HW1 [ ] HW2 [ ] HW3 [ ] HW4 [ ] HW5
Time Spent: ___ mins

-----

## Day 27

Theme: Review + Catch-Up

- [ ] Re-watch any video where PQ score was below 3/5
- [ ] Redo hardest HW from any week
- [ ] Write Month 1 concept map connecting all topics
- [ ] Connect the thread: generator lazy evaluation -> Spark lazy evaluation -> YARN container lifecycle
- [ ] Start mini project README

Time Spent: ___ mins

-----

## Day 28

Theme: Buffer + SQL Full Revision

- [ ] Re-watch any Hadoop/HDFS/MR/YARN video that felt unclear
- [ ] Redo any incomplete HW from Week 4
- [ ] Write one-page summary: MapReduce end-to-end + YARN job submission flow

SQL Revision:

- [ ] SQL Mixed 1: One query using JOINs + CTE + Window Function + CASE WHEN together
- [ ] SQL Mixed 2: One query using Subquery + GROUP BY + HAVING + String function together

Time Spent: ___ mins

-----

## Day 29

Theme: Month 1 Mini Project

Requirements:

- [ ] Reads real CSV using Pandas with chunksize
- [ ] Cleans data: drop nulls, fix dtypes, rename to snake_case
- [ ] Transforms: filter, groupby, aggregate, derived column
- [ ] Writes output to CSV and Parquet
- [ ] @timer and @retry(3) on each stage (Day 8)
- [ ] Full logging to console AND log file (Day 13)
- [ ] Generator-based chunked reading (Day 7)
- [ ] Abstract Pipeline base class with concrete SalesPipeline (Days 4-5)
- [ ] README.md: purpose, setup, how to run, sample output

GitHub Link: ___ | Time Spent: ___ mins

-----

## Day 30 — FINAL TEST DAY

Scope: Full Month 1 — Python + Big Data + Hadoop + HDFS + MapReduce + YARN + SQL

TEST — questions given on Day 30
Score: ___/12

-----

# Month 1 Final Self-Assessment

Topic                                        | Rating 1-5 | More Work Needed
Lambda, Map, Filter                          |            |
Comprehensions (list dict set generator)     |            |
functools.reduce                             |            |
File IO + Exception Handling                 |            |
OOP: Classes + Inheritance + MRO             |            |
OOP: Magic Methods + Encapsulation + Abstract|            |
Iterators + Generators + Generator Pipelines |            |
Decorators + Decorator Factories             |            |
NumPy: arrays broadcasting axis vectorize    |            |
Pandas: DataFrame groupby merge chunked read |            |
Data Source Reading + SQLite                 |            |
Logging: setup levels multi-handler          |            |
Big Data 5 Vs + Distributed fundamentals     |            |
ETL vs ELT, DB vs DW vs Data Lake            |            |
Hadoop: origin properties ecosystem          |            |
HDFS: architecture blocks replication        |            |
NameNode HA: Secondary vs Standby            |            |
HDFS Read + Write flow step by step          |            |
MapReduce: Map Shuffle Reduce end to end     |            |
Combiner + Zero Reducer + Input Splits       |            |
YARN: RM + NM + AM + Container               |            |
YARN job submission flow step by step        |            |
Linux + HDFS CLI commands                    |            |
SQL: SELECT WHERE GROUP BY HAVING            |            |
SQL: JOINs                                   |            |
SQL: Subqueries + CASE WHEN + NULL           |            |
SQL: Window Functions                        |            |
SQL: CTEs + String/Date functions            |            |

Ready for Month 2 (Spark) when:

- [ ] Day 30 score 7 out of 10 or above
- [ ] SQL done on all 9 SQL days
- [ ] Mini project pushed to GitHub with README
- [ ] All videos #26 through #110 checked
- [ ] No topic rated below 3
- [ ] Can explain: generator lazy evaluation -> why Spark’s .filter() does not run immediately

-----

Send completed notebook each day. Tests on Day 10, Day 20, Day 30. No skipping.
5 days done. 25 to go.
