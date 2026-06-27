# Hands-On 4: Query Optimization – Indexes, EXPLAIN & the N+1 Problem

---

## 📖 Overview

This hands-on focuses on improving database performance using query optimization techniques. It covers query execution plans, indexing strategies, and identifying the N+1 query problem using SQL and Python.

---

## 🎯 Objectives

- Analyze query execution plans using `EXPLAIN`.
- Improve query performance by creating indexes.
- Compare query plans before and after indexing.
- Identify and resolve the N+1 query problem.
- Understand the importance of efficient database access.

---

## 🛠️ Technologies Used

- MySQL
- SQL
- Python
- MySQL Connector for Python
- MySQL Workbench
- Visual Studio Code

---

## 📂 Files

```text
HandsOn4/
├── HandsOn4.sql
├── n_plus_one.py
└── README.md
```

---

# Task 1 – Baseline Performance Analysis

## Description

Analyzed the execution plan of a SQL query before creating any indexes to understand how MySQL accesses the tables.

### Activities Performed

- Executed the query using `EXPLAIN`.
- Examined the query execution plan.
- Identified Full Table Scans.
- Documented the estimated rows examined.

### Learning Outcome

Learned how to analyze query execution plans and identify potential performance bottlenecks.

---

# Task 2 – Query Optimization Using Indexes

## Description

Created indexes to optimize query execution and compared the updated execution plan with the baseline.

### Activities Performed

- Created a B-Tree index on `students.enrollment_year`.
- Created a composite UNIQUE index on `enrollments(student_id, course_id)`.
- Created an index on `courses.course_code`.
- Re-executed `EXPLAIN` to compare query plans.
- Created an additional index to optimize searches for records with `NULL` grades.

### Learning Outcome

Learned how indexes improve query performance by reducing table scans and minimizing the number of rows examined.

---

# Task 3 – N+1 Query Problem

## Description

Implemented two Python programs to demonstrate the N+1 query problem and its optimized solution using SQL JOINs.

### Activities Performed

- Simulated the N+1 query problem using multiple SQL queries.
- Replaced multiple queries with a single JOIN query.
- Compared the number of database queries executed.
- Measured execution time using Python's `time` module.
- Documented the impact of the N+1 problem on large datasets.

### Learning Outcome

Learned how the N+1 query problem affects application performance and how JOIN queries eliminate unnecessary database round-trips.

---

## 📚 Key Concepts Learned

- Query Optimization
- EXPLAIN
- Query Execution Plans
- Full Table Scan
- Index Scan
- B-Tree Index
- Composite Index
- N+1 Query Problem
- SQL JOIN
- Database Performance

---

## ✅ Conclusion

This hands-on provided practical experience in analyzing SQL query execution plans, improving database performance using indexes, and optimizing application performance by eliminating the N+1 query problem through efficient JOIN queries.