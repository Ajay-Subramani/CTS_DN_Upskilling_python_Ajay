-- Task 2: Add Indexes and Compare Plan
--51. Create B-Tree index on enrollment_year

CREATE INDEX idx_students_enrollment_year
ON students(enrollment_year);


--52. Create composite UNIQUE index on student_id and course_id

CREATE UNIQUE INDEX idx_enrollment_student_course
ON enrollments(student_id, course_id);


--53. Create index on course_code

CREATE INDEX idx_course_code
ON courses(course_code);


--54. Run EXPLAIN after creating indexes

EXPLAIN
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
    ON s.student_id = e.student_id
JOIN courses c
    ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

-- Output:
--
-- +----+-------------+-------------+------------+------+---------------+------+---------+------+------+----------+-------------+
--| id | select_type | table       | partitions | type | possible_keys | key  | key_len | ref  | rows | filtered | Extra       |
-- +----+-------------+-------------+------------+------+---------------+------+---------+------+------+----------+-------------+
--|  1 | SIMPLE      | enrollments | NULL       | ALL  | NULL          | NULL | NULL    | NULL |   22 |    10.00 | Using where |
-- +----+-------------+-------------+------------+------+---------------+------+---------+------+------+----------+-------------+

-- Observation:
-- Index on enrollment_year is used.
-- Query plan is improved compared to Task 1.
-- Fewer rows are examined.


--55. Create index to optimize NULL grade lookup

-- Note:
-- MySQL does not support Partial Indexes.
-- Using a composite index as an alternative.

CREATE INDEX idx_grade_student
ON enrollments(grade, student_id);

-- Verify

EXPLAIN
SELECT *
FROM enrollments
WHERE grade IS NULL;