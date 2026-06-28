# Hands-On 6: ORM Integration – SQLAlchemy

---

## 📖 Overview

This hands-on focuses on integrating Object Relational Mapping (ORM) using SQLAlchemy with a MySQL database. It demonstrates how to define ORM models, perform CRUD operations, and optimize database queries by resolving the N+1 query problem using eager loading.

---

## 🎯 Objectives

- Connect SQLAlchemy to a MySQL database.
- Define ORM models and relationships.
- Perform CRUD operations using SQLAlchemy sessions.
- Implement eager loading using `joinedload()`.
- Understand how ORM improves database interaction.

---

## 🛠️ Technologies Used

- Python
- SQLAlchemy
- MySQL
- PyMySQL
- Visual Studio Code

---

## 📂 Files

```text
HandsOn6/
├── models.py
├── crud.py
├── requirements.txt
└── README.md
```

---

# Task 1 – Define ORM Models

## Description

Created SQLAlchemy ORM models that mirror the relational database schema and established relationships between entities.

### Activities Performed

- Configured SQLAlchemy engine for MySQL.
- Created ORM model classes:
  - Department
  - Student
  - Course
  - Enrollment
  - Professor
- Defined one-to-many and many-to-one relationships.
- Generated database tables using `Base.metadata.create_all()`.

### Learning Outcome

Learned how SQLAlchemy maps Python classes to relational database tables and automatically creates database schemas.

---

# Task 2 – CRUD Operations using SQLAlchemy

## Description

Performed Create, Read, Update, and Delete operations using SQLAlchemy's Session API instead of writing raw SQL queries.

### Activities Performed

- Inserted departments, students, courses, and enrollments.
- Retrieved students belonging to the Computer Science department.
- Displayed enrollment details with related student and course information.
- Updated a student's enrollment year.
- Deleted an enrollment record.
- Verified all database operations using SQLAlchemy sessions.

### Learning Outcome

Learned how ORM simplifies database operations by representing records as Python objects.

---

# Task 3 – Eager Loading to Fix N+1 Problem

## Description

Demonstrated the N+1 Query Problem and optimized database access using SQLAlchemy's `joinedload()`.

### Activities Performed

- Observed multiple SQL queries generated with lazy loading.
- Used `joinedload()` to eagerly load related student and course data.
- Compared query execution before and after optimization.
- Verified reduced SQL queries using `echo=True`.

### Learning Outcome

Learned how eager loading improves application performance by eliminating unnecessary database queries.

---

## 📚 Key Concepts Learned

- SQLAlchemy ORM
- Declarative Models
- Relationships
- Session Management
- CRUD Operations
- Lazy Loading
- Eager Loading
- joinedload()
- N+1 Query Problem
- Query Optimization

---

## ✅ Conclusion

This hands-on provided practical experience in using SQLAlchemy ORM to interact with a relational database through Python objects. It also demonstrated how eager loading with `joinedload()` optimizes database performance by eliminating the N+1 query problem.