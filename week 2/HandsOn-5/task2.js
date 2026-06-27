// Task 2: CRUD Operations
//65. Find all feedback with rating 5

db.feedback.find(
    { rating: 5 }
);


//66. Find CS101 feedback with 'challenging' tag

db.feedback.find(
    {
        course_code: "CS101",
        tags: "challenging"
    }
);


//67. Retrieve only student_id, course_code and rating

db.feedback.find(
    {},
    {
        _id: 0,
        student_id: 1,
        course_code: 1,
        rating: 1
    }
);


//68. Add needs_review field for rating less than 3

db.feedback.updateMany(
    {
        rating: { $lt: 3 }
    },
    {
        $set: {
            needs_review: true
        }
    }
);


// Verify

db.feedback.find(
    {
        needs_review: true
    }
);


//69. Add 'reviewed' tag to documents needing review

db.feedback.updateMany(
    {
        needs_review: true
    },
    {
        $push: {
            tags: "reviewed"
        }
    }
);


// Verify

db.feedback.find(
    {
        needs_review: true
    }
);


//70. Delete feedback from semester '2021-EVEN'

db.feedback.deleteMany(
    {
        semester: "2021-EVEN"
    }
);


// Verify

db.feedback.find();

db.feedback.countDocuments();

// Expected Output:
// 9 documents remaining