# Hands-On 5: MongoDB – Document Modelling, CRUD & Aggregation

---

## 📖 Overview

This hands-on introduces MongoDB, a NoSQL document database, by modeling course feedback data using flexible JSON-like documents. It covers document creation, CRUD operations, aggregation pipelines, and indexing to efficiently store and analyze feedback information.

---

## 🎯 Objectives

- Model data using MongoDB documents and collections.
- Perform CRUD operations on a MongoDB collection.
- Build aggregation pipelines for analytical reports.
- Create and verify indexes to improve query performance.
- Understand document-based database design.

---

## 🛠️ Technologies Used

- MongoDB Community Server
- MongoDB Compass
- MongoDB Shell (mongosh)
- JavaScript

---

## 📂 Files

```text
HandsOn5/
├── HandsOn5.js
└── README.md
```

---

# Task 1 – Create Collection and Insert Documents

## Description

Created a MongoDB database and collection to store course feedback documents with flexible document structures.

### Activities Performed

- Created the `college_nosql` database.
- Created the `feedback` collection.
- Inserted 10 feedback documents with different ratings, semesters, and tags.
- Added one document without the `attachments` field to demonstrate MongoDB's schema-less design.
- Verified the inserted documents using `countDocuments()`.

### Learning Outcome

Learned how MongoDB stores flexible documents and how collections can contain documents with different structures.

---

# Task 2 – CRUD Operations

## Description

Performed Create, Read, Update, and Delete operations on the feedback collection.

### Activities Performed

- Retrieved documents with a rating of 5.
- Retrieved CS101 feedback containing the `challenging` tag.
- Displayed selected fields using projection.
- Updated low-rated feedback by adding a `needs_review` field.
- Added a new `reviewed` tag to selected documents.
- Deleted feedback documents belonging to a specific semester.

### Learning Outcome

Learned how to efficiently perform CRUD operations on MongoDB collections using query operators and update operators.

---

# Task 3 – Aggregation Pipeline

## Description

Built aggregation pipelines to generate analytical reports and optimized queries using indexes.

### Activities Performed

- Calculated average ratings and total feedback count for each course.
- Renamed and rounded average ratings using `$project` and `$round`.
- Generated a tag frequency leaderboard using `$unwind` and `$group`.
- Created an index on `course_code`.
- Verified index usage using `explain("executionStats")` and confirmed `IXSCAN` was used instead of `COLLSCAN`.

### Learning Outcome

Learned how MongoDB Aggregation Pipelines process data efficiently and how indexes significantly improve query performance.

---

## 📚 Key Concepts Learned

- MongoDB
- Documents & Collections
- BSON
- CRUD Operations
- Projection
- Aggregation Pipeline
- `$match`
- `$group`
- `$project`
- `$sort`
- `$unwind`
- Indexes
- `IXSCAN`
- Query Optimization

---

## ✅ Conclusion

This hands-on provided practical experience in designing document-based data models, performing CRUD operations, generating analytical reports using aggregation pipelines, and improving query performance through indexing in MongoDB.