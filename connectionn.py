import mysql.connector
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gokulnath143",
        port=3306,
        use_pure=True
    )
    cursor=conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS college_db")
    print("Database created successfully")
    cursor.execute("USE college_db")
    create="""CREATE TABLE STUDENTS(
                roll_number INT,
                name VARCHAR(30),
                department VARCHAR(30),
                SECTION VARCHAR(10))"""
    def insert_student(roll_number, name, department, section):
        sql = "INSERT INTO STUDENTS (roll_number, name, department, section) VALUES (%s, %s, %s, %s)"
        values = (roll_number, name, department, section)
        cursor.execute(sql, values)
        conn.commit()
        print(f"Inserted student: {name}")

    insert_student(1, "Gokul", "CSE", "A")
    insert_student(2, "Mouli", "CY", "B")

    def view_students():
        cursor.execute("SELECT * FROM STUDENTS")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    
    def update_student(roll_number, new_name=None, new_department=None, new_section=None):
        updates = []
        values = []
        if new_name:
            updates.append("name=%s")
            values.append(new_name)
        if new_department:
            updates.append("department=%s")
            values.append(new_department)
        if new_section:
            updates.append("section=%s")
            values.append(new_section)
        
        values.append(roll_number)
        sql = f"UPDATE STUDENTS SET {', '.join(updates)} WHERE roll_number=%s"
        cursor.execute(sql, values)
        conn.commit()
        print(f"Updated student roll_number={roll_number}")
        print("\nAll students:")
    view_students()

    def delete_student(roll_number):
        sql = "DELETE FROM STUDENTS WHERE roll_number=%s"
        cursor.execute(sql, (roll_number,))
        conn.commit()
        print(f"Deleted student roll_number={roll_number}")
    
except Exception as e:
    print("Error",e)
cursor.close()
