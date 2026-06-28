from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (
    Department,
    Student,
    Course,
    Enrollment
)

DATABASE_URL = "mysql+pymysql://root:root@localhost/college_dbs_orm"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

Session = sessionmaker(bind=engine)
session = Session()


# Task 2: CRUD Operations

# 80. Open Session

print("Session Started")


# 81. Insert Departments

cs = Department(
    dept_name="Computer Science",
    hod_name="Dr. Ramesh Kumar",
    budget=850000
)

ec = Department(
    dept_name="Electronics",
    hod_name="Dr. Priya Nair",
    budget=620000
)

me = Department(
    dept_name="Mechanical",
    hod_name="Dr. Suresh Iyer",
    budget=540000
)

session.add_all([cs, ec, me])
session.commit()

print("Departments Inserted")


# Insert Students

students = [

    Student(
        first_name="Arjun",
        last_name="Mehta",
        email="arjun@gmail.com",
        enrollment_year=2022,
        department=cs
    ),

    Student(
        first_name="Priya",
        last_name="Suresh",
        email="priya@gmail.com",
        enrollment_year=2022,
        department=cs
    ),

    Student(
        first_name="Rohan",
        last_name="Verma",
        email="rohan@gmail.com",
        enrollment_year=2021,
        department=ec
    ),

    Student(
        first_name="Sneha",
        last_name="Patel",
        email="sneha@gmail.com",
        enrollment_year=2023,
        department=me
    ),

    Student(
        first_name="Vikram",
        last_name="Das",
        email="vikram@gmail.com",
        enrollment_year=2022,
        department=cs
    )

]

session.add_all(students)
session.commit()

print("Students Inserted")


# 82. Insert Courses

course1 = Course(
    course_name="Data Structures",
    course_code="CS101",
    credits=4,
    department=cs
)

course2 = Course(
    course_name="Database Management Systems",
    course_code="CS102",
    credits=3,
    department=cs
)

course3 = Course(
    course_name="Circuit Theory",
    course_code="EC101",
    credits=3,
    department=ec
)

session.add_all([course1, course2, course3])
session.commit()

print("Courses Inserted")


# Insert Enrollments

enrollments = [

    Enrollment(
        student=students[0],
        course=course1
    ),

    Enrollment(
        student=students[1],
        course=course1
    ),

    Enrollment(
        student=students[2],
        course=course3
    ),

    Enrollment(
        student=students[4],
        course=course2
    )

]

session.add_all(enrollments)
session.commit()

print("Enrollments Inserted")


# 83. Read Students in Computer Science

print("\nStudents in Computer Science Department\n")

cs_students = (
    session.query(Student)
    .join(Department)
    .filter(Department.dept_name == "Computer Science")
    .all()
)

for student in cs_students:
    print(
        student.student_id,
        student.first_name,
        student.last_name
    )


# 84. Read Enrollments

print("\nEnrollment Details\n")

records = session.query(Enrollment).all()

for record in records:
    print(
        record.student.first_name,
        "->",
        record.course.course_name
    )


# 85. Update Student Enrollment Year

student = (
    session.query(Student)
    .filter(Student.email == "arjun@gmail.com")
    .first()
)

if student:
    student.enrollment_year = 2024
    session.commit()
    print("\nStudent Updated Successfully")


# Verify Update

updated_student = (
    session.query(Student)
    .filter(Student.email == "arjun@gmail.com")
    .first()
)

print(
    updated_student.first_name,
    updated_student.enrollment_year
)


# 86. Delete Enrollment

enrollment = session.query(Enrollment).first()

if enrollment:
    session.delete(enrollment)
    session.commit()
    print("\nEnrollment Deleted Successfully")


# Verify Delete

print("\nRemaining Enrollments")

remaining = session.query(Enrollment).all()

for record in remaining:
    print(
        record.enrollment_id,
        record.student.first_name,
        record.course.course_name
    )

# Task 3: Eager Loading to Fix N+1 Problem

# 87. Observe the N+1 Problem

print("\nN+1 Problem Demonstration\n")

enrollments = session.query(Enrollment).all()

for enrollment in enrollments:
    print(
        enrollment.student.first_name,
        "-",
        enrollment.course.course_name
    )

print("\nObservation:")
print("With echo=True, SQLAlchemy executes multiple SQL queries.")
print("One query retrieves enrollments, followed by additional")
print("queries to fetch each related student and course.")
print("This is known as the N+1 Query Problem.")


# 88. Use joinedload to eliminate N+1

from sqlalchemy.orm import joinedload

print("\nUsing joinedload()\n")

enrollments = (
    session.query(Enrollment)
    .options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    )
    .all()
)

for enrollment in enrollments:
    print(
        enrollment.student.first_name,
        "-",
        enrollment.course.course_name
    )


# 89. Verify Query Count

print("\nObservation:")
print("With joinedload(), SQLAlchemy generates a single JOIN query.")
print("All related Student and Course data is loaded together.")
print("Query count is reduced significantly.")


# 90. Compare Results

print("\nComparison")
print("--------------------------------------------")
print("Without joinedload()")
print("- Multiple SQL queries are executed.")
print("- N+1 Query Problem occurs.")
print("- Lower performance.")

print("\nWith joinedload()")
print("- Single JOIN query is executed.")
print("- N+1 Problem is eliminated.")
print("- Better performance.")


# 91. Bonus - Django ORM Equivalent

print("\nBonus (Django ORM)")
print("--------------------------------------------")
print(
    "Enrollment.objects.select_related('student', 'course').all()"
)

session.close()

print("\nSession Closed")


#Hands-On 6 - SQLAlchemy ORM

#Task 2:
#- CRUD operations implemented using SQLAlchemy Session.

#Task 3:
# - Without joinedload():
#  Multiple SQL queries are executed (N+1 Problem).

#- With joinedload():
#  A single JOIN query retrieves Enrollment,
#  Student and Course data efficiently.

#Result:
#Query count is reduced from multiple queries
#to a single optimized query using joinedload().