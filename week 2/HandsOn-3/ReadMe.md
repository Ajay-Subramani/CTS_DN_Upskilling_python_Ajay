# Hands-On 3: Advanced SQL – Subqueries, Views & Transactions

---

## 📖 Overview

This hands-on focuses on advanced SQL concepts using PostgreSQL. It covers subqueries, views, user-defined functions, transactions, and savepoints to perform complex database operations while maintaining data integrity.

---

## 🎯 Objectives

- Write complex SQL queries using subqueries.
- Create and use SQL views.
- Implement user-defined functions.
- Perform transactions using COMMIT and ROLLBACK.
- Use SAVEPOINT for partial transaction rollback.

---

## 🛠️ Technologies Used

- PostgreSQL
- SQL
- pgAdmin 4
- Visual Studio Code

---

## 📂 Files

```text
HandsOn3/
├── HandsOn3.sql
└── README.md
```

---

## Tasks Completed

### Task 1 – Subqueries

- Retrieved students enrolled in more courses than the average.
- Identified courses where all students received grade 'A'.
- Found the highest-paid professor in each department.
- Filtered departments based on average professor salary.

### Task 2 – Views

- Created a student enrollment summary view.
- Created a course statistics view.
- Queried data from the created views.
- Recreated a view using `WITH CHECK OPTION`.

### Task 3 – Functions & Transactions

- Created a function to enroll students.
- Created a department transfer log table.
- Performed student transfer using transactions.
- Demonstrated transaction management using SAVEPOINT.

---

## 📚 Key Concepts Learned

- Subqueries
- Correlated & Non-Correlated Queries
- SQL Views
- User-Defined Functions
- Transactions
- COMMIT
- ROLLBACK
- SAVEPOINT
- Data Integrity

---

## ✅ Conclusion

This hands-on enhanced my understanding of advanced SQL concepts by implementing reusable views, user-defined functions, and transaction management techniques to ensure reliable and efficient database operations.