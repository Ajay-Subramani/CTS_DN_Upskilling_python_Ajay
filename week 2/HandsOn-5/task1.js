// Task 1: Create the Collection and Insert Documents
//60. Create database

use("college_nosql");


//61. Create feedback collection

db.createCollection("feedback");

//62. Insert 10 feedback documents

db.feedback.insertMany([
{
    student_id: 1,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 5,
    comments: "Excellent teaching. Would recommend.",
    tags: ["challenging", "well-structured", "good-examples"],
    submitted_at: new Date("2022-11-30T10:15:00Z"),
    attachments: [
        { filename: "notes.pdf", size_kb: 240 }
    ]
},
{
    student_id: 2,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 4,
    comments: "Good explanations and practical sessions.",
    tags: ["challenging", "interactive"],
    submitted_at: new Date("2022-11-29T09:20:00Z"),
    attachments: [
        { filename: "assignment.pdf", size_kb: 180 }
    ]
},
{
    student_id: 3,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 3,
    comments: "Average course with useful examples.",
    tags: ["good-examples"],
    submitted_at: new Date("2022-11-28T11:00:00Z"),
    attachments: [
        { filename: "lab.pdf", size_kb: 210 }
    ]
},
{
    student_id: 4,
    course_code: "CS102",
    semester: "2022-EVEN",
    rating: 5,
    comments: "Loved the database concepts.",
    tags: ["well-structured", "interesting"],
    submitted_at: new Date("2022-12-02T08:30:00Z"),
    attachments: [
        { filename: "db_notes.pdf", size_kb: 300 }
    ]
},
{
    student_id: 5,
    course_code: "CS102",
    semester: "2022-EVEN",
    rating: 2,
    comments: "Needs more practical examples.",
    tags: ["difficult"],
    submitted_at: new Date("2022-12-01T10:45:00Z"),
    attachments: [
        { filename: "feedback.docx", size_kb: 150 }
    ]
},
{
    student_id: 6,
    course_code: "EC101",
    semester: "2021-EVEN",
    rating: 1,
    comments: "Course pace was too fast.",
    tags: ["fast-paced"],
    submitted_at: new Date("2021-11-20T09:00:00Z"),
    attachments: [
        { filename: "review.pdf", size_kb: 100 }
    ]
},
{
    student_id: 7,
    course_code: "ME101",
    semester: "2023-ODD",
    rating: 4,
    comments: "Very informative sessions.",
    tags: ["practical", "interactive"],
    submitted_at: new Date("2023-10-10T12:00:00Z"),
    attachments: [
        { filename: "summary.pdf", size_kb: 190 }
    ]
},
{
    student_id: 8,
    course_code: "CS103",
    semester: "2023-ODD",
    rating: 5,
    comments: "Excellent programming assignments.",
    tags: ["coding", "challenging"],
    submitted_at: new Date("2023-10-12T14:00:00Z"),
    attachments: [
        { filename: "programs.zip", size_kb: 450 }
    ]
},
{
    student_id: 9,
    course_code: "CS103",
    semester: "2023-ODD",
    rating: 2,
    comments: "Assignments were difficult.",
    tags: ["challenging"],
    submitted_at: new Date("2023-10-13T15:30:00Z"),
    attachments: [
        { filename: "assignment.docx", size_kb: 170 }
    ]
},
{
    student_id: 10,
    course_code: "CS104",
    semester: "2022-ODD",
    rating: 4,
    comments: "Good course content.",
    tags: ["well-structured", "helpful"],
    submitted_at: new Date("2022-11-27T16:00:00Z")
}
]);


//63. Verify one document without attachments

db.feedback.find(
    { student_id: 10 }
);


//64. Count total documents

db.feedback.countDocuments();

// Expected Output:
// 10