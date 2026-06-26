# Hands-On 1: Schema Design & Core SQL – DDL and Normalisation

## 📖 Overview

This hands-on focuses on designing a relational database for a **Student Course Registration System** using PostgreSQL. The exercise covers database schema creation, normalization principles, referential integrity, and schema modification using SQL Data Definition Language (DDL) commands.

---

## 🎯 Objectives

- Design a normalized relational database.
- Create tables with appropriate constraints.
- Establish relationships using foreign keys.
- Verify database normalization (1NF, 2NF, 3NF).
- Modify the schema using `ALTER TABLE` statements.

---

## 🛠️ Technologies Used

- PostgreSQL
- SQL
- pgAdmin 4
- Visual Studio Code

---

## 📂 Files

```
HandsOn1/
├── hands_on_1.sql
└── README.md
```

---

# Task 1 – Create the Database Schema

### Description

In this task, the complete database schema for the **Student Course Registration System** was created. Five relational tables were designed based on the given requirements.

### Activities Performed

- Created the `departments` table.
- Created the `students` table.
- Created the `courses` table.
- Created the `enrollments` table.
- Created the `professors` table.
- Applied the following constraints:
  - Primary Key
  - Foreign Key
  - NOT NULL
  - UNIQUE

### Learning Outcome

Learned how to design a relational database and establish relationships between tables while maintaining referential integrity.

---

# Task 2 – Verify Database Normalization

### Description

The created schema was analyzed to ensure it follows standard database normalization principles.

### Activities Performed

- Verified First Normal Form (1NF).
- Verified Second Normal Form (2NF).
- Verified Third Normal Form (3NF).
- Added SQL comments explaining why the schema satisfies each normal form.

### Learning Outcome

Understood how normalization minimizes redundancy and improves database consistency.

---

# Task 3 – Modify the Database Schema

### Description

The existing schema was modified using SQL DDL commands without affecting the stored data.

### Activities Performed

- Added the `phone_number` column to the `students` table.
- Added the `max_seats` column to the `courses` table.
- Added a `CHECK` constraint on the `grade` column.
- Renamed the `hod_name` column to `head_of_dept`.
- Removed the `phone_number` column to simulate schema rollback.

### Learning Outcome

Learned how to safely update an existing database schema using `ALTER TABLE` statements.

---

## 📚 Key Concepts Learned

- Database Schema Design
- Normalization (1NF, 2NF, 3NF)
- CREATE TABLE
- ALTER TABLE
- PRIMARY KEY
- FOREIGN KEY
- UNIQUE Constraint
- CHECK Constraint
- Referential Integrity

---

## ✅ Conclusion

This hands-on provided practical experience in designing and modifying a relational database using PostgreSQL. It also reinforced the importance of normalization, constraints, and schema evolution in building reliable database systems.