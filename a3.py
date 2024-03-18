# the code need install psycopg2, enter the next line command into cmd
# pip install psycopg2
import psycopg2

# Database connection configuration
def connect_db():
    conn = psycopg2.connect(
        dbname="a3",
        user="postgres",
        password="wasd1234",
        host="localhost"
    )
    return conn, conn.cursor()

# Get all student records
def getAllStudents():
    conn, cur = connect_db()
    cur.execute("SELECT * FROM students;")
    print("Fetching all students records:")
    for record in cur.fetchall():
        print(record)
    cur.close()
    conn.close()

# Add student records
def addStudent(first_name, last_name, email, enrollment_date):
    conn, cur = connect_db()
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
                (first_name, last_name, email, enrollment_date))
    conn.commit()
    print(f"Added student: {first_name} {last_name}, Email: {email}, Enrollment Date: {enrollment_date}")
    cur.close()
    conn.close()

# Update student email address
def updateStudentEmail(student_id, new_email):
    conn, cur = connect_db()
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s;",
                (new_email, student_id))
    conn.commit()
    print(f"Updated student ID {student_id} email to: {new_email}")
    cur.close()
    conn.close()

# Delete student records
def deleteStudent(student_id):
    conn, cur = connect_db()
    cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
    conn.commit()
    print(f"Deleted student with ID: {student_id}")
    cur.close()
    conn.close()

# Call the functions defined above in turn
# If need to test a single function, can comment the others to test it step by step, 
#    and can modify the information as required
if __name__ == '__main__':
    getAllStudents()
    addStudent('Ada', 'Doe', 'ada@example.com', '2024-03-10')
    updateStudentEmail(4, 'ada.newemail@example.com')
    deleteStudent(4)