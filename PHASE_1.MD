# 🎯 Big Data Engineer — 15-Day Study Plan
### 👤 Learner: Chandra Sekhar Sahu | Titan Company Limited
### 📅 Plan Start: May 3, 2026 | ✅ Completed Till: Abstraction in Python

---

> ### 📌 HOW TO USE THIS PLAN
> - **☐** = Not started | **☑** = Done
> - **⏱** = Video duration
> - **🧠 Concept Check** = Questions you must answer *without* looking at the video again
> - **💻 Hands-On Task** = Code you must write from scratch in VS Code / Jupyter
> - **📝 Quick Notes Rule** = After every video, write 3 bullet points in your own words
> - **🔁 Revision Slot** = 20 min at end of each day — re-read your notes from that day

---

---

## 📅 DAY 1 — Sunday, May 3, 2026
### 🎯 Theme: Advanced OOP in Python — The Hidden Power Tools

---

### 📺 Videos to Watch

| ☐ | Topic | Duration |
|---|---|---|
| ☐ | Magic Methods In Python | ⏱ 8 min |
| ☐ | Custom Exception In Python | ⏱ 7 min |
| ☐ | Operator Overloading In Python | ⏱ 8 min |
| ☐ | Iterators In Python | ⏱ 6 min |
| ☐ | Generators In Python | ⏱ 11 min |

**Total Watch Time: ~40 min**

---

### 🧠 Concept Check (Answer these BEFORE moving to Day 2)

1. What is `__init__`, `__str__`, `__repr__`, `__len__` and when would you use each?
2. What is the difference between `__eq__` and `is` in Python?
3. You have a class `BankAccount`. How would you use operator overloading to add two accounts using `+`?
4. What is the difference between an Iterator and an Iterable? Which one implements `__next__`?
5. Why are Generators memory-efficient compared to returning a full list?
6. Write a custom exception called `InsufficientFundsError` — when should it be raised?

---

### 💻 Hands-On Tasks (Open VS Code — actually type, never copy-paste)

**Task 1 — Magic Methods:**
```python
# Create a class 'Product' with name, price, quantity
# Implement: __str__, __repr__, __add__ (adds price), __lt__ (compare prices)
# Test: print(p1), print(p1 + p2), print(p1 < p2)
```

**Task 2 — Custom Exception:**
```python
# Create: InsufficientFundsError, InvalidAccountError
# Build a BankAccount class that raises these when needed
# Test both exceptions with try/except blocks
```

**Task 3 — Iterator from Scratch:**
```python
# Build a class 'CountDown' that counts down from N to 0
# Implement __iter__ and __next__ manually (no range(), no reversed())
# Use it in a for loop
```

**Task 4 — Generator:**
```python
# Write a generator function that yields Fibonacci numbers infinitely
# Use next() 10 times to get first 10 Fibonacci numbers
# Compare memory usage concept: generator vs list
```

---

### 📝 End of Day Checklist
- ☐ Wrote 3-bullet summary for each video in a notebook
- ☐ All 4 coding tasks completed and saved in `day01_advanced_oop.py`
- ☐ Ran all code — no errors
- ☐ 20-min revision of today's notes done

---

---

## 📅 DAY 2 — Monday, May 4, 2026
### 🎯 Theme: Decorators + NumPy — Python Gets Serious

---

### 📺 Videos to Watch

| ☐ | Topic | Duration |
|---|---|---|
| ☐ | Decorators In Python | ⏱ 21 min |
| ☐ | Working With Numpy In Python | ⏱ 28 min |

**Total Watch Time: ~49 min**

---

### 🧠 Concept Check

1. What problem do Decorators solve? Explain using logging as an example.
2. What is `*args` and `**kwargs` and why do wrappers inside decorators need them?
3. What is `@functools.wraps` and why should you always use it?
4. What is the difference between a Python list and a NumPy array? Name 3 differences.
5. What does `axis=0` mean vs `axis=1` in NumPy operations?
6. What is broadcasting in NumPy? Give a real example.

---

### 💻 Hands-On Tasks

**Task 1 — Decorator:**
```python
# Write a decorator @timer that prints how long a function takes to run
# Write a decorator @logger that prints function name + arguments every time it's called
# Stack both decorators on a function called process_data(n)
```

**Task 2 — Decorator for validation:**
```python
# Write @validate_positive that raises ValueError if any argument is negative
# Apply it to a function calculate_area(length, width)
```

**Task 3 — NumPy Essentials (build these from scratch):**
```python
import numpy as np

# 1. Create a 5x5 matrix of random integers between 1 and 100
# 2. Find: mean, median, std deviation of each row
# 3. Replace all values > 50 with 0 (boolean masking)
# 4. Reshape it to (25,) then back to (5,5)
# 5. Stack two 5x5 matrices vertically and horizontally
# 6. Perform dot product of two 3x3 matrices
```

---

### 📝 End of Day Checklist
- ☐ Decorator tasks done — both decorators work and are stackable
- ☐ NumPy code runs correctly
- ☐ Saved as `day02_decorators_numpy.py`
- ☐ 20-min revision done

---

---

## 📅 DAY 3 — Tuesday, May 5, 2026
### 🎯 Theme: Pandas — The Data Engine You'll Use Every Day

---

### 📺 Videos to Watch

| ☐ | Topic | Duration |
|---|---|---|
| ☐ | Pandas DataFrame And Series | ⏱ 29 min |
| ☐ | Data Manipulation And Analysis | ⏱ 24 min |
| ☐ | Data Source Reading | ⏱ 15 min |

**Total Watch Time: ~68 min**

---

### 🧠 Concept Check

1. What is the difference between a Pandas Series and a DataFrame?
2. What is the difference between `.loc[]` and `.iloc[]`? When would each fail?
3. What does `groupby()` actually return before you call an aggregation on it?
4. What is the difference between `merge()` and `join()` in Pandas?
5. What are the 4 types of joins in Pandas merge? Give a use case for each.
6. What happens to NaN values during a groupby aggregation?

---

### 💻 Hands-On Tasks

**Task 1 — Build a mini sales dataset:**
```python
import pandas as pd
import numpy as np

# Create a DataFrame with 50 rows:
# Columns: order_id, customer_name, product, category, quantity, price, date, region
# Use np.random for numeric columns
# Add some NaN values intentionally in 'price' column
```

**Task 2 — Manipulate it:**
```python
# 1. Filter: all orders from 'South' region with quantity > 5
# 2. GroupBy category — find total revenue (quantity * price) per category
# 3. Sort by revenue descending
# 4. Find top 3 products by average price
# 5. Fill NaN prices with the median price of that category
```

**Task 3 — Merge two DataFrames:**
```python
# Create a second DataFrame: customer_id, customer_name, loyalty_tier
# Merge with sales DataFrame on customer_name
# Find average order value per loyalty tier
```

**Task 4 — Read from CSV:**
```python
# Save your DataFrame to CSV: df.to_csv('sales_data.csv', index=False)
# Read it back with: pd.read_csv()
# Read only first 10 rows, only specific columns — practice read parameters
```

---

### 📝 End of Day Checklist
- ☐ Mini dataset created, manipulated, merged
- ☐ Read/write CSV works
- ☐ Saved as `day03_pandas.py`
- ☐ 20-min revision done

---

---

## 📅 DAY 4 — Wednesday, May 6, 2026
### 🎯 Theme: Python SQLite + Logging — Production-Ready Python

---

### 📺 Videos to Watch

| ☐ | Topic | Duration |
|---|---|---|
| ☐ | Python With SQLite | ⏱ 17 min |
| ☐ | Logging In Python | ⏱ 14 min |
| ☐ | Logging With Multiple Loggers | ⏱ 4 min |
| ☐ | Logging In a Real World Example | ⏱ 7 min |
| ☐ | Python Outro | ⏱ 1 min |

**Total Watch Time: ~43 min**

---

### 🧠 Concept Check

1. What are the 5 logging levels in Python and when should each be used?
2. What is the difference between a Logger, Handler, and Formatter in Python logging?
3. Why is `logging` better than `print()` for production code?
4. What is SQLite? How is it different from MySQL?
5. What does a cursor object do in SQLite — why do you need it?

---

### 💻 Hands-On Tasks

**Task 1 — SQLite Mini Project:**
```python
import sqlite3

# 1. Create a database called titan_store.db
# 2. Create tables: products(id, name, category, price) and orders(id, product_id, qty, date)
# 3. Insert 10 products, 20 orders using executemany()
# 4. Query: total revenue per category
# 5. Update price of one product
# 6. Delete all orders older than a specific date
```

**Task 2 — Logging Pipeline:**
```python
import logging

# Build a logging setup with:
# - FileHandler writing to app.log
# - StreamHandler writing to console
# - Log level: DEBUG for file, WARNING for console
# - Format: [timestamp] [level] [module_name] — message

# Create 2 separate loggers: db_logger and api_logger
# Log different messages from each
```

**Task 3 — Combine Both:**
```python
# Wrap your SQLite operations from Task 1 with proper logging
# Log every INSERT, UPDATE, DELETE operation
# Log exceptions with logger.exception() inside try/except
```

---

### 🏆 PYTHON MODULE COMPLETE — Self-Assessment
Answer these 5 questions to test your Python readiness for Big Data:
1. Can you explain generators and why Spark uses lazy evaluation (same concept)?
2. Can you write a decorator that retries a function 3 times on failure?
3. Can you read a CSV into Pandas, clean NaN values, group and aggregate?
4. Can you set up a proper logging system in a multi-module Python project?
5. Can you query a SQLite database from Python using parameterized queries?

If you answered YES to all 5 — you are Big Data Python ready. 🎉

---

### 📝 End of Day Checklist
- ☐ SQLite tasks done and data persisted in .db file
- ☐ Logging setup with two loggers works
- ☐ Saved as `day04_sqlite_logging.py`
- ☐ 20-min revision done

---

---

## 📅 DAY 5 — Thursday, May 7, 2026
### 🎯 Theme: Big Data Foundations — Why Does This World Exist?

---

### 📺 Videos to Watch

| ☐ | Topic | Duration |
|---|---|---|
| ☐ | SQL Section Intro | ⏱ 1 min |
| ☐ | Basic To Intermediate MySQL Tutorials (Section Intro) | ⏱ 1 min |
| ☐ | What is Big Data — A Practical Example | ⏱ 18 min |
| ☐ | 5 V's of Big Data | ⏱ 22 min |
| ☐ | Big Data and Distributed Systems | ⏱ 18 min |

**Total Watch Time: ~60 min**

---

### 🧠 Concept Check

1. Define Big Data in your own words. What makes data "big"?
2. Explain each of the 5 V's with a real-world Titan Company example for each.
3. Why can't a single powerful machine solve Big Data problems?
4. What is horizontal vs vertical scaling? Which one Big Data uses and why?
5. What is a distributed system? What are its main challenges?

---

### 💻 Hands-On Tasks

**Task 1 — 5 V's in Real Life (Write in markdown or notebook):**
```
Map the 5 V's to a real Titan scenario:
- Volume: How much data does Titan's retail/e-commerce generate daily?
- Velocity: How fast does watch inventory data change?
- Variety: What types of data does Titan deal with (POS, web, social, sensor)?
- Veracity: What data quality issues might Titan face?
- Value: What business decisions can Titan make from this data?
```

**Task 2 — Distributed vs Centralized (Draw or write):**
```
Sketch (on paper or in markdown) the difference between:
1. Storing 1TB of sales data on ONE powerful server
2. Storing 1TB of sales data across 10 nodes in a cluster
Label: What happens if one machine fails in each scenario?
```

**Task 3 — SQL Revision (30 min):**
```sql
-- Practice these without looking at notes:
-- 1. Create a sales table with proper constraints
-- 2. Write a JOIN query across 3 tables
-- 3. Write a subquery using EXISTS
-- 4. Use window functions: ROW_NUMBER(), RANK(), LAG()
-- 5. Write a CTE (Common Table Expression)
```

---

### 📝 End of Day Checklist
- ☐ 5 V's mapped to Titan context — written down
- ☐ SQL revision queries executed in MySQL Workbench
- ☐ 20-min revision done

---

---

## 📅 DAY 6 — Friday, May 8, 2026
### 🎯 Theme: Big Data Architecture — Making Smart Design Choices

---

### 📺 Videos to Watch

| ☐ | Topic | Duration |
|---|---|---|
| ☐ | Designing a Good Big Data System | ⏱ 11 min |
| ☐ | On-Premise Infra vs Cloud Solutions | ⏱ 20 min |
| ☐ | Database vs Data Warehouse vs Data Lake | ⏱ 29 min |
| ☐ | ETL vs ELT | ⏱ 22 min |
| ☐ | What Does a Data Engineer Do & Where Big Data Fits In | ⏱ 18 min |

**Total Watch Time: ~100 min**

---

### 🧠 Concept Check

1. What are the key properties of a well-designed Big Data system?
2. Name 3 scenarios where On-Premise is better than Cloud, and 3 where Cloud wins.
3. Fill this table in your own words:

| | Database | Data Warehouse | Data Lake |
|---|---|---|---|
| Data Type | | | |
| Schema | | | |
| Users | | | |
| Query Speed | | | |
| Example Tool | | | |

4. What is the key difference between ETL and ELT?
5. In which scenario would you choose ELT over ETL?
6. List 5 real daily tasks a Data Engineer does.

---

### 💻 Hands-On Tasks

**Task 1 — Architecture Decision (Scenario Writing):**
```
Titan Company wants to analyze:
- 5 years of POS transaction data (5TB)
- Real-time inventory updates from 500 stores
- Customer browsing behavior from Titan's website
- Unstructured data: customer reviews, images

For each data type, decide:
1. Where should it be stored? (DB / DW / Data Lake)
2. What processing model? (ETL or ELT)
3. On-prem or Cloud?
Write your reasoning. There's no single right answer — justify yours.
```

**Task 2 — ETL Mini Pipeline in Python:**
```python
# Simulate an ETL pipeline:
# E — Extract: Read data from a CSV file (sales_data.csv from Day 3)
# T — Transform: Clean NaN values, add revenue column (qty * price), filter valid records
# L — Load: Write cleaned data into a new SQLite table (use titan_store.db from Day 4)
# Add proper logging at each step
```

---

### 📝 End of Day Checklist
- ☐ Architecture comparison table filled
- ☐ ETL Python pipeline working end-to-end
- ☐ Scenario written for Titan data architecture
- ☐ 20-min revision done

---

---

## 📅 DAY 7 — Saturday, May 9, 2026
### 🎯 Theme: Hadoop — The Original Big Data Giant

---

### 📺 Videos to Watch

| ☐ | Topic | Duration |
|---|---|---|
| ☐ | Section Intro | ⏱ 2 min |
| ☐ | Introduction To Hadoop | ⏱ 5 min |
| ☐ | Properties of Hadoop | ⏱ 9 min |
| ☐ | Hadoop Ecosystem — Main Components | ⏱ 9 min |
| ☐ | Hadoop Ecosystem — Components (detailed) | ⏱ 29 min |

**Total Watch Time: ~54 min**

---

### 🧠 Concept Check

1. What 4 key properties make Hadoop powerful for Big Data?
2. Draw the Hadoop Ecosystem from memory. Label at least 8 components.
3. What is the role of each: HDFS, YARN, MapReduce in Hadoop?
4. What is the difference between Hadoop 1.x and Hadoop 2.x (YARN's role)?
5. Name 3 tools in the Hadoop ecosystem and what specific problem each solves.

---

### 💻 Hands-On Tasks

**Task 1 — Ecosystem Mind Map (pen & paper or draw.io):**
```
Draw the Hadoop ecosystem with these categories:
- Storage Layer (HDFS, HBase, etc.)
- Processing Layer (MapReduce, Spark, etc.)
- Resource Management (YARN)
- Ingestion (Kafka, Flume, Sqoop)
- Query (Hive, Pig, Impala)
- Coordination (ZooKeeper)
Connect them with arrows showing data flow.
```

**Task 2 — Research Task:**
```
Answer in your notes (use web research if needed):
1. Which Hadoop ecosystem tools are still heavily used in 2025?
2. Which tools have been replaced by modern alternatives?
3. Where does Spark fit vs MapReduce — are they replacements or complements?
```

**Task 3 — Reflection:**
```
Write 5 sentences answering:
"If I were designing Titan's Big Data platform today,
which Hadoop ecosystem components would I use and which would I skip?"
```

---

### 📝 End of Day Checklist
- ☐ Ecosystem mind map drawn
- ☐ Research task answered
- ☐ Reflection written
- ☐ 20-min revision done

---

---

## 📅 DAY 8 — Sunday, May 10, 2026
### 🎯 Theme: HDFS — How Data Actually Lives in a Cluster

---

### 📺 Videos to Watch

| ☐ | Topic | Duration |
|---|---|---|
| ☐ | Intro to HDFS and Common Terminology | ⏱ 22 min |
| ☐ | Why HDFS | ⏱ 4 min |
| ☐ | HDFS Architecture | ⏱ 15 min |
| ☐ | Blocks In HDFS | ⏱ 12 min |
| ☐ | Replication Factor in HDFS | ⏱ 9 min |

**Total Watch Time: ~62 min**

---

### 🧠 Concept Check

1. What is the default block size in HDFS? Why is it so large compared to traditional file systems?
2. Explain the NameNode vs DataNode roles in a single sentence each.
3. If you store a 400MB file with a 128MB block size and replication factor 3, how many total block copies exist across the cluster?
4. What is metadata in HDFS? Where is it stored?
5. Why does HDFS follow "write once, read many" — what design decisions enforce this?
6. What happens when replication factor = 1 and a DataNode dies?

---

### 💻 Hands-On Tasks

**Task 1 — Block Calculation (Math Practice):**
```
Given:
- File size: 1.5 GB
- Block size: 128 MB
- Replication factor: 3

Calculate:
1. Number of blocks for this file
2. Total storage used across the cluster
3. If you have 5 DataNodes, how are blocks distributed?
```

**Task 2 — Architecture Diagram:**
```
Draw HDFS architecture with:
- 1 NameNode (label what it stores: metadata, namespace, block mapping)
- 4 DataNodes (show blocks distributed across them)
- Client reading a file (show the read flow step by step)
- Replication factor = 2 (show duplicate blocks)
```

**Task 3 — Comparison Table:**
```
Fill in:
| Property | Traditional Filesystem | HDFS |
|---|---|---|
| Block Size | 4KB | ? |
| Designed For | Random access | ? |
| Hardware | Expensive | ? |
| Fault Tolerance | RAID | ? |
| Best For | Small files | ? |
```

---

### 📝 End of Day Checklist
- ☐ Block calculation done correctly
- ☐ Architecture diagram drawn with labels
- ☐ Comparison table filled
- ☐ 20-min revision done

---

---

## 📅 DAY 9 — Monday, May 11, 2026
### 🎯 Theme: HDFS Fault Tolerance — What Happens When Things Break

---

### 📺 Videos to Watch

| ☐ | Topic | Duration |
|---|---|---|
| ☐ | Rack Awareness in HDFS | ⏱ 7 min |
| ☐ | Node Failure | ⏱ 0 min (quick overview) |
| ☐ | Data Node Failure — Temporary | ⏱ 11 min |
| ☐ | Data Node Failure — Permanent | ⏱ 14 min |
| ☐ | Secondary Name Node | ⏱ 17 min |

**Total Watch Time: ~49 min**

---

### 🧠 Concept Check

1. What is Rack Awareness? How does it improve fault tolerance in HDFS?
2. With replication factor 3, how does HDFS distribute replicas across racks?
3. What is the difference between temporary and permanent DataNode failure in terms of HDFS response?
4. What does the Secondary NameNode actually do? (Most people get this wrong — it does NOT replace the NameNode on failure)
5. What are FSImage and EditLog? Why does HDFS need both?
6. What problem does the Secondary NameNode solve?

---

### 💻 Hands-On Tasks

**Task 1 — Failure Scenario Analysis (write answers):**
```
Scenario A: You have 3 racks, 2 nodes per rack, RF=3
A full rack goes down. Which blocks are lost? Which are safe?

Scenario B: NameNode goes down (no HA setup).
What happens to reads? What happens to writes? 
How do you recover?

Scenario C: Secondary NameNode goes down.
What is the immediate impact on the cluster?
```

**Task 2 — FSImage + EditLog Diagram:**
```
Draw the checkpoint process:
1. NameNode maintains: FSImage (snapshot) + EditLog (changes)
2. Secondary NameNode merges them periodically
3. Show what happens to EditLog size over time without checkpointing
4. Show why a large EditLog causes slow NameNode restarts
```

**Task 3 — Quick Revision Quiz (write answers from memory):**
```
1. Default replication factor = ?
2. Default block size = ?
3. Where is metadata stored = ?
4. Secondary NameNode replaces NameNode on failure: True / False?
5. Rack Awareness places all 3 replicas on different racks: True / False?
```

---

### 📝 End of Day Checklist
- ☐ All 3 failure scenarios analyzed
- ☐ FSImage + EditLog diagram drawn
- ☐ Quick quiz answered (check against your notes)
- ☐ 20-min revision done

---

---

## 📅 DAY 10 — Tuesday, May 12, 2026
### 🎯 Theme: HDFS High Availability — Making HDFS Production-Ready

---

### 📺 Videos to Watch

| ☐ | Topic | Duration |
|---|---|---|
| ☐ | Standby Name Node | ⏱ 10 min |
| ☐ | Hadoop HA Architecture | ⏱ 20 min |
| ☐ | Data Write in HDFS | ⏱ 22 min |
| ☐ | Read Request in HDFS | ⏱ 10 min |

**Total Watch Time: ~62 min**

---

### 🧠 Concept Check

1. What is the difference between Secondary NameNode and Standby NameNode? (Critical distinction)
2. What is the role of ZooKeeper in Hadoop HA?
3. What is a "split-brain" scenario in HA? How does HDFS prevent it?
4. Walk through the HDFS write pipeline step by step (client → NameNode → DataNodes → acknowledgment)
5. Walk through the HDFS read process step by step
6. What is a "pipeline" in HDFS write? Why does HDFS use it instead of writing to all nodes simultaneously?

---

### 💻 Hands-On Tasks

**Task 1 — HA Architecture Diagram:**
```
Draw Hadoop HA setup with:
- Active NameNode
- Standby NameNode
- JournalNodes (shared edit log) — minimum 3
- ZooKeeper ensemble
- DataNodes
Show: What happens step by step when Active NameNode fails
```

**Task 2 — Write Pipeline Trace:**
```
Trace a WRITE operation for a 300MB file:
- Block size = 128 MB → how many blocks?
- RF = 3 → how many DataNodes involved per block?
- Draw packet flow: Client → DN1 → DN2 → DN3 → ACK back
- What happens if DN2 fails mid-write?
```

**Task 3 — Read Trace:**
```
Trace a READ operation:
- Client contacts NameNode → gets block locations
- Client picks "closest" DataNode (rack awareness)
- What happens if the closest DataNode is busy / down?
- What is checksumming in HDFS read?
```

---

### 📝 End of Day Checklist
- ☐ HA diagram drawn with ZooKeeper + JournalNodes
- ☐ Write pipeline traced for a 300MB file
- ☐ Read trace completed with failure scenario
- ☐ 20-min revision done

---

---

## 📅 DAY 11 — Wednesday, May 13, 2026
### 🎯 Theme: GCP Setup + Live Hadoop Cluster — Hands Get Dirty! 🖥️

---

### 📺 Videos to Watch

| ☐ | Topic | Duration |
|---|---|---|
| ☐ | Create GCP Account | ⏱ 24 min |
| ☐ | GCP Hadoop Cluster Creation | ⏱ 29 min |
| ☐ | Exploring Our Hadoop Cluster | ⏱ 24 min |
| ☐ | GCP Cluster Best Practices | ⏱ 4 min |

**Total Watch Time: ~81 min**

---

### 🧠 Concept Check

1. What is Google Cloud Dataproc? How is it different from setting up Hadoop manually?
2. What are the node types in a Dataproc cluster (Master vs Worker)?
3. What is the cost implication of leaving a Dataproc cluster running? What best practice addresses this?
4. Where does HDFS data go when a Dataproc cluster is deleted?
5. What is GCS (Google Cloud Storage) and how does it relate to HDFS in cloud deployments?

---

### 💻 Hands-On Tasks

**Task 1 — Actually set up your GCP account and cluster (follow the video)**
```
Required actions:
☐ Create GCP free tier account
☐ Enable Dataproc API
☐ Create a single-node cluster (cheapest option for learning)
☐ SSH into the master node
☐ Run: hadoop version
☐ Run: hdfs dfsadmin -report
☐ Take a screenshot of your running cluster dashboard
```

**Task 2 — Explore the Cluster:**
```bash
# Run these commands on your cluster after SSH:
hadoop version
hdfs dfsadmin -report
yarn node -list
hdfs dfs -ls /
hdfs dfs -mkdir /user/chandra/test
hdfs dfs -ls /user/chandra/
```

**Task 3 — STOP the cluster when done**
```
⚠️ IMPORTANT: Stop/delete your cluster after every session.
GCP charges by the hour. A running cluster = burning free credits.
Best practice: Use startup/shutdown scripts or delete and recreate.
```

---

### 📝 End of Day Checklist
- ☐ GCP account created
- ☐ Dataproc cluster created and explored
- ☐ All bash commands run and output noted
- ☐ Cluster STOPPED after session
- ☐ 20-min revision done

---

---

## 📅 DAY 12 — Thursday, May 14, 2026
### 🎯 Theme: Linux Commands — Your Cluster's Native Language

---

### 📺 Videos to Watch

| ☐ | Topic | Duration |
|---|---|---|
| ☐ | Linux Commands — 1 | ⏱ 32 min |
| ☐ | Linux Commands — 2 | ⏱ 27 min |

**Total Watch Time: ~59 min**

---

### 🧠 Concept Check

1. What is the difference between absolute path and relative path in Linux?
2. What does `chmod 755` mean? Break down each digit.
3. What is the difference between `>` and `>>` in Linux?
4. What is piping (`|`) in Linux? Give 3 practical examples.
5. What is the difference between `grep`, `awk`, and `sed`?
6. How do you find all files larger than 100MB in a directory tree?

---

### 💻 Hands-On Tasks (Run on your GCP cluster terminal OR local Linux/WSL)

**Task 1 — File Navigation:**
```bash
# Practice these until they are muscle memory:
pwd
ls -la
cd /tmp && mkdir practice && cd practice
touch file1.txt file2.log file3.csv
ls -lh
cp file1.txt backup_file1.txt
mv file2.log logs/  # create logs dir first
rm file3.csv
```

**Task 2 — Text Processing:**
```bash
# Create a sample file with 100 lines:
seq 1 100 > numbers.txt
cat numbers.txt | head -20
cat numbers.txt | tail -10
grep "5" numbers.txt          # lines containing 5
grep "^5" numbers.txt         # lines starting with 5
wc -l numbers.txt             # count lines
```

**Task 3 — Process & Permission:**
```bash
ps aux | grep java            # find Java processes (Hadoop runs on Java)
top                           # live process monitor (q to quit)
df -h                         # disk space
free -h                       # memory usage
chmod 644 file1.txt
ls -la file1.txt              # verify permissions changed
```

**Task 4 — Pipes & Redirection:**
```bash
cat /etc/passwd | cut -d: -f1 | sort | head -10
ls -la | awk '{print $5, $9}'           # print size and filename
echo "hadoop learning" > note.txt
cat note.txt >> note.txt                # append
cat note.txt
```

---

### 📝 End of Day Checklist
- ☐ All Linux commands practiced in terminal
- ☐ Text processing commands understood
- ☐ Piping concepts practiced
- ☐ 20-min revision done

---

---

## 📅 DAY 13 — Friday, May 15, 2026
### 🎯 Theme: HDFS Commands — Speaking to Your Distributed Filesystem

---

### 📺 Videos to Watch

| ☐ | Topic | Duration |
|---|---|---|
| ☐ | HDFS Commands | ⏱ 30 min |
| ☐ | Hadoop Outro | ⏱ 2 min |

**Total Watch Time: ~32 min**

---

### 🧠 Concept Check

1. What is the difference between `hdfs dfs -ls` and Linux `ls`?
2. How do you copy a file FROM your local system TO HDFS?
3. How do you copy a file FROM HDFS TO your local system?
4. What command shows HDFS disk usage summary?
5. What is `hdfs dfsadmin -report` — what does it tell you?
6. Can you edit a file that's already on HDFS? Why or why not?

---

### 💻 Hands-On Tasks (on GCP Dataproc cluster)

**Task 1 — HDFS Basic Operations:**
```bash
# Navigate HDFS
hdfs dfs -ls /
hdfs dfs -ls /user/

# Create directories
hdfs dfs -mkdir /user/chandra
hdfs dfs -mkdir /user/chandra/data
hdfs dfs -mkdir /user/chandra/output

# Check
hdfs dfs -ls /user/chandra/
```

**Task 2 — Upload and Download:**
```bash
# Create a local file first
echo "Hello HDFS from Chandra" > local_test.txt
cat local_test.txt

# Upload to HDFS
hdfs dfs -put local_test.txt /user/chandra/data/
hdfs dfs -ls /user/chandra/data/

# Read directly from HDFS (without downloading)
hdfs dfs -cat /user/chandra/data/local_test.txt

# Download back to local
hdfs dfs -get /user/chandra/data/local_test.txt downloaded_test.txt
cat downloaded_test.txt
```

**Task 3 — Cluster Health:**
```bash
hdfs dfsadmin -report         # full cluster report
hdfs dfs -df -h               # HDFS disk usage
hdfs dfs -du -h /user/        # size of each user directory
hdfs fsck / -files -blocks    # check filesystem health
```

**Task 4 — Upload Real Data:**
```bash
# Download a public dataset to your cluster
wget https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

# Upload to HDFS
hdfs dfs -put titanic.csv /user/chandra/data/
hdfs dfs -ls /user/chandra/data/
hdfs dfs -cat /user/chandra/data/titanic.csv | head -5
```

---

### 🏆 HADOOP MODULE COMPLETE — Self Assessment
Answer from memory:
1. HDFS default block size = ?
2. What does NameNode store?
3. Command to upload file to HDFS?
4. Command to check HDFS cluster health?
5. What is the difference between Secondary NameNode and Standby NameNode?
6. In Hadoop HA, what prevents split-brain?

---

### 📝 End of Day Checklist
- ☐ All HDFS commands practiced on live cluster
- ☐ Real data uploaded to HDFS
- ☐ Self-assessment answered
- ☐ Cluster STOPPED
- ☐ 20-min revision done

---

---

## 📅 DAY 14 — Saturday, May 16, 2026
### 🎯 Theme: MapReduce Theory — Divide, Conquer, and Combine

---

### 📺 Videos to Watch

| ☐ | Topic | Duration |
|---|---|---|
| ☐ | Map Reduce Intro | ⏱ 1 min |
| ☐ | Intro To Distributed Processing | ⏱ 11 min |
| ☐ | Map Reduce Introduction | ⏱ 17 min |
| ☐ | Map Reduce & Cluster | ⏱ 12 min |

**Total Watch Time: ~41 min**

---

### 🧠 Concept Check

1. Explain MapReduce using a non-technical real-world analogy (not word count).
2. What are the 3 phases of MapReduce? What happens in each?
3. What is a key-value pair? Give 3 examples of naturally key-value structured data.
4. What is the Shuffle & Sort phase — why is it often the slowest part?
5. What does it mean that MapReduce moves "computation to data"?
6. How does MapReduce handle a DataNode failure mid-job?

---

### 💻 Hands-On Tasks

**Task 1 — MapReduce Mental Simulation (on paper first):**
```
Input dataset (sales transactions):
TXN001, Electronics, 5000
TXN002, Clothing, 1200
TXN003, Electronics, 3400
TXN004, Watches, 8900
TXN005, Clothing, 2300
TXN006, Watches, 15000
TXN007, Electronics, 6700

MapReduce Goal: Total revenue per category

Step 1 — MAP phase (what does each mapper emit?):
Write the key-value pairs emitted by the mapper for each line.

Step 2 — SHUFFLE & SORT (group by key):
Show the grouped output after shuffle.

Step 3 — REDUCE phase (what does each reducer produce?):
Write the final output.
```

**Task 2 — Python Simulation of MapReduce:**
```python
from collections import defaultdict

# Raw data
transactions = [
    ("TXN001", "Electronics", 5000),
    ("TXN002", "Clothing", 1200),
    ("TXN003", "Electronics", 3400),
    ("TXN004", "Watches", 8900),
    ("TXN005", "Clothing", 2300),
    ("TXN006", "Watches", 15000),
    ("TXN007", "Electronics", 6700),
]

# MAP function — your job: implement this
def mapper(transaction):
    txn_id, category, amount = transaction
    # emit (key, value) — what should key and value be?
    return (category, amount)

# SHUFFLE & SORT — framework does this
def shuffle_and_sort(mapped_pairs):
    grouped = defaultdict(list)
    for key, value in mapped_pairs:
        grouped[key].append(value)
    return dict(grouped)

# REDUCE function — your job: implement this
def reducer(key, values):
    # aggregate the values for this key
    return (key, sum(values))

# Run the full pipeline
mapped = [mapper(t) for t in transactions]
shuffled = shuffle_and_sort(mapped)
result = [reducer(k, v) for k, v in shuffled.items()]

print("Final Result:", result)
```

**Task 3 — Extend it:**
```python
# Modify the above to also compute:
# 1. Count of transactions per category
# 2. Average transaction value per category
# 3. Maximum transaction per category
# (All in one MapReduce pass — one mapper, one reducer per metric)
```

---

### 📝 End of Day Checklist
- ☐ Mental simulation on paper done for 3 phases
- ☐ Python MapReduce simulation running correctly
- ☐ Extended to compute count, average, max
- ☐ 20-min revision done

---

---

## 📅 DAY 15 — Sunday, May 17, 2026
### 🎯 Theme: MapReduce Practicals — Running Real Jobs on a Cluster

---

### 📺 Videos to Watch

| ☐ | Topic | Duration |
|---|---|---|
| ☐ | Map Reduce Practical Part 1 | ⏱ 17 min |
| ☐ | MR Example Part 2 | ⏱ 22 min |

**Total Watch Time: ~39 min**

---

### 🧠 Concept Check

1. What is the Hadoop streaming API and why is it useful for Python-based MapReduce?
2. What is the difference between the mapper and reducer scripts in Hadoop streaming?
3. How does Hadoop pass data between mapper and reducer (via stdin/stdout)?
4. What does `yarn jar hadoop-streaming.jar` do?

---

### 💻 Hands-On Tasks (on GCP Dataproc cluster)

**Task 1 — Word Count (Classic, but essential):**
```python
# mapper.py
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print(f"{word.lower()}\t1")
```

```python
# reducer.py
import sys
from collections import defaultdict

word_count = defaultdict(int)

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    word_count[word] += int(count)

for word, count in sorted(word_count.items()):
    print(f"{word}\t{count}")
```

```bash
# Test locally FIRST (always test locally before cluster):
echo "hello world hello hadoop hello" | python3 mapper.py | sort | python3 reducer.py

# Upload mapper and reducer to cluster
# Create an input file on HDFS and run:
hdfs dfs -mkdir /user/chandra/wordcount_input
echo "the quick brown fox jumps over the lazy dog the fox" > input.txt
hdfs dfs -put input.txt /user/chandra/wordcount_input/

# Run on Hadoop cluster using streaming:
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
  -input /user/chandra/wordcount_input/ \
  -output /user/chandra/wordcount_output/ \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py

# Check results:
hdfs dfs -cat /user/chandra/wordcount_output/part-00000
```

**Task 2 — Custom MapReduce (Sales Data):**
```python
# Use the titanic.csv you uploaded on Day 13
# Goal: Count passengers per class (Pclass column)

# mapper_titanic.py — parse CSV, emit (Pclass, 1)
# reducer_titanic.py — sum counts per Pclass

# Run on cluster and verify output
```

**Task 3 — 15-Day Revision (30 min):**
```
Look at your notes from Days 1-15 and answer:
1. What is the Python concept that makes Spark's lazy evaluation possible? (Day 1-2)
2. What is the difference between Data Lake and Data Warehouse? (Day 6)
3. How many block copies exist for a 500MB file with RF=3 and 128MB blocks? (Day 8)
4. What is the role of ZooKeeper in Hadoop HA? (Day 10)
5. What Linux command checks HDFS cluster health? (Day 13)
6. What are the 3 phases of MapReduce? (Day 14)
```

---

### 🏆 15-DAY MILESTONE CHECKPOINT

**You have now completed:**
- ✅ Advanced Python OOP (Magic Methods, Iterators, Generators, Decorators)
- ✅ NumPy and Pandas (Data manipulation powerhouse)
- ✅ Python with SQLite and Logging
- ✅ Big Data Foundations (5 V's, Architecture, ETL vs ELT)
- ✅ Hadoop Ecosystem + HDFS Architecture
- ✅ HDFS Fault Tolerance + HA Architecture
- ✅ GCP Dataproc Setup + Linux + HDFS Commands
- ✅ MapReduce Theory + Practicals

**What's Next (Days 16–30):**
- MapReduce Advanced Practicals (Reducers, Combiners, Log Files)
- YARN Architecture
- Higher Order Functions Bridge
- Spark Introduction → RDD → DataFrames

---

### 📝 End of Day Checklist
- ☐ Word count MapReduce runs on cluster successfully
- ☐ Custom Titanic MapReduce runs successfully
- ☐ 15-day revision quiz answered
- ☐ Cluster STOPPED
- ☐ Proud of yourself (mandatory ✅)

---

---

## 📌 QUICK REFERENCE — Study Rules

### ⏰ Daily Time Budget
| Activity | Time |
|---|---|
| Video watching | 45–90 min |
| Hands-on coding | 60–90 min |
| Concept check (write answers) | 20 min |
| End-of-day revision | 20 min |
| **Total per day** | **~3 hours** |

### 🛠️ Tools You Need Active
| Tool | Purpose |
|---|---|
| VS Code | Python coding (Days 1–6) |
| MySQL Workbench | SQL practice |
| GCP Dataproc | Hadoop/HDFS/MR (Days 11–15) |
| Jupyter Notebook (optional) | Pandas/NumPy exploration |
| draw.io or pen+paper | Architecture diagrams |

### 🔑 The Golden Rule
> **For every 1 hour of video, spend 1.5 hours practicing.**
> Understanding a concept ≠ being able to use it.
> Writing code from scratch = the only real test.

---

*Study Plan generated on May 3, 2026 | TitanAI for Titan Company Limited*
*Next 15 days (Days 16–30) covering MapReduce Advanced + YARN + Spark — request when ready*

