# Hands-On 7: Migrations & Versioning using Alembic

---

## 📖 Overview

This hands-on demonstrates database schema versioning using Alembic with SQLAlchemy. It covers creating migration files, applying schema changes, tracking migration history, and performing rollback and recovery operations to keep the database schema synchronized with the application models.

---

## 🎯 Objectives

- Configure Alembic for SQLAlchemy.
- Generate and apply database migrations.
- Modify the database schema using incremental migrations.
- Track migration history and schema versions.
- Perform rollback and recovery of database migrations.

---

## 🛠️ Technologies Used

- Python
- SQLAlchemy
- Alembic
- MySQL
- PyMySQL
- Visual Studio Code

---

## 📂 Files

```text
HandsOn7/
├── models.py
├── requirements.txt
├── README.md
├── Task1_Observation.txt
├── Task2_Observation.txt
├── Task3_Observation.txt
├── alembic.ini
└── migrations/
    ├── env.py
    ├── script.py.mako
    ├── README
    └── versions/
        ├── initial_schema.py
        ├── add_is_active_to_students.py
        └── create_course_schedules.py
```

---

# Task 1 – Alembic Setup and Initial Migration

## Description

Configured Alembic for the SQLAlchemy project and generated the initial migration from the existing ORM models.

### Activities Performed

- Initialized Alembic in the project.
- Configured the database connection in `alembic.ini`.
- Linked Alembic with SQLAlchemy models using `Base.metadata`.
- Generated the initial migration.
- Applied the migration to the database.
- Verified the creation of the `alembic_version` table.

### Learning Outcome

Learned how Alembic generates and applies migration files while maintaining database version history.

---

# Task 2 – Incremental Migrations

## Description

Modified the database schema by adding a new column and creating a new table using Alembic migrations.

### Activities Performed

- Added the `is_active` column to the Student model.
- Generated and applied a migration for the new column.
- Created the `CourseSchedule` model.
- Generated and applied a migration for the new table.
- Verified the schema changes in MySQL.
- Viewed the complete migration history.

### Learning Outcome

Learned how to evolve a database schema safely using incremental migrations without manually writing SQL.

---

# Task 3 – Rollback and Recovery

## Description

Performed rollback operations to previous migration versions and restored the latest schema using Alembic.

### Activities Performed

- Checked the current migration revision.
- Rolled back one migration.
- Rolled back all migrations to the base revision.
- Reapplied all migrations to the latest version.
- Verified the database schema after each operation.

### Learning Outcome

Learned how Alembic manages schema version history and safely restores previous or latest database states.

---

## 📚 Key Concepts Learned

- Database Migrations
- Schema Versioning
- Alembic
- SQLAlchemy Integration
- Migration History
- Upgrade and Downgrade
- Rollback and Recovery
- Version Control for Database Schema

---

## ✅ Conclusion

This hands-on provided practical experience in managing database schema changes using Alembic. It demonstrated how to generate migrations, apply incremental schema updates, track migration history, and safely perform rollback and recovery operations while keeping the database synchronized with SQLAlchemy models.