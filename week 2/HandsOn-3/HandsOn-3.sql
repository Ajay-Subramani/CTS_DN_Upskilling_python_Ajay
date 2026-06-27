
-- task 1
--35. Students enrolled in more courses than average

SELECT
    s.student_id,
    s.first_name,
    s.last_name,
    COUNT(e.course_id) AS total_courses
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name
HAVING COUNT(e.course_id) >
(
    SELECT AVG(course_count)
    FROM
    (
        SELECT COUNT(*) AS course_count
        FROM enrollments
        GROUP BY student_id
    ) avg_enrollments
);


--36. Courses where all students scored 'A'

SELECT c.course_name
FROM courses c
WHERE NOT EXISTS
(
    SELECT 1
    FROM enrollments e
    WHERE e.course_id = c.course_id
      AND e.grade <> 'A'
);


--37. Highest paid professor in each department

SELECT
    p.professor_id,
    p.prof_name,
    p.salary,
    d.dept_name
FROM professors p
JOIN departments d
ON p.department_id = d.department_id
WHERE p.salary =
(
    SELECT MAX(salary)
    FROM professors p2
    WHERE p2.department_id = p.department_id
);


--38. Departments with average salary greater than 85000

SELECT
    d.dept_name,
    dept.avg_salary
FROM
(
    SELECT
        department_id,
        AVG(salary) AS avg_salary
    FROM professors
    GROUP BY department_id
) dept
JOIN departments d
ON dept.department_id = d.department_id
WHERE dept.avg_salary > 85000;

-- task 2
--39. Create student enrollment summary view

CREATE OR REPLACE VIEW vw_student_enrollment_summary AS
SELECT
    s.student_id,
    s.first_name || ' ' || s.last_name AS student_name,
    d.dept_name,
    COUNT(e.course_id) AS total_courses,
    ROUND(
        AVG(
            CASE
                WHEN e.grade='A' THEN 4
                WHEN e.grade='B' THEN 3
                WHEN e.grade='C' THEN 2
                WHEN e.grade='D' THEN 1
                WHEN e.grade='F' THEN 0
            END
        ),2
    ) AS gpa
FROM students s
JOIN departments d
ON s.department_id=d.department_id
LEFT JOIN enrollments e
ON s.student_id=e.student_id
GROUP BY
    s.student_id,
    student_name,
    d.dept_name;


--40. Create course statistics view

CREATE OR REPLACE VIEW vw_course_stats AS
SELECT
    c.course_name,
    c.course_code,
    COUNT(e.enrollment_id) AS total_enrollments,
    ROUND(
        AVG(
            CASE
                WHEN e.grade='A' THEN 4
                WHEN e.grade='B' THEN 3
                WHEN e.grade='C' THEN 2
                WHEN e.grade='D' THEN 1
                WHEN e.grade='F' THEN 0
            END
        ),2
    ) AS avg_gpa
FROM courses c
LEFT JOIN enrollments e
ON c.course_id=e.course_id
GROUP BY
    c.course_name,
    c.course_code;


--41. Students with GPA greater than 3

SELECT *
FROM vw_student_enrollment_summary
WHERE gpa > 3;

--42. Update through the student summary view

UPDATE vw_student_enrollment_summary
SET student_name = 'Updated Student'
WHERE student_id = 1;

-- Note:
-- This update will fail because the view is based on multiple tables
-- and is not automatically updatable in PostgreSQL.


--43. Recreate student summary view with CHECK OPTION

DROP VIEW IF EXISTS vw_student_enrollment_summary;

CREATE VIEW vw_student_enrollment_summary AS
SELECT
    student_id,
    first_name,
    last_name,
    email,
    enrollment_year
FROM students
WHERE enrollment_year >= 2022
WITH LOCAL CHECK OPTION;

--task 3
--44. Create function to enroll a student

CREATE OR REPLACE FUNCTION fn_enroll_student
(
    p_student_id INT,
    p_course_id INT,
    p_enrollment_date DATE
)
RETURNS VOID
LANGUAGE plpgsql
AS
$$
BEGIN

    IF EXISTS
    (
        SELECT 1
        FROM enrollments
        WHERE student_id = p_student_id
        AND course_id = p_course_id
    )
    THEN
        RAISE EXCEPTION 'Student is already enrolled in this course.';
    END IF;

    INSERT INTO enrollments
    (
        student_id,
        course_id,
        enrollment_date
    )
    VALUES
    (
        p_student_id,
        p_course_id,
        p_enrollment_date
    );

END;
$$;


-- Test function

SELECT fn_enroll_student(2,5,CURRENT_DATE);


--45. Create department transfer log table

CREATE TABLE department_transfer_log
(
    log_id SERIAL PRIMARY KEY,
    student_id INT,
    old_department INT,
    new_department INT,
    transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


--46. Transfer student using transaction

BEGIN;

UPDATE students
SET department_id = 2
WHERE student_id = 1;

INSERT INTO department_transfer_log
(
    student_id,
    old_department,
    new_department
)
VALUES
(
    1,
    1,
    2
);

COMMIT;


--47. Demonstrate SAVEPOINT and partial rollback

BEGIN;

INSERT INTO enrollments
(
    student_id,
    course_id,
    enrollment_date
)
VALUES
(
    3,
    2,
    CURRENT_DATE
);

SAVEPOINT first_insert;

-- Intentional duplicate enrollment
INSERT INTO enrollments
(
    student_id,
    course_id,
    enrollment_date
)
VALUES
(
    3,
    2,
    CURRENT_DATE
);

ROLLBACK TO SAVEPOINT first_insert;

COMMIT;


-- Verify inserted record

SELECT *
FROM enrollments
WHERE student_id = 3
AND course_id = 2;