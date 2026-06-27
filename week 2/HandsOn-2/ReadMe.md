# Hands-On 2: Writing SQL Queries – DML, Joins & Aggregations

---

## 📖 Overview

This hands-on focuses on performing database operations using SQL Data Manipulation Language (DML) and retrieving meaningful information using SQL queries. It covers CRUD operations, filtering, joins, aggregate functions, grouping, and data analysis on the Student Course Registration System database.

---

## 🎯 Objectives

- Perform CRUD operations using SQL.
- Retrieve data using filtering and sorting.
- Work with multiple tables using JOIN operations.
- Generate reports using aggregate functions.
- Analyze data using GROUP BY and HAVING clauses.

---

## 🛠️ Technologies Used

- PostgreSQL
- SQL
- pgAdmin 4
- Visual Studio Code

---

## 📂 Files

```text
HandsOn2/
├── HandsOn2.sql
└── README.md
```

---

# Task 1 – Data Manipulation (DML)

## Description

Performed basic database operations to insert, update, and delete records while maintaining data consistency.

### Activities Performed

- Inserted the given sample data into all tables.
- Added additional student records.
- Updated student grades.
- Deleted enrollment records with NULL grades.
- Verified the changes using SQL queries.

### Learning Outcome

Learned how to manipulate data using SQL DML statements such as INSERT, UPDATE, DELETE, and SELECT.

---

# Task 2 – Single Table Queries

## Description

Retrieved and filtered data from individual tables using SQL query clauses.

### Activities Performed

- Retrieved students enrolled in a specific year.
- Listed courses based on credits.
- Filtered professors using salary range.
- Used the LIKE operator for email filtering.
- Counted students by enrollment year.

### Learning Outcome

Learned how to filter, sort, and retrieve records efficiently using SQL.

---

# Task 3 – Multi-Table Joins

## Description

Combined data from multiple related tables using SQL JOIN operations.

### Activities Performed

- Joined Students and Departments.
- Joined Students, Courses, and Enrollments.
- Used LEFT JOIN to identify students without enrollments.
- Counted enrollments for each course.
- Displayed professors with their respective departments.

### Learning Outcome

Learned how to retrieve related information from multiple tables using JOIN operations.

---

# Task 4 – Aggregations and Grouping

## Description

Generated summary reports using SQL aggregate functions and grouping techniques.

### Activities Performed

- Counted enrollments per course.
- Calculated average professor salary by department.
- Filtered departments based on budget.
- Displayed grade distribution for a course.
- Used HAVING with GROUP BY for aggregated filtering.

### Learning Outcome

Learned how to summarize and analyze relational data using aggregate functions, GROUP BY, and HAVING clauses.

---

## 📚 Key Concepts Learned

- INSERT
- UPDATE
- DELETE
- SELECT
- WHERE
- ORDER BY
- LIKE
- INNER JOIN
- LEFT JOIN
- Aggregate Functions
- COUNT()
- SUM()
- AVG()
- MAX()
- GROUP BY
- HAVING

---

## ✅ Conclusion

This hands-on provided practical experience in manipulating and querying relational databases using SQL. It strengthened the understanding of DML operations, joins, filtering techniques, and data aggregation for generating meaningful reports.

---

## 👨‍💻 Author

**Ajay S**

B.E. Computer Science and Engineering

Easwari Engineering College

Digital Nurture 5.0 – Python Full Stack Engineer Track