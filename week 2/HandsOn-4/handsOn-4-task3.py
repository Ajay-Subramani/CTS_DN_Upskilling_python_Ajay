import mysql.connector
import time

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_dbs"
)

cursor = conn.cursor()
# 56. Simulate N+1 Problem

print("Version 1 : N+1 Problem")

query_count = 0

start = time.time()

# First query
cursor.execute("SELECT student_id, course_id FROM enrollments")
enrollments = cursor.fetchall()
query_count += 1

for enrollment in enrollments:
    student_id = enrollment[0]

    cursor.execute(
        "SELECT first_name, last_name FROM students WHERE student_id = %s",
        (student_id,)
    )
    student = cursor.fetchone()
    query_count += 1

    print(student)

end = time.time()

print(f"\nQueries Executed : {query_count}")
print(f"Execution Time   : {end-start:.6f} seconds")

# 57. Fix N+1 using JOIN

print("\nVersion 2 : JOIN Query")

query_count = 0

start = time.time()

cursor.execute("""
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
    ON s.student_id = e.student_id
JOIN courses c
    ON c.course_id = e.course_id
""")

records = cursor.fetchall()
query_count += 1

for row in records:
    print(row)

end = time.time()

print(f"\nQueries Executed : {query_count}")
print(f"Execution Time   : {end-start:.6f} seconds")


# 58. Compare Round Trips

print("\nComparison")
print("--------------------------")
print("Version 1 : Multiple Queries")
print("Version 2 : Single JOIN Query")
print("JOIN eliminates unnecessary database round-trips.")

# 59. N+1 Observation

print("\nObservation")
print("--------------------------------------------")
print("If there are 10,000 enrollments:")
print("Version 1 -> 10,001 queries")
print("Version 2 -> 1 query")

cursor.close()
conn.close()


"""----- Version 1 : N+1 Problem -----

--('Arjun', 'Mehta')
--('Arjun', 'Mehta')
--('Priya', 'Suresh')

--Queries Executed : 13
--Execution Time   : 0.008123 seconds

----- Version 2 : JOIN Query -----

--('Arjun', 'Mehta', 'Data Structures & Algorithms')
--('Arjun', 'Mehta', 'Database Management Systems')

--Queries Executed : 1
--Execution Time   : 0.001257 seconds

--Comparison
--------------------------
--Version 1 : Multiple Queries
--Version 2 : Single JOIN Query
--JOIN eliminates unnecessary database round-trips.

--Observation
--------------------------------------------
--If there are 10,000 enrollments:
--Version 1 -> 10,001 queries
--Version 2 -> 1 query"""