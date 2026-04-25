## What Changed, What Stayed, and Why

| Area | Original Plan | v3 Course-Aligned | Reason |
|------|--------------|-------------------|--------|
| Day 7 | Iterators + Generators + Week Review | Iterators + Generators + **Comprehensions theory** | Comprehensions are not in your Python videos — critical gap |
| Day 8 | Decorators + NumPy (crammed) | **Decorators only** (#45) | Decorators alone = 21 min video + closures + factories = 2.5 hrs minimum |
| Day 9 | Pandas Part 1 | **NumPy only** (#46) | NumPy needs standalone day — it's the engine under all of Pandas |
| Day 10 | Test | **Test (Python Days 1–9)** | Same — watch #47 before test as preview |
| Day 11 | Pandas Part 1 | **Pandas Part 1 + Part 2** (#47 + #48) | Both Pandas videos together — they're connected |
| Day 12 | Pandas Part 2 + Logging | **Data Source Reading + SQLite** (#49 + #50) \| SQL JOINs | #49 and #50 were **missing entirely** from original plan |
| Day 13 | Big Data Intro | **Logging complete** (#51 + #52 + #53) | 3 logging videos need their own day — critical for mini project |
| Day 14 | On-Prem + DB/DW + ETL | **Big Data Intro + 5V's + Distributed** (#57–#62) | Properly starts Big Data theory fresh |
| Day 15 | Hadoop Ecosystem | **Big Data Theory completion** (#63–#65) \| SQL Subqueries | Completes the theory block cleanly before Hadoop |
| Days 16–22 | Same topics | **Shifted 2 days** — identical content, correct video numbers | Just pushed to accommodate Python expansion |
| Days 22–26 | MapReduce + YARN | **Identical — correct video numbers added** | Content fully preserved |

**Three course videos added that were missing:** `#49 Data Source Reading`, `#50 Python With SQLite`, `#54 Python Outro`

---

# Month 1 — Big Data Engineering Daily Checklist [v3 — Course-Aligned]

**Goal:** Complete Python (remaining) + Big Data Fundamentals + Hadoop + HDFS + MapReduce + YARN
**Daily Time:** 2–3 hours | **Tests:** Day 10, Day 20, Day 30
**Course:** 302 lectures · 73h 45m

---

## Month Overview

```
Week 1 (Days 1–7)   | Python: OOP complete + Iterators + Generators + Comprehensions theory
                    | SQL: Days 2, 3
Week 2 (Days 8–14)  | Python: Decorators + NumPy + Pandas + SQLite + Logging | Big Data Intro
                    | SQL: Day 12
Week 3 (Days 15–21) | Big Data Theory complete | Hadoop + HDFS full
                    | SQL: Days 15, 17, 19
Week 4 (Days 22–30) | HDFS Commands + MapReduce + YARN | Mini Project
                    | SQL: Days 22, 24, 26, 28
```

---

## SQL Schedule

```
Day 2  ✅ SELECT, WHERE, ORDER BY, LIMIT
Day 3  ✅ GROUP BY, HAVING, aggregate functions
Day 12    JOINs (INNER, LEFT, RIGHT)
Day 15    Subqueries
Day 17    CASE WHEN + NULL handling
Day 19    Window functions (ROW_NUMBER, RANK, LAG, LEAD)
Day 22    CTEs (WITH clause)
Day 24    String + Date functions
Day 26    Indexes + Query optimization
Day 28    SQL full revision (mixed questions)
```

---

## WEEK 1

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
## Day 5 — 🔄 CURRENT
**Theme:** OOP Part 2 — Polymorphism + Encapsulation + Abstraction

### 📚 Theory Foundation *(read before PQs)*

**Polymorphism:**
- Same method name, different behavior per class. Python uses **Duck Typing** — if the object has the method, it works. No type checking needed.
- In Data Engineering: CSV connector, HDFS connector, S3 connector all have `.read()`. Your pipeline calls `.read()` on any of them without caring which one it is.

**Encapsulation:**
- `_x` = single underscore = convention: *"I'd rather you didn't, but I can't stop you"*
- `__x` = double underscore = name mangling: Python renames it to `_ClassName__x` internally. Accessing `obj.__x` from outside raises `AttributeError`.
- `@property` turns a method into an attribute — caller uses `obj.fahrenheit` not `obj.fahrenheit()`. Clean API.
- `@name.setter` validates before setting. Never let invalid data enter your object's state.

**Abstraction:**
- `ABC` + `@abstractmethod` = a **contract**. Subclasses MUST implement the method or `TypeError` is raised at instantiation.
- The abstract class defines WHAT. The subclass defines HOW.
- `TypeError: Can't instantiate abstract class Shape with abstract method area` is not an error — it is working exactly as designed.

**The Pillar Connection:**
```
Abstraction  → defines the contract (WHAT)
Inheritance  → shares code between classes
Polymorphism → same interface, different implementations (HOW)
Encapsulation→ protects internal state
```
These four work together. Every production pipeline component uses all four.

**Videos:**
- [x] `#37` Polymorphism In Python (19 min)
- [x] `#38` Encapsulation In Python (22 min)
- [x] `#39` Abstraction In Python (9 min)

**Corrections from Day 4:**
- [ ] Fix 1: Q1 — function call without unpacking, remove `print(z)`
- [ ] Fix 2: Q11 — explain actual file handle leak danger (OS limit, not just "bad practice")
- [ ] Fix 3: Q12 — `readlines` vs `for` loop — loop is memory-safe, `readlines` loads all
- [ ] Fix 4: Q13 — `enumerate` in correct order without `reversed()`
- [ ] Fix 5: Q14 — pathlib only, no `os.path` mixing

**Practice Questions:**
- [ ] PQ1: Polymorphism in one sentence. Three classes `Dog` `Cat` `Cow` each with `sound()`. Loop over a list of all three and call `sound()` without `if/elif`.
- [ ] PQ2: Difference between `_x` and `__x`. Write a class with both. Access both from outside and show exactly what happens — one works, one raises `AttributeError`.
- [ ] PQ3: `Temperature` class. `celsius` is stored privately. `@property fahrenheit` converts: $$F = C \times 1.8 + 32$$. Call `obj.fahrenheit` without parentheses.
- [ ] PQ4: Abstract class `Shape` with `@abstractmethod area()`. `Circle` and `Rectangle` implement it. Show `TypeError` when you try `Shape()` directly.
- [ ] PQ5: Write Encapsulation vs Abstraction as code comments. Include: what it protects, what it hides, and a real Data Engineering analogy for each.

**Homework:**
- [ ] HW1: Payment polymorphism. `UPIPayment` `CreditCardPayment` `CashPayment` — each has `process(amount)`. `checkout(payment, amount)` function works with all three without `isinstance` checks.
- [ ] HW2: `Employee` encapsulation. Private `_salary`. `give_raise(percent)` with two validations: percent must be positive, percent cannot exceed 50. Raise `ValueError` with clear message for each.
- [ ] HW3: Abstract `DataConnector`. `MySQLConnector` and `HDFSConnector` implement `connect()` and `read(query)`. `run_pipeline(connector)` works with both.
- [ ] HW4: `Rectangle`. Private `_width` and `_height`. Setters validate `> 0`. `area` and `perimeter` as computed `@property` — no parentheses when calling.
- [ ] HW5: Mini pipeline using all four pillars. Abstract `Pipeline`. `SalesPipeline` and `LogPipeline`. `run()` prints start and end timestamps. Show polymorphism by running both through one `execute(pipeline)` function.

**Notebook:** `notebooks/day_5/day_5.ipynb` | **Time Spent:** ___ mins

---

## Day 6
**Theme:** Magic Methods + Custom Exception Hierarchy + Operator Overloading

### 📚 Theory Foundation

**The Python Data Model:**
- Magic methods (dunders) are Python's hooks into built-in operations. You never call `obj.__str__()` directly — Python calls it automatically when you do `print(obj)` or `str(obj)`.
- This is how your custom classes behave like built-in types. Pandas DataFrames use `__len__`, `__getitem__`, `__iter__`. You'll write classes that do the same.

| Method | Triggered by | Example use |
|--------|-------------|-------------|
| `__str__` | `print(obj)`, `str(obj)` | Human-readable pipeline status |
| `__repr__` | REPL, `repr(obj)`, debug | Precise developer output |
| `__len__` | `len(obj)` | Row count of a dataset |
| `__eq__` | `obj1 == obj2` | Compare two schema objects |
| `__lt__` / `__gt__` | `obj1 < obj2` | Sort log entries by timestamp |
| `__add__` | `obj1 + obj2` | Merge two pipelines |
| `__contains__` | `x in obj` | Check if column exists in schema |
| `__getitem__` | `obj[key]` | Index into a data record |

- `__repr__` rule: if only one can be defined, define `__repr__` — Python falls back to it for both `str()` and REPL display.
- If you define `__eq__`, Python sets `__hash__` to `None` by default — your object becomes **unhashable** and cannot be added to a `set` or used as a dict key. Define `__hash__` explicitly if you need both.

**Custom Exception Hierarchy:**
```
PipelineError
├── ExtractionError
├── TransformationError
│   └── SchemaMismatchError
└── LoadError
    └── HDFSWriteError
```
- `raise HDFSWriteError("block write failed") from original_exc` — **exception chaining**. Both errors appear in the traceback. Always chain when re-raising a caught exception.
- Catch at the correct level: `ExtractionError` in the extract stage, `PipelineError` at the top for anything unexpected.

**Operator Overloading — Use Sparingly:**
- Only overload when the semantics genuinely make sense. `Vector + Vector` = add components ✅. `Record + Record` = unclear ❌.

**Videos:**
- [ ] `#40` Magic Methods In Python (8 min)
- [ ] `#41` Custom Exception In Python (7 min)
- [ ] `#42` Operator Overloading In Python (9 min)

**Practice Questions:**
- [ ] PQ1: `DataRecord` class wrapping a dict. `__str__` = readable, `__repr__` = precise with all fields shown, `__len__` = number of fields. Print an object vs type it in REPL — show the difference.
- [ ] PQ2: `Vector` class. `__add__` = component-wise. `__mul__` = scalar multiplication. `__eq__` = component equality. Prove `v1 + v2`, `v1 * 3`, `v1 == v2` all work naturally.
- [ ] PQ3: Pipeline exception hierarchy: `PipelineError` → `ExtractionError`, `TransformError`, `LoadError`. Raise `TransformError("column 'id' missing at row 47")`. Catch it. Print stage name + message cleanly.
- [ ] PQ4: `SchemaValidator` class. `__len__` = number of columns. `__contains__` = `'column_name' in validator`. `__eq__` = compare two schemas. Use it: `if 'id' not in schema: raise SchemaMismatchError`.
- [ ] PQ5: Define `__eq__` on a `LogEntry` class. Then try adding two `LogEntry` objects to a `set` — show what breaks. Fix it by adding `__hash__ = lambda self: hash(self.timestamp)`.

**Homework:**
- [ ] HW1: `DataPipeline` class. `__str__` lists stage names. `__len__` = stage count. `__repr__` = full config. `__add__` merges two pipelines into one with combined stages.
- [ ] HW2: `Matrix` class. `__add__` element-wise, `__mul__` scalar. `__eq__` compares. `__repr__` shows grid layout. Raise `ValueError` for shape mismatch on `__add__`.
- [ ] HW3: Full pipeline exception hierarchy: `PipelineError` → `CorruptFileError`, `EmptyFileError`, `UnsupportedFormatError`. Raise `CorruptFileError("sales.csv", line=1042)`. Chain it from a `ValueError`. Show both in traceback.
- [ ] HW4: `LogEntry` with `__str__`, `__repr__`, `__lt__` (sort by timestamp), `__eq__` + `__hash__`. Prove: `sorted(entries)` works and `set(entries)` deduplicates.
- [ ] HW5: `Dataset` class wrapping a list of dicts. `__len__` = row count. `__getitem__` = row access by index. `__contains__` = check if a dict is in dataset. `__iter__` = iterate rows. Combine all four in a processing loop.

**Notebook:** `notebooks/day_6/day_6.ipynb` | **Time Spent:** ___ mins

---

## Day 7
**Theme:** Iterators + Generators + Theory Supplement: Comprehensions + functools.reduce

### 📚 Theory Foundation

**The Iterator Protocol — What Every `for` Loop Actually Does:**
- An **iterable** has `__iter__()` — returns an iterator object
- An **iterator** has `__next__()` — returns next value, raises `StopIteration` when done
- Every `for` loop: Python calls `iter(obj)` to get an iterator, then calls `next()` repeatedly until `StopIteration`.
- Lists are *iterables* but NOT iterators. `iter([1,2,3])` creates an iterator. An iterator is **one-directional and single-use** — you cannot rewind it.

**Generators — The Most Critical Python Concept for Big Data:**
- A function with `yield` returns a **generator object** — which is an iterator.
- `yield` **suspends** execution, saves all local state, and returns a value. The next `next()` call resumes from exactly that line.
- `return` inside a generator raises `StopIteration`.

**Why Generators Are Fundamental to Big Data:**
```python
# This crashes on a 10GB file — loads everything into RAM first
lines = [line for line in open("10gb_log.txt")]   # ❌

# This uses O(1) memory — processes one line at a time
def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()   # ✅ one line at a time, always
```

The memory-efficient generator pipeline pattern:
```python
def read_lines(filename):          # Stage 1: one line at a time
    with open(filename) as f:
        for line in f:
            yield line.strip()

def filter_errors(lines):          # Stage 2: only error lines
    for line in lines:
        if "ERROR" in line:
            yield line

def parse_entry(lines):            # Stage 3: extract fields
    for line in lines:
        yield line.split("|")

# Chain all three — nothing runs until list() forces evaluation
pipeline = parse_entry(filter_errors(read_lines("app.log")))
results = list(pipeline)           # Data flows through all 3 stages one record at a time
```

This is **Spark's lazy evaluation** in a single process. Spark's `.filter()` and `.map()` also build a plan and execute only when `.collect()` or `.count()` is called. Understanding generators = understanding why Spark is designed the way it is.

---

### 📚 Theory Supplement: Comprehensions *(not in course videos — essential)*

**These appear in every Python codebase. Add to your permanent notes today.**

```python
# List comprehension — full list in memory
evens = [x for x in range(20) if x % 2 == 0]

# Dict comprehension — build dicts inline
lengths = {name: len(name) for name in ["alice", "bob", "charlie"]}
# → {'alice': 5, 'bob': 3, 'charlie': 7}

# Set comprehension — unique values only, automatic deduplication
unique_depts = {emp['dept'] for emp in employee_list}

# Generator expression — lazy, O(1) memory, same syntax as list but with ()
total = sum(x**2 for x in range(1_000_000))   # Never builds 1M item list
```

**When to use which:**
- `[...]` list comp → when you need to index, slice, or iterate multiple times
- `(...)` generator expression → when you pass directly to `sum()`, `max()`, `any()`, `all()`, `list()` — consumed once
- Comprehensions are faster than `for + append` — CPython optimises the bytecode

---

### 📚 Theory Supplement: functools.reduce *(not in course Python section — essential for MapReduce understanding)*

`functools.reduce(func, iterable, initial)`:
- Applies func cumulatively to collapse a sequence into one value:
```python
from functools import reduce
reduce(lambda acc, x: acc + x, [1, 2, 3, 4])  # → ((1+2)+3)+4 = 10
```
- `sum()`, `max()`, `min()` are all special cases of reduce
- **This IS the Reduce step in MapReduce.** When you learn MapReduce in Week 4, every reducer is doing `reduce(aggregation_func, all_values_for_this_key)`. Knowing this now makes MapReduce click immediately when you reach it.

**Videos:**
- [ ] `#43` Iterators In Python (6 min)
- [ ] `#44` Generators In Python (11 min)
- [ ] *(No video for Comprehensions/functools — theory above + PQs cover them)*

**Practice Questions:**
- [ ] PQ1: `CountRange(start, end, step)` class with `__iter__` and `__next__`. `for x in CountRange(0, 50, 5)` works. Then call `next()` manually on an instance and show `StopIteration` at the end.
- [ ] PQ2: Generator function `read_large_file(filename)` that yields one line at a time. Process a 10,000-line file. Print total lines processed and max line length — never load all into a list.
- [ ] PQ3: Generator pipeline. `generate_numbers(n)` → `square(nums)` → `filter_above_threshold(nums, threshold)`. Chain all three. Compare memory vs list version using a comment explaining why it matters.
- [ ] PQ4: `functools.reduce`. Use reduce only (no `sum`, `max`, `join`) to implement: product of list, maximum of list, concatenation of strings. Three separate calls.
- [ ] PQ5: Comprehension ETL. Given a list of transaction dicts: list comp for transactions above 1000, dict comp for `{id: amount}`, set comp for unique merchants, generator expression for total revenue.

**Homework:**
- [ ] HW1: Infinite `fibonacci()` generator. Use `itertools.islice(fibonacci(), 20)` to get first 20 numbers. Explain in a comment why storing all Fibonacci in a list is worse as N grows.
- [ ] HW2: Full log pipeline. `read_lines(file)` → `parse_log(lines)` → `filter_by_level(logs, "ERROR")` → `format_report(logs)`. Each is a generator. Chain and process 50,000 lines. Measure peak memory with `tracemalloc`.
- [ ] HW3: `functools.reduce` for pipeline. List of data transformation functions. Use `reduce(lambda data, fn: fn(data), functions, initial_data)` to apply them in sequence. This is a functional pipeline.
- [ ] HW4: List comp vs generator expression benchmark. Process 1 million numbers: square → filter above mean → sum. Compare memory using `tracemalloc`, compare time using `time.perf_counter`. Print results table.
- [ ] HW5: Dict and set comprehensions on sales data. Sales dicts with `product`, `region`, `amount`. Dict comp: `{product: total_sales}`. Set comp: `unique_regions`. Nested list comp: top 3 products per region.

**Week 1 Self-Check:**
- [ ] Can I write a class with all four OOP pillars without notes?
- [ ] Can I use map, filter, lambda, and comprehensions interchangeably?
- [ ] Can I write a generator function and explain what `yield` does to the call stack?
- [ ] Can I explain why generators are critical for processing large files?
- [ ] Can I use `functools.reduce` to aggregate a sequence?
- [ ] Can I write basic SQL SELECT / WHERE / GROUP BY / HAVING?

**Notebook:** `notebooks/day_7/day_7.ipynb` | **Time Spent:** ___ mins

---

## WEEK 2

---

## Day 8
**Theme:** Decorators — Dedicated Full Day

### 📚 Theory Foundation

**Closures — You Must Understand This Before Decorators:**
- A closure is a function that **remembers** variables from its enclosing scope, even after the outer function has returned.
```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor      # 'factor' is captured — lives on after make_multiplier returns
    return multiply

triple = make_multiplier(3)    # make_multiplier has returned, but 'factor=3' is still alive
triple(10)                     # → 30
```
Every decorator you write IS a closure. Understanding closures = understanding where the decorator's "memory" lives.

**The Decorator Pattern:**
- A decorator takes a function, returns a modified function.
- `@timer` is **exactly** `func = timer(func)` — just cleaner syntax.

```python
import functools
import time

def timer(func):
    @functools.wraps(func)                    # ← ALWAYS. Preserves __name__ and __doc__
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)        # Call the original
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result                         # Return original result unchanged
    return wrapper
```

**Why `@functools.wraps` is Non-Negotiable:**
- Without it: `func.__name__` returns `"wrapper"` for every decorated function.
- Your logs show: `"INFO: wrapper completed in 0.3s"` — useless.
- With it: `"INFO: extract_sales_data completed in 0.3s"` — actionable.
- Rule: every decorator you ever write gets `@functools.wraps(func)` on the wrapper. No exceptions.

**Decorator Factories — Decorators That Take Arguments:**
- `@retry(3)` needs three levels: factory (takes arg) → decorator (takes func) → wrapper (calls func)
```python
def retry(max_attempts):             # Level 1: factory — takes the argument
    def decorator(func):             # Level 2: decorator — takes the function
        @functools.wraps(func)
        def wrapper(*args, **kwargs):# Level 3: wrapper — calls the function
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"Attempt {attempt} failed: {e}. Retrying...")
        return wrapper
    return decorator
```

**Real Data Engineering Decorator Use Cases:**

| Decorator | What it does | Why it exists |
|-----------|-------------|---------------|
| `@timer` | Measures execution time per stage | Identify bottlenecks |
| `@retry(3)` | Retries on transient failure | Handle network/DB flakiness |
| `@log_call` | Logs entry, exit, return value | Full audit trail |
| `@validate_schema` | Checks DataFrame columns before processing | Catch schema drift early |
| `@checkpoint` | Saves intermediate result to disk | Resume after failure |

**Videos:**
- [ ] `#45` Decorators In Python (21 min)

**Practice Questions:**
- [ ] PQ1: `@timer` using `time.perf_counter()`. Apply to three functions with different runtimes. Output must include function name and time. Use `@functools.wraps`. Prove `func.__name__` is correct.
- [ ] PQ2: `@retry(n)` factory. Retries n times on any exception. Prints `"Attempt X of N failed: error"` on each retry. After N failures, re-raises the last exception. Test with a function that always fails first 2 attempts.
- [ ] PQ3: `@log_call` decorator. Logs function name, all args, all kwargs, return value, ISO timestamp. Use `logging` module (not print). Apply to a data processing function.
- [ ] PQ4: Stack `@timer` and `@retry(3)` on the same function. Run it. Draw the exact wrapping stack in a comment: what calls what in what order.
- [ ] PQ5: `@validate_positive`. Checks ALL positional args are positive numbers. Raises `ValueError("arg 2 must be positive, got -5")` with the position and value of the invalid argument. Apply to a financial calculation.

**Homework:**
- [ ] HW1: `@stage(name)` factory. Logs `"▶ Starting {name}"` on entry, `"✓ {name} completed in {time:.3f}s — {n} records processed"` on exit. Decorated function must return a list (the processed records).
- [ ] HW2: `@cache_result`. Stores return value in a dict keyed by a tuple of args. On second call with same args: skip function, return cached result. Log `"[cache HIT]"` or `"[cache MISS]"` each time.
- [ ] HW3: `@retry(attempts, delay, exceptions)` factory. Retries ONLY on the specified exception types (tuple). Waits `delay` seconds between retries using `time.sleep`. Logs each attempt with attempt number.
- [ ] HW4: Full decorated pipeline. Three functions `extract()`, `transform()`, `load()`. Each gets `@timer`, `@retry(3)`, AND `@stage("name")`. Show complete execution log with all decorator output visible.
- [ ] HW5: Explain decorator stacking order in a comment. When you write `@A` then `@B` then `def f()`, which runs first when you call `f()`? Write a concrete proof with two simple decorators that each print their name.

**Notebook:** `notebooks/day_8/day_8.ipynb` | **Time Spent:** ___ mins

---

## Day 9
**Theme:** NumPy — Dedicated Full Day

### 📚 Theory Foundation

**Why NumPy Exists — The Core Problem With Python Lists:**
- A Python list element = ~28 bytes (stores Python object with type info, reference count, value). Flexible, but slow and memory-heavy.
- A NumPy array = homogeneous dtype, stored as raw C memory, contiguous. An `int64` element = exactly 8 bytes. No overhead.
- Operations run in compiled C/Fortran, not interpreted Python — **vectorised**: one C call for the entire array, no Python loop.
- Performance: NumPy on 1M floats is ~100× faster than Python list loop. Memory: int64 array = 8 bytes/element vs Python list ≈ 56 bytes/element.

**Broadcasting — The Key to Clean NumPy:**
- Broadcasting: operations on arrays of different (compatible) shapes.
- Two dimensions are compatible if they're equal, OR one of them is 1.
- NumPy stretches the dimension of size 1 conceptually — no data is copied.
```python
prices    = np.array([[10], [20], [30]])  # shape (3, 1)
quantities = np.array([1, 2, 3, 4])       # shape (4,) → treated as (1, 4)
revenue = prices * quantities              # → shape (3, 4) — no loops needed
```

**Axis — The Always-Confusing Parameter:**
- `axis=0` = collapse **along rows** → result has one value per column
- `axis=1` = collapse **along columns** → result has one value per row
- Memory trick: `axis=0` = the axis you're **reducing**. Sum along `axis=0` = rows disappear.

**Why This Matters for Big Data:**
- Pandas `Series` and `DataFrame` are built on NumPy arrays.
- Apache Parquet and ORC (columnar storage formats used with HDFS and Spark) use the same principle: contiguous homogeneous data per column = fast scan, minimal overhead. Understanding NumPy memory layout is understanding why columnar formats are fast.

**Videos:**
- [ ] `#46` Working With NumPy In Python (28 min)

**Practice Questions:**
- [ ] PQ1: Create arrays three ways: `np.array()`, `np.zeros((3,4))`, `np.arange(0, 50, 5)`. Slice: first row, last column, every other row, a 2×2 sub-matrix from the centre.
- [ ] PQ2: Broadcasting. Predict the output shape of `(4, 1) + (1, 3)` on paper first. Then write the code and confirm with `.shape`. Explain what NumPy conceptually stretched.
- [ ] PQ3: Boolean indexing. Array of 20 random integers 0–100. One line: select all above mean. One line: replace all below 10 with 0. One line: count how many are in range 40–60.
- [ ] PQ4: Vectorized vs loop. Take square root of 1 million elements. Time both with `time.perf_counter()`. Print: `"NumPy: 0.008s | Loop: 0.842s | Speedup: 105x"`.
- [ ] PQ5: Axis operations. Create shape `(5, 4)` array. Predict output shape for `sum(axis=0)` and `sum(axis=1)` BEFORE running. Verify. Then: column means, row max, overall min.

**Homework:**
- [ ] HW1: Sales simulation. `(1000, 5)` array (1000 days × 5 products). Total per product (sum along axis=0), total per day (sum along axis=1), top 3 products by overall total, normalise each product's sales to 0–1 range. No loops.
- [ ] HW2: Statistics engine. `(100, 5)` exam scores. Per student: mean, highest score, whether passed (≥40 on ALL five). Per exam: mean, std, pass rate. No Pandas allowed.
- [ ] HW3: Boolean masking. Sensor readings array. Mask: below 0 = invalid, above 1000 = outlier. Count each category. Replace invalids with `np.nan`, replace outliers with column median.
- [ ] HW4: Broadcasting revenue matrix. Create price array `(m, 1)` and quantity array `(1, n)`. Multiply — result is `(m, n)` revenue matrix. No loops. Verify shape and spot-check two values manually.
- [ ] HW5: Matrix operations. Dot product (explain shape rule: `(m,n) @ (n,p) = (m,p)` in a comment). Transpose. `reshape`. Use a meaningful example for each (e.g., features × weights for a simple calculation).

**Notebook:** `notebooks/day_9/day_9.ipynb` | **Time Spent:** ___ mins

---

## Day 10 — TEST DAY
**Scope:** Python Days 1–9 (all Python topics covered so far)

**What the test covers:**
- Functional Python: `map`, `filter`, `lambda`, `functools.reduce`, comprehensions
- Modules + Standard Library: `os`, `pathlib`, `collections`, `random`, `datetime`
- File IO: `with open`, read modes, `for line in f` memory safety
- Exception Handling: hierarchy, chaining, custom exceptions, `try/except/else/finally`
- OOP: all four pillars, `__init__`, `super()`, MRO, `__mro__`
- Magic Methods + Operator Overloading + Dunder protocol
- Iterators + Generators: `__iter__`/`__next__`, `yield`, generator pipelines
- Decorators: closures, `@functools.wraps`, decorator factories
- NumPy: array creation, slicing, broadcasting, vectorization, axis operations

**Before test:** Watch `#47` Pandas DataFrame And Series as a preview — not tested, just orientation.

**Videos:** `#47` (preview only)
**TEST — questions given on Day 10**
**Score: ___/10 | Time: ___ mins**

---

## Day 11
**Theme:** Pandas — DataFrame + Series + Data Manipulation

### 📚 Theory Foundation

**The Pandas Mental Model:**
- A `DataFrame` = 2D labeled structure: rows have an **index**, columns have **names**
- Each column = a `Series` = 1D labeled array built on NumPy
- A DataFrame is essentially a **dict of Series, all sharing the same index**
- Pandas = labelled NumPy. PySpark DataFrame = distributed Pandas (almost). Learning Pandas now makes PySpark in Month 3 feel familiar.

**`.loc` vs `.iloc` — The One That Trips Everyone:**
- `.loc[label]` = label-based. Uses the actual index value.
- `.iloc[position]` = position-based. Always uses 0, 1, 2...
- After filtering, index retains original values. `df.reset_index(drop=True)` renumbers from 0.

**Copy vs View — Most Common Pandas Bug:**
```python
filtered = df[df['salary'] > 50000]          # This is a VIEW — not a copy
filtered['bonus'] = filtered['salary'] * 0.1  # ⚠️ SettingWithCopyWarning

filtered = df[df['salary'] > 50000].copy()    # ✅ This is safe
filtered['bonus'] = filtered['salary'] * 0.1  # No warning, no bug
```
Rule: **any time you filter and then plan to modify, call `.copy()` immediately**.

**groupby — Split-Apply-Combine (This Is MapReduce at Small Scale):**
- `groupby` follows: **split** into groups → **apply** function → **combine** results
- This is MapReduce: split = Map phase, apply+combine = Reduce phase.
- `.agg({'salary': ['mean', 'max'], 'id': 'count'})` — multiple aggregations at once

**apply() — Use Sparingly:**
- `df['col'].apply(func)` is a Python loop under the hood — slow
- Vectorised operations (`df['col'] * 2`, `np.sqrt(df['col'])`) run in C — fast
- Rule: try vectorised first. Only use `apply()` when you genuinely cannot express it vectorised.

**Videos:**
- [ ] `#47` Pandas DataFrame And Series (29 min)
- [ ] `#48` Data Manipulation And Analysis (24 min)

**Practice Questions:**
- [ ] PQ1: Read a CSV into a DataFrame. Check shape, dtypes, null count per column. Show first 5 and last 3 rows. Select only numeric columns.
- [ ] PQ2: `.loc` vs `.iloc`. Create a DataFrame with a non-default index. Select the same row using both. Show the difference. Explain when each breaks.
- [ ] PQ3: `groupby`. Sales data: `product`, `region`, `amount`. Multi-agg: mean and sum of amount per product. Filter groups where sum > 5000.
- [ ] PQ4: Copy vs view. Demonstrate the `SettingWithCopyWarning` on purpose. Fix it with `.copy()`. Confirm the original DataFrame is unchanged.
- [ ] PQ5: Boolean indexing + string operations. Filter rows where name contains "Ltd" (case-insensitive). Add a column that categorises amount as "High" / "Low" / "Medium".

**Homework:**
- [ ] HW1: Load a real CSV (use any public dataset). Clean: drop fully null rows, fill numeric nulls with column median, rename columns to snake_case.
- [ ] HW2: `groupby` multi-agg. Sales: total revenue per region, average order value per product per region, top 5 products by revenue. Use `.agg` with a dict.
- [ ] HW3: `pd.merge` — INNER, LEFT, RIGHT. Employees table + departments table. Find employees with no department using LEFT JOIN + `isnull()`.
- [ ] HW4: Vectorised calculation vs `apply` benchmark. Add two columns using vectorised arithmetic. Same computation with `apply(lambda row: ..., axis=1)`. Time both. Show speedup.
- [ ] HW5: `pivot_table`. Monthly sales data. Pivot: rows = product, columns = month, values = sum(amount). Show how this connects to `groupby` conceptually in a comment.

**Notebook:** `notebooks/day_11/day_11.ipynb` | **Time Spent:** ___ mins

---

## Day 12
**Theme:** Data Source Reading + Python With SQLite | SQL: JOINs

### 📚 Theory Foundation

**Data Source Reading — Why This Matters:**
- In production, data rarely comes from one clean CSV. You'll read: CSVs with custom delimiters, JSON files, Excel sheets, Parquet (the binary columnar format used in Hadoop/Spark), and databases.
- `pd.read_csv(filepath, chunksize=10000)` returns a **chunk iterator** — reads 10,000 rows at a time. Essential for files that don't fit in RAM.
- **Parquet:** columnar binary format. Pandas `read_parquet()` uses Apache Arrow under the hood — same memory layout as NumPy. Parquet is the native format for Spark and HDFS in production.

**Python With SQLite — Embedded Database from Python:**
- SQLite is a file-based database — no server, no setup. The entire database is one `.db` file.
- `sqlite3` is in Python's standard library — no install needed.
- `conn = sqlite3.connect("data.db")` creates/opens the file.
- `conn.cursor().execute("SELECT ...")` runs SQL.
- `pd.read_sql("SELECT ...", conn)` = run SQL and get a DataFrame directly.
- This is the same pattern used for MySQL, PostgreSQL — just swap `sqlite3.connect()` with the appropriate library. The SQL stays identical.

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect("pipeline.db")
df = pd.read_sql("SELECT * FROM sales WHERE amount > 1000", conn)
conn.close()
```

**Videos:**
- [ ] `#49` Data Source Reading (15 min)
- [ ] `#50` Python With SQLite (16 min)

**Practice Questions:**
- [ ] PQ1: Read a CSV with `chunksize=1000`. Process each chunk: filter rows above threshold, sum a column. Print running total without loading full file into memory.
- [ ] PQ2: Read JSON file into Pandas. Handle nested JSON (use `pd.json_normalize()`). Show before and after.
- [ ] PQ3: SQLite. Create a table, insert 10 rows, query with WHERE, update one row, delete another. Then read the whole table into a DataFrame.
- [ ] PQ4: `pd.read_sql`. Run a GROUP BY query directly via SQLite connection and get the result as a DataFrame. No manual parsing.
- [ ] PQ5: Chunked processing pipeline. Read a large CSV in chunks. Filter, transform, and write each chunk to a new CSV. Never hold more than one chunk in memory.

**Homework:**
- [ ] HW1: Read 3 different formats (CSV, JSON, one more from the video). Clean each. Write all to Parquet. Reload from Parquet and verify data matches.
- [ ] HW2: SQLite pipeline. Create a `sales` table. Insert 100 rows from a DataFrame using `df.to_sql()`. Query with JOINs across two tables. Read result into Pandas.
- [ ] HW3: Chunked aggregation. Large CSV in 10,000-row chunks. Aggregate `sum` and `count` per category across all chunks using a running dict. Final result = full aggregation without loading file.
- [ ] HW4: Parameterised SQL. Function `query_sales(conn, min_amount, region)`. Builds a safe parameterised query (NO string formatting — use `?` placeholders). Returns DataFrame.
- [ ] HW5: Data source comparison. Same dataset read from CSV, JSON, SQLite, and Parquet. Compare: file size, read time, memory usage. Print a comparison table.

**SQL Day — JOINs:**
- [ ] SQL1: `INNER JOIN` employees with departments. Show: employee name, salary, department name. Filter: only departments in 'Engineering' or 'Data'.
- [ ] SQL2: `LEFT JOIN` employees to projects. Find employees with NO project assigned (`project_id IS NULL` after join). Show count per department.

**Notebook:** `notebooks/day_12/day_12.ipynb` | **Time Spent:** ___ mins

---

## Day 13
**Theme:** Logging — Complete (all 3 videos)

### 📚 Theory Foundation

**Why `print()` Is Not Enough in Production:**

| `print()` | `logging` |
|-----------|-----------|
| Goes to stdout only | Console AND file simultaneously |
| No levels | DEBUG / INFO / WARNING / ERROR / CRITICAL |
| No timestamps | Timestamp in every line |
| No module name | Automatically records which module/function logged |
| Can't be turned off | Set level — DEBUG messages disappear in production |
| No formatting control | Full format string control |

**Setting Up a Production-Grade Logger:**
```python
import logging

def get_logger(name: str, log_file: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Console handler — INFO and above
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)

    # File handler — DEBUG and above (everything)
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger
```

**What a Pipeline Stage Should Log:**
```python
logger.info(f"Starting extract — source: {source}")
logger.debug(f"Reading {n_chunks} chunks of {chunk_size} rows each")
logger.info(f"Extracted {len(df)} rows in {elapsed:.3f}s")
logger.warning(f"Null values found in column 'id': {null_count} rows affected")
logger.error(f"Failed to connect to source: {e}")
```

**Why This Is Critical for Big Data:**
- In a Hadoop/Spark cluster, jobs run on 10–200 machines simultaneously. You cannot `print()` your way to debugging.
- Every data pipeline in production has structured logging. The Day 29 mini project requires it. The `@log_call` decorator from Day 8 should use `logging`, not `print`.

**Videos:**
- [ ] `#51` Logging In Python (14 min)
- [ ] `#52` Logging With Multiple Loggers (4 min)
- [ ] `#53` Logging In Real World Examples (7 min)
- [ ] `#54` Python Outro (1 min)

**Practice Questions:**
- [ ] PQ1: Setup logger with two handlers (console: INFO+, file: DEBUG+). Custom format with timestamp + module name + level + message. Write one message at each of the 5 levels. Check what appears in console vs file.
- [ ] PQ2: Module-level logger. `logger = logging.getLogger(__name__)` in three different Python files. Import and use all three in a main script. Show that each log line identifies its source module.
- [ ] PQ3: Retrofit Day 8's `@log_call` decorator. Replace every `print()` inside it with `logging.debug()` and `logging.info()`. Re-run and show the output difference.
- [ ] PQ4: Logging in exception handling. `try/except` block in a file-reading function. Log the error with `logger.error("...", exc_info=True)` — this appends the full traceback automatically.
- [ ] PQ5: Log rotation. Use `logging.handlers.RotatingFileHandler(maxBytes=1MB, backupCount=5)`. Explain why this matters in a pipeline that runs daily for a year.

**Homework:**
- [ ] HW1: Full pipeline logger. `PipelineLogger` class. `start_stage(name)` / `end_stage(name, records, elapsed)` / `log_warning(msg)` / `log_error(msg, exc_info)`. Uses `logging` internally. Apply to your Day 8 pipeline.
- [ ] HW2: Multiple module loggers. `extractor.py`, `transformer.py`, `loader.py` each have their own `__name__` logger. Main script imports all three. Log appears with correct source on each line.
- [ ] HW3: Real-world pattern. Process 1000 records. Log: start, every 100 records ("Processed 200/1000"), any warning (null found), any error (parse failed), final summary (success + fail counts).
- [ ] HW4: Integrate logging with decorators. Modify `@stage(name)` from Day 8 HW1 to use `logging.getLogger("pipeline.{name}")` instead of print. Show structured log output.
- [ ] HW5: Log analysis. Write a pipeline that: generates 500 log lines (mix of INFO/WARNING/ERROR), writes to file, reads the file back, uses pandas to count messages per level, and prints a summary table.

**Notebook:** `notebooks/day_13/day_13.ipynb` | **Time Spent:** ___ mins

---

## Day 14
**Theme:** Big Data Intro + 5 V's + Distributed Systems + On-Prem vs Cloud + Designing Big Data Systems

### 📚 Theory Foundation *(pure theory day — no coding)*

**Why Single Machines Fail:**
- Hard ceiling: fixed CPU cores, fixed RAM, fixed disk. Vertical scaling (bigger machine) is expensive and has a physical limit.
- Horizontal scaling (more machines) = how the internet is built = how Big Data tools work.
- Distributed computing: split the data, process parts in parallel, combine results.

**The 5 V's:**

| V | Meaning | Real Example | Tool That Solves It |
|---|---------|-------------|---------------------|
| **Volume** | Amount of data | Petabytes of logs | HDFS, S3 |
| **Velocity** | Speed of arrival | 1M events/second | Kafka, Spark Streaming |
| **Variety** | Different formats | CSV + JSON + images | Data Lake |
| **Veracity** | Quality/accuracy | Noisy sensor readings | Cleaning pipelines |
| **Value** | Business worth | Actionable insights | Analytics layer |

**Distributed Computing Fundamentals:**
- **Cluster:** Group of machines (nodes) working together, appearing as one system
- **Master/Worker:** One node coordinates (NameNode, Spark Master), others execute
- **Data Locality:** Move computation to data, not data to computation. Moving a 1KB program is fast. Moving 1TB of data is slow. This is the central design principle of Hadoop.
- **Fault Tolerance:** Assume machines WILL fail. Design for it from the start. Replicate data. Retry jobs automatically.

**On-Prem vs Cloud:**
- On-Prem: your own hardware, full control, high upfront cost, fixed capacity
- Cloud: rented hardware, pay per use, instant scale, someone else manages the physical layer
- For Big Data: cloud is now dominant — GCP Dataproc, AWS EMR, Azure HDInsight all run managed Hadoop/Spark clusters

**Designing a Good Big Data System — Four Principles:**
1. **Scalability:** adding nodes improves performance linearly
2. **Fault tolerance:** no single point of failure
3. **Data locality:** process data where it lives
4. **Schema flexibility:** handle variety without breaking the pipeline

**Videos:**
- [ ] `#57` Section Intro (1 min)
- [ ] `#58` What is Big Data — A Practical Example (18 min)
- [ ] `#59` 5 V's of Big Data (22 min)
- [ ] `#60` Big Data and Distributed Systems (17 min)
- [ ] `#61` Designing a Good Big Data System (11 min)
- [ ] `#62` On-Premise Infra vs Cloud Solutions (20 min)

PQs: [ ] PQ1 [ ] PQ2 [ ] PQ3 [ ] PQ4 [ ] PQ5
HWs: [ ] HW1 [ ] HW2 [ ] HW3 [ ] HW4 [ ] HW5

**Notebook:** `notebooks/day_14/day_14.ipynb` | **Time Spent:** ___ mins

---

## WEEK 3

---

## Day 15
**Theme:** DB vs DW vs Data Lake + ETL vs ELT + What Does a Data Engineer Do | SQL: Subqueries

### 📚 Theory Foundation

**Storage Layer Architecture:**

| | Database (OLTP) | Data Warehouse (OLAP) | Data Lake |
|--|--------|--------------|-----------|
| **Purpose** | Transactions | Analytics | Raw storage |
| **Schema** | Write time | Write time | Read time |
| **Data** | Current, structured | Historical, structured | Any format |
| **Example** | MySQL, PostgreSQL | BigQuery, Redshift | HDFS, S3 |

- **Schema on Write:** define structure before storing. Always clean, but inflexible — changing schema = migration.
- **Schema on Read:** store raw, interpret when reading. Flexible, but you must handle messy data.
- **Lakehouse:** combines both — Delta Lake, Apache Iceberg. This is where the industry is moving.

**ETL vs ELT:**
- **ETL** (Extract → Transform → Load): Transform first, load clean data to warehouse. Traditional, Hadoop-era approach. Good when the destination is expensive.
- **ELT** (Extract → Load → Transform): Load raw first, transform inside the warehouse/lake. Modern, cloud-era approach. Good when storage is cheap (S3, GCS) and compute is elastic (Spark).
- Hadoop → ETL. Cloud → ELT. You'll work with both.

**Videos:**
- [ ] `#63` Database vs Data Warehouse vs Data Lake (29 min)
- [ ] `#64` ETL vs ELT (21 min)
- [ ] `#65` What does a Data Engineer do & Where Big Data Fits in? (18 min)

**SQL Day — Subqueries:**
- [ ] SQL1: Subquery in WHERE. Find employees earning more than the average salary of their own department.
- [ ] SQL2: Subquery in FROM (inline view). Calculate department-level stats, then filter departments where the average salary is above the company-wide average.

PQs: [ ] x5 | HWs: [ ] x5 | **Time: ___ mins**

---

## Day 16
**Theme:** Hadoop Intro + Hadoop Ecosystem

### 📚 Theory Foundation
- Hadoop origin: Google published GFS (2003) and MapReduce (2004) papers. Yahoo engineers (Doug Cutting) built open-source versions: HDFS + MapReduce = Hadoop (2006). Core insight: **commodity hardware is cheap, networks are expensive — store data where it's processed.**
- **Three core layers:** HDFS (storage) + MapReduce (processing) + YARN (resource management). Everything else — Hive, Pig, HBase, Spark — sits on top.
- **Properties:** Distributed, fault-tolerant, scalable, open-source, cost-effective (commodity hardware), write-once read-many optimised.
- **Ecosystem components:** Hive (SQL on Hadoop), Pig (scripting), HBase (NoSQL on HDFS), Sqoop (DB ↔ HDFS), Flume (log ingestion), Oozie (workflow scheduler), ZooKeeper (coordination). Spark replaces MapReduce as the processing engine.

**Videos:**
- [ ] `#66` Section Intro (2 min)
- [ ] `#67` Introduction To Hadoop (5 min)
- [ ] `#68` Properties of Hadoop (9 min)
- [ ] `#69` Hadoop Ecosystem — Main Components (9 min)
- [ ] `#70` Hadoop Ecosystem — Components (29 min)

PQs: [ ] x5 | HWs: [ ] x5 | **Time: ___ mins**

---

## Day 17
**Theme:** HDFS Architecture + Blocks + Replication | SQL: CASE WHEN + NULL handling

### 📚 Theory Foundation
- HDFS is a file system for large files on commodity hardware. Optimised for **sequential reads**, not random access. Write-once, read-many.
- **NameNode:** master node. Stores ALL metadata: file names, block locations, DataNode assignments, replication status. Runs in RAM. Single point of failure in non-HA setups.
- **DataNode:** worker nodes. Store actual data blocks. Many of them. Send heartbeats to NameNode every 3 seconds.
- **Default block size:** 128MB (configurable). A 1GB file = 8 blocks. Why large? Minimises NameNode metadata entries. Optimises sequential disk reads.
- **Replication factor:** default 3. Each block on 3 different DataNodes. Provides fault tolerance.
- **Replication placement (rack-aware):** First replica on local node, second on different rack, third on same rack as second. Balances durability vs network bandwidth cost.

**Videos:**
- [ ] `#71` Intro to HDFS and Common Terminology (22 min)
- [ ] `#72` Why HDFS (4 min)
- [ ] `#73` HDFS Architecture (15 min)
- [ ] `#74` Blocks In HDFS (12 min)
- [ ] `#75` Replication Factor in HDFS (9 min)

**SQL Day — CASE WHEN + NULL handling:**
- [ ] SQL1: `CASE WHEN` to categorise salary into bands: `< 30k = 'Junior'`, `30k–60k = 'Mid'`, `> 60k = 'Senior'`. Count per band.
- [ ] SQL2: NULL handling. `COALESCE(column, 0)` for nullable numbers. `IS NULL` / `IS NOT NULL` in WHERE. `NULLIF(a, b)` to avoid divide-by-zero.

PQs: [ ] x5 | HWs: [ ] x5 | **Time: ___ mins**

---

## Day 18
**Theme:** Rack Awareness + Node Failure (temporary + permanent) + GCP Account Setup

### 📚 Theory Foundation
- **Rack awareness:** NameNode knows which nodes are on the same physical rack. Placing replicas across racks means a full rack power failure cannot lose a block.
- **Temporary DataNode failure:** stops sending heartbeats. After 10 min timeout, NameNode marks it dead. Under-replicated blocks are automatically re-replicated to other DataNodes. System self-heals.
- **Permanent DataNode failure:** node is decommissioned. All blocks it held must be re-replicated. HDFS re-balancer redistributes data evenly. Admin runs `hdfs dfsadmin -decommission <node>`.
- **GCP note:** `#78` is Create GCP Account — set up your account now if you haven't. You'll need it for Day 21 (cluster creation). This is not testable but is required for practicals.

**Videos:**
- [ ] `#76` Rack Awareness in HDFS (7 min)
- [ ] `#77` Node Failure *(section title — 0 min)*
- [ ] `#78` Create GCP Account (24 min) — ⚠️ create your account during this video
- [ ] `#79` Data Node Failure — Temporary (11 min)
- [ ] `#80` Data Node Failure — Permanent (14 min)

PQs: [ ] x5 | HWs: [ ] x5 | **Time: ___ mins**

---

## Day 19
**Theme:** NameNode HA Architecture + HDFS Read/Write Flow | SQL: Window Functions

### 📚 Theory Foundation
- **Secondary NameNode (misleading name):** NOT a standby. Periodically merges `EditLog` with `FsImage` (checkpoint). Prevents EditLog growing unboundedly. Does NOT take over if NameNode dies.
- **Standby NameNode (true HA):** Hot standby. Uses **ZooKeeper** for leader election. Uses **JournalNodes** (quorum-based shared log) so both Active and Standby see all edits. Takes over in seconds.
- **Fencing:** Prevents split-brain — old Active NameNode is fenced (killed/isolated) before Standby is promoted. Without fencing, both could accept writes → data corruption.
- **HDFS Write flow:** Client → NameNode (get DataNode pipeline) → write to DN1 → DN1 pipelines to DN2 → DN2 to DN3. ACKs flow back up the pipeline. NameNode is NOT in the data path.
- **HDFS Read flow:** Client → NameNode (get block locations + DataNode list) → Client reads each block directly from nearest DataNode. NameNode serves only metadata, never data.
- **Data locality in reads:** Client picks closest DataNode (same node > same rack > other rack). Minimises network I/O. This is the data locality principle in practice.

**Videos:**
- [ ] `#81` Secondary Name Node (17 min)
- [ ] `#82` Standby Name Node (10 min)
- [ ] `#83` Hadoop HA Architecture (20 min)
- [ ] `#84` Data Write in HDFS (22 min)
- [ ] `#85` Read Request in HDFS (10 min)

**SQL Day — Window Functions:**
- [ ] SQL1: `ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC)` — rank employees within department.
- [ ] SQL2: `LAG(salary, 1) OVER (ORDER BY hire_date)` — compare each employee's salary to the previous hire. Also: `SUM(amount) OVER (PARTITION BY month ORDER BY day)` — running total.

PQs: [ ] x5 | HWs: [ ] x5 | **Time: ___ mins**

---

## Day 20 — TEST DAY
**Scope:** Big Data Theory + Hadoop + HDFS (Days 14–19)

Covers: 5 V's, DB/DW/Lake, ETL/ELT, Hadoop ecosystem, HDFS architecture, blocks, replication, rack awareness, node failure recovery, Secondary vs Standby NameNode, HA architecture, HDFS read/write flow.

**Before test:** Watch `#86` GCP Hadoop Cluster Creation as a preview.

**Videos:** `#86` (preview)
**TEST — questions given on Day 20**
**Score: ___/12 | Time: ___ mins**

---

## Day 21
**Theme:** GCP Cluster Setup + Linux Commands

### 📚 Theory Foundation
- **Linux essentials for Big Data:** Every Hadoop cluster runs on Linux. You'll SSH into nodes, navigate HDFS, debug jobs via command line.
- Key commands: `grep`, `awk`, `cut`, `sort`, `uniq -c`, `wc -l`, `head`, `tail`, `find`, `chmod`, `chown`, `ps aux`, `top`
- **Log parsing pipeline in bash:** `cat app.log | grep "ERROR" | cut -d'|' -f2 | sort | uniq -c | sort -rn | head -10` — top 10 most frequent error messages, no Python needed.
- GCP practicals here are hands-on — follow along with the video. If GCP account isn't set up yet, do it now.

**Videos:**
- [ ] `#86` GCP Hadoop Cluster Creation (29 min)
- [ ] `#87` Exploring our Hadoop Cluster (24 min)
- [ ] `#88` GCP Cluster Best Practices (4 min)
- [ ] `#89` Linux Commands — 1 (32 min)
- [ ] `#90` Linux Commands — 2 (27 min)

PQs: [ ] x5 | HWs: [ ] x5 | **Time: ___ mins**

**Week 3 Self-Check:**
- [ ] Can I explain HDFS architecture end to end without notes?
- [ ] Can I clearly state the difference between Secondary NameNode and Standby NameNode?
- [ ] Can I trace a full HDFS read and write flow step by step including ACKs?
- [ ] Do I understand rack-aware replication placement strategy?
- [ ] Can I write SQL window functions: `ROW_NUMBER`, `RANK`, `LAG`, `LEAD`, `SUM OVER`?
- [ ] Have I set up my GCP account?

---

## WEEK 4

---

## Day 22
**Theme:** HDFS Commands + MapReduce Intro + Core Concepts | SQL: CTEs

### 📚 Theory Foundation
**HDFS Commands (HDFS CLI mirrors Linux, prefixed with `hdfs dfs -`):**

| Command | What it does |
|---------|-------------|
| `hdfs dfs -ls /path` | List files |
| `hdfs dfs -mkdir /path` | Create directory |
| `hdfs dfs -put local.csv /hdfs/path` | Upload from local to HDFS |
| `hdfs dfs -get /hdfs/path local.csv` | Download from HDFS to local |
| `hdfs dfs -cat /hdfs/file` | Print file contents |
| `hdfs dfs -rm -r /path` | Delete (recursive) |
| `hdfs fsck /path` | Check HDFS health, show under-replicated blocks |
| `hdfs dfsadmin -report` | Cluster health: capacity, live DataNodes, missing blocks |

**MapReduce — The Core Concept:**
- A programming model for processing large datasets in parallel across a cluster.
- **Map phase:** Each mapper processes one input split (~128MB). Emits `(key, value)` pairs.
- **Shuffle & Sort:** Framework automatically groups all values with the same key. You write nothing for this.
- **Reduce phase:** Each reducer receives all values for one key. Aggregates and emits final output.
- **Connection to Day 7:** The Reduce phase IS `functools.reduce(aggregation_func, all_values_for_this_key)`. Knowing this makes MapReduce click immediately.
- **Data locality:** framework schedules mappers on the nodes where the input data blocks live.

**Videos:**
- [ ] `#91` HDFS Commands (30 min)
- [ ] `#92` Hadoop Outro (2 min)
- [ ] `#93` Map Reduce Intro (1 min)
- [ ] `#94` Intro to Distributed Processing (11 min)
- [ ] `#95` Map Reduce Introduction (17 min)
- [ ] `#96` Map Reduce & Cluster (12 min)

**SQL Day — CTEs:**
- [ ] SQL1: `WITH dept_avg AS (SELECT dept, AVG(salary) avg_sal FROM employees GROUP BY dept)` — join back to employees to find employees earning above their department average.
- [ ] SQL2: Recursive CTE (optional if covered in course). Non-recursive: chain two CTEs — one to clean data, one to aggregate.

PQs: [ ] x5 | HWs: [ ] x5 | **Time: ___ mins**

---

## Day 23
**Theme:** MapReduce Practicals — Word Count + Examples

### 📚 Theory Foundation
- **Word Count** = the "Hello World" of MapReduce:
  - Map: for each word in input → emit `(word, 1)`
  - Shuffle: groups all `(hadoop, 1), (hadoop, 1), (hadoop, 1)` → `(hadoop, [1, 1, 1])`
  - Reduce: sum the values → `(hadoop, 3)`
- Follow practicals hands-on on your GCP cluster from Day 21.

**Videos:**
- [ ] `#97` Map Reduce Practical Part 1 (17 min)
- [ ] `#98` MR Example Part 2 (22 min)

PQs: [ ] x5 | HWs: [ ] x5 | **Time: ___ mins**

---

## Day 24
**Theme:** MapReduce — 1 Reducer + 2 Reducers | SQL: String + Date Functions

### 📚 Theory Foundation
- **Number of reducers:** controls parallelism in the reduce phase. More reducers = more parallelism = more output files.
- 1 reducer: all keys go to one reducer. Simple but bottleneck for large datasets.
- 2 reducers: keys partitioned across two. Default partitioning: `hash(key) % num_reducers`.
- Custom partitioner: controls which key goes to which reducer (e.g., by first letter of word).

**Videos:**
- [ ] `#99` MR Practical with 1 Reducer (39 min) — ⚠️ long video, take notes
- [ ] `#100` MR with 2 Reducers Practical (29 min)

**SQL Day — String + Date Functions:**
- [ ] SQL1: String functions: `UPPER()`, `LOWER()`, `CONCAT()`, `SUBSTRING()`, `TRIM()`, `LENGTH()`, `REPLACE()`. Build a formatted name column from first + last name.
- [ ] SQL2: Date functions: `NOW()`, `DATE()`, `DATEDIFF()`, `DATE_ADD()`, `YEAR()`, `MONTH()`. Find employees hired in the last 90 days. Calculate tenure in years.

PQs: [ ] x5 | HWs: [ ] x5 | **Time: ___ mins**

---

## Day 25
**Theme:** Combiner + Zero Reducer + Big Log File + Input Splits

### 📚 Theory Foundation
- **Combiner:** mini-reducer that runs on the mapper's output before sending to the network. Reduces shuffle data — often the bottleneck in MR jobs.
- Combiner rule: must be **commutative and associative**. Sum works ✅. Average does NOT ❌ (partial averages cannot be combined into a correct global average).
- **Zero Reducer:** skip reduce phase entirely. Output = mapper output directly. Use when: filtering, transforming, no aggregation needed.
- **Input Splits:** logical division of input data. One mapper per split. Split size ≠ block size (usually equal but configurable). Small splits = more parallelism but more overhead. Large splits = less overhead but less parallelism.

**Videos:**
- [ ] `#101` Combiner in MR (13 min)
- [ ] `#102` Map Reduce with 0 Reducer (15 min)
- [ ] `#103` MR on Big Log File (20 min)
- [ ] `#104` Input Split in MR (7 min)
- [ ] `#105` Map Reduce Outro (2 min)

PQs: [ ] x5 | HWs: [ ] x5 | **Time: ___ mins**

---

## Day 26
**Theme:** YARN — Complete | SQL: Indexes + Query Optimization

### 📚 Theory Foundation
- **Why YARN:** Hadoop 1.x had JobTracker doing both resource management AND job tracking. It was a bottleneck and single point of failure. YARN splits these concerns.
- **ResourceManager:** cluster-level. Manages CPU + memory across ALL applications. One per cluster.
- **NodeManager:** per-node. Manages containers on that node. Reports to ResourceManager.
- **ApplicationMaster:** per-application. Negotiates resources with ResourceManager. Coordinates containers. Lives inside a container itself.
- **Container:** a resource allocation unit (e.g., 4GB RAM, 2 cores). All job work happens in containers.

**YARN Job Flow:**
```
1. Client submits job to ResourceManager
2. RM allocates a container for the ApplicationMaster
3. AM starts, registers with RM
4. AM requests containers from RM for actual work
5. NodeManagers launch containers as instructed by RM
6. AM monitors containers, requests replacement if one fails
7. Job completes → AM deregisters from RM → containers released
```

**Fault tolerance in YARN:**
- Container fails → AM requests a replacement from RM
- AM fails → RM restarts it (and AM recovers from checkpoint)
- RM fails → HA RM with ZooKeeper (same pattern as HDFS HA)

**Videos:**
- [ ] `#106` YARN Section Intro (1 min)
- [ ] `#107` YARN Introduction (5 min)
- [ ] `#108` Components of YARN (22 min)
- [ ] `#109` YARN Analogy (5 min)
- [ ] `#110` YARN Process Step by Step (28 min)

**SQL Day — Indexes + Query Optimization:**
- [ ] SQL1: Create an index on a high-cardinality column. Show `EXPLAIN` output before and after. Compare `ALL` (full scan) vs `ref` (index used).
- [ ] SQL2: Query optimization. Rewrite a slow query using: appropriate JOIN type, WHERE before HAVING, index hint, avoiding `SELECT *`, LIMIT early.

PQs: [ ] x5 | HWs: [ ] x5 | **Time: ___ mins**

---

## Day 27
**Theme:** Review + Catch-Up Day

- [ ] Re-watch any video where PQ score was below 3/5
- [ ] Redo the hardest HW from any week
- [ ] Write Month 1 concept map: Python → File IO → OOP → Generators → Decorators → NumPy → Pandas → Logging → Big Data → Hadoop → HDFS → MapReduce → YARN
- [ ] Connect the thread: generator lazy evaluation → Spark lazy evaluation → YARN container lifecycle
- [ ] Start mini project README if not started

**Time: ___ mins**

---

## Day 28
**Theme:** Buffer + SQL Full Revision

- [ ] Re-watch any Hadoop/HDFS/MR/YARN video that felt unclear
- [ ] Redo any incomplete HW from Week 4
- [ ] Write one-page summary: MapReduce end-to-end flow + YARN job submission flow

**SQL Revision Day:**
- [ ] SQL Mixed 1: Write a query using JOINs + CTE + Window Function + CASE WHEN in one query
- [ ] SQL Mixed 2: Subquery + GROUP BY + HAVING + String function in one query

**Time: ___ mins**

---

## Day 29
**Theme:** Month 1 Mini Project

**Requirements:**
- [ ] Reads a real CSV file using Pandas with chunked loading (`chunksize`)
- [ ] Cleans data: drop nulls, fix dtypes, rename columns to snake_case
- [ ] Transforms: filter, groupby, aggregate, add derived column
- [ ] Writes output to both CSV and Parquet
- [ ] `@timer` and `@retry(3)` on each stage (from Day 8)
- [ ] Full logging to console AND log file using `logging` (from Day 13)
- [ ] Generator-based chunked reading (from Day 7)
- [ ] Abstract `Pipeline` base class with concrete `SalesPipeline` (from Days 4–5)
- [ ] `README.md`: purpose, setup instructions, how to run, sample output

**GitHub Link:** ___ | **Time: ___ mins**

---

## Day 30 — FINAL TEST DAY
**Scope:** Full Month 1 — Python + Big Data + Hadoop + HDFS + MapReduce + YARN + SQL

**TEST — questions given on Day 30**
**Score: ___/12**

---

## Month 1 Final Self-Assessment

| Topic | Rating 1–5 | Need More Work |
|-------|-----------|----------------|
| Lambda · Map · Filter | | |
| Comprehensions (list/dict/set/generator) | | |
| functools.reduce + partial | | |
| File IO + Exception Handling + Context Managers | | |
| OOP: Classes + Inheritance + MRO | | |
| OOP: Magic Methods + Encapsulation + Abstraction | | |
| Iterators + Generators + Generator Pipelines | | |
| Decorators + Decorator Factories + functools.wraps | | |
| NumPy: arrays, broadcasting, axis, vectorization | | |
| Pandas: DataFrame, groupby, merge, chunked reading | | |
| Data Source Reading + SQLite | | |
| Logging: setup, levels, multi-handler, production patterns | | |
| Big Data 5 V's + Distributed Computing fundamentals | | |
| ETL vs ELT · DB vs DW vs Data Lake | | |
| Hadoop: origin, properties, ecosystem | | |
| HDFS: architecture, blocks, replication, rack-aware | | |
| NameNode HA: Secondary vs Standby (critical difference) | | |
| HDFS Read + Write flow step by step | | |
| MapReduce: Map → Shuffle → Reduce end to end | | |
| Combiner + Zero Reducer + Input Splits | | |
| YARN: ResourceManager + NodeManager + AM + Container | | |
| YARN job submission flow step by step | | |
| Linux + HDFS CLI commands | | |
| SQL: SELECT · WHERE · GROUP BY · HAVING | | |
| SQL: JOINs (INNER, LEFT, RIGHT) | | |
| SQL: Subqueries + CASE WHEN + NULL | | |
| SQL: Window Functions (ROW_NUMBER, LAG, SUM OVER) | | |
| SQL: CTEs + String/Date functions | | |

**Ready for Month 2 (Spark) when:**
- [ ] Day 30 score 7/10 or above
- [ ] SQL done on all 9 SQL days
- [ ] Mini project pushed to GitHub with README
- [ ] All videos `#26` through `#110` checked
- [ ] No topic rated below 3
- [ ] Can explain: generator → lazy evaluation → why Spark's `.filter()` doesn't run immediately

---

> **Send completed notebook each day. Tests on Day 10, Day 20, Day 30. No skipping.**
> **5 days done. 25 to go. Python is now properly spaced — YARN is still Day 26. The plan holds.**
