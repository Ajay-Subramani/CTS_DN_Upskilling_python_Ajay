# Database Integration

This repository contains the hands-on exercises completed as part of the **Digital Nurture 5.0 – Python Full Stack Engineer Track** for the **Database Integration** module.

## Database Schema

A MySQL database named **`college_dbs`** and **`college_dbs_orm`** was created based on the given **Student Course Registration System**. The database schema includes all required tables, relationships, constraints, and sample data provided in the hands-on exercise book.

**`college_db.sql`** contains:

- Database creation
- Table creation
- Primary Key and Foreign Key constraints
- Sample data insertion

---

## Hands-On Exercises

Each hands-on exercise is organized in its own directory.

- Every SQL exercise is saved as **`HandsOn-{n}.sql`**, where **n** is the exercise number.
- SQLAlchemy ORM and Alembic exercises are implemented using **Python**.
- Every hands-on directory contains a dedicated **`README.md`** explaining the objectives, implementation, and expected outcomes.

---

## Folder Structure

```text
Week4-5_DatabaseIntegration/
│
├── DBSchema.sql
├── README.md
│
├── HandsOn1/
│   ├── HandsOn1.sql
│   └── README.md
│
├── HandsOn2/
│   ├── HandsOn2.sql
│   └── README.md
│
├── HandsOn3/
│   ├── HandsOn3.sql
│   └── README.md
│
├── HandsOn4/
│   ├── HandsOn4.sql
│   ├── handsOn-4-task3.py
│   └── README.md
│
├── HandsOn5/
│   ├── HandsOn5.js
│   └── README.md
│
├── HandsOn6/
│   ├── models.py
│   ├── crud.py
│   ├── requirements.txt
│   └── README.md
│
└── HandsOn7/
    ├── models.py
    ├── crud.py
    ├── requirements.txt
    ├── alembic.ini
    ├── README.md
    ├── Task1_Observation.txt
    ├── Task2_Observation.txt
    ├── Task3_Observation.txt
    └── migrations/
        ├── env.py
        ├── script.py.mako
        ├── README
        └── versions/
```

---

## Topics Covered

- Database Schema Design
- SQL DDL, DML and DQL Operations
- Joins and Aggregate Functions
- Query Optimization and Indexing
- EXPLAIN and Query Execution Plans
- N+1 Query Problem
- MongoDB CRUD Operations
- Aggregation Pipeline
- SQLAlchemy ORM
- ORM Relationships and CRUD Operations
- Alembic Database Migrations
- Database Versioning and Rollback

---

## Technologies Used

- MySQL
- MongoDB
- Python
- SQLAlchemy
- Alembic
- PyMySQL
- MongoDB Shell (mongoosh)
- Visual Studio Code

---

## Learning Outcomes

After completing this module, I gained practical experience in:

- Designing and creating relational database schemas.
- Writing SQL queries for data retrieval and manipulation.
- Optimizing database performance using indexes and query execution plans.
- Working with MongoDB collections, CRUD operations, and aggregation pipelines.
- Building database applications using SQLAlchemy ORM.
- Managing schema changes through Alembic migrations.
- Understanding database versioning, migration history, and rollback strategies.

---

## Conclusion

This repository demonstrates the practical implementation of database concepts using **MySQL**, **MongoDB**, **SQLAlchemy ORM**, and **Alembic**. The hands-on exercises cover database design, querying, optimization, NoSQL operations, ORM integration, and schema versioning, providing a strong foundation in database integration for Python Full Stack development.