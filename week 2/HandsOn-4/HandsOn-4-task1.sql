-- Task 1: Baseline Performance – No Indexes
--48. Run EXPLAIN on the query

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
-- +----+-------------+-------------+--------+---------------+---------+---------+------------------------+------+-------------+
-- | id | select_type | table       | type   | possible_keys | key     | key_len | ref                    | rows | Extra       |
-- +----+-------------+-------------+--------+---------------+---------+---------+------------------------+------+-------------+
-- |  1 | SIMPLE      | students    | ALL    | NULL          | NULL    | NULL    | NULL                   |    8 | Using where |
-- |  1 | SIMPLE      | enrollments | ref    | student_id    | student_id | 4     | college_db.students.student_id |   12 |             |
-- |  1 | SIMPLE      | courses     | eq_ref | PRIMARY       | PRIMARY | 4       | college_db.enrollments.course_id |    1 |             |
-- +----+-------------+-------------+--------+---------------+---------+---------+------------------------+------+-------------+


--49. Identify table scan

-- Observation:
-- The students table uses a Full Table Scan (type = ALL)
-- because no index exists on enrollment_year.


--50. Note estimated rows examined

-- Rows Examined:
-- students    : 8
-- enrollments : 12
-- courses     : 1

-- Conclusion:
-- Since there is no index on students.enrollment_year,
-- MySQL scans the entire students table before performing the joins.