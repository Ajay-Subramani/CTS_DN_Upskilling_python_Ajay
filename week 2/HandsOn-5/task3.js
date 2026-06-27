// Task 3: Aggregation Pipeline
//71. Average rating and feedback count for 2022-ODD

db.feedback.aggregate([
    {
        $match: {
            semester: "2022-ODD"
        }
    },
    {
        $group: {
            _id: "$course_code",
            avg_rating: {
                $avg: "$rating"
            },
            total_feedback: {
                $sum: 1
            }
        }
    },
    {
        $sort: {
            avg_rating: -1
        }
    }
]);


//72. Rename average rating and round to 1 decimal

db.feedback.aggregate([
    {
        $match: {
            semester: "2022-ODD"
        }
    },
    {
        $group: {
            _id: "$course_code",
            avg_rating: {
                $avg: "$rating"
            },
            total_feedback: {
                $sum: 1
            }
        }
    },
    {
        $project: {
            _id: 0,
            course_code: "$_id",
            average_rating: {
                $round: ["$avg_rating", 1]
            },
            total_feedback: 1
        }
    },
    {
        $sort: {
            average_rating: -1
        }
    }
]);


//73. Tag frequency leaderboard

db.feedback.aggregate([
    {
        $unwind: "$tags"
    },
    {
        $group: {
            _id: "$tags",
            tag_count: {
                $sum: 1
            }
        }
    },
    {
        $sort: {
            tag_count: -1
        }
    }
]);


//74. Create index on course_code

db.feedback.createIndex(
    {
        course_code: 1
    }
);


// Verify index usage

db.feedback.find(
    {
        course_code: "CS101"
    }
).explain("executionStats");


// Expected Output:
//
// Aggregation 1:
// One document per course with average rating and feedback count.
//
// Aggregation 2:
// Average rating displayed as 'average_rating'
// rounded to one decimal place.
//
// Aggregation 3:
// Displays tags ordered by highest frequency.
//
// Explain:
// Winning plan should contain "IXSCAN"
// instead of "COLLSCAN".