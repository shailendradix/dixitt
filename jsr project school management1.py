import mysql.connector

# to connect to mysql 
db = mysql.connector.connect(
    host="localhost",
    user="SHAILENDRA",
    password="shailendra@123",
    database="school_management"
)

# creating a cursor object we will use this for all operations
cursor = db.cursor()

# defining function for adding student 
def add_student():
    roll_number = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    grade = input("Enter Grade: ")
    section = input("Enter Section: ")
    
    sql = "INSERT INTO students (roll_number, name, grade, section) VALUES (%s, %s, %s, %s)"
    values = (roll_number, name, grade, section)
    
    cursor.execute(sql, values)
    db.commit()
    
    print("Student added successfully.")

# in case we want to see data off all students defining function 
def display_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    
    if students:
        print("Roll Number\tName\tGrade\tSection")
        print("-----------------------------------------")
        for student in students:
            print(f"{student[0]}\t\t{student[1]}\t{student[2]}\t{student[3]}")
    else:
        print("No students found.")

# defining function to update existing data of student
def update_student():
    roll_number = int(input("Enter Roll Number of the student to update: "))
    field = input("Enter the field to update (name/grade/section): ")
    new_value = input("Enter the new value: ")
    
    sql = f"UPDATE students SET {field} = %s WHERE roll_number = %s"
    values = (new_value, roll_number)
    
    cursor.execute(sql, values)
    db.commit()
    
    if cursor.rowcount == 0:
        print("No student found with the provided roll number.")
    else:
        print("Student details updated successfully.")

# defining function to delete student record 
def delete_student():
    roll_number = int(input("Enter Roll Number of the student to delete: "))
    
    sql = "DELETE FROM students WHERE roll_number = %s"
    values = (roll_number,)
    
    cursor.execute(sql, values)
    db.commit()
    
    if cursor.rowcount == 0:
        print("No student found with the provided roll number.")
    else:
        print("Student record deleted successfully.")
# Function to add a new employee
def add_employee():
    employee_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    designation = input("Enter Designation: ")
    salary = float(input("Enter Salary: "))
    
    sql = "INSERT INTO employees (employee_id, name, designation, salary) VALUES (%s, %s, %s, %s)"
    values = (employee_id, name, designation, salary)
    
    cursor.execute(sql, values)
    db.commit()
    
    print("Employee added successfully.")

# Function to display all employees
def display_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    
    if employees:
        print("Employee ID\tName\tDesignation\tSalary")
        print("-----------------------------------------")
        for employee in employees:
            print(f"{employee[0]}\t\t{employee[1]}\t{employee[2]}\t\t{employee[3]}")
    else:
        print("No employees found.")

# Function to update an employee's details
def update_employee():
    employee_id = int(input("Enter Employee ID to update: "))
    field = input("Enter the field to update (name/designation/salary): ")
    new_value = input("Enter the new value: ")
    
    sql = f"UPDATE employees SET {field} = %s WHERE employee_id = %s"
    values = (new_value, employee_id)
    
    cursor.execute(sql, values)
    db.commit()
    
    if cursor.rowcount == 0:
        print("No employee found with the provided ID.")
    else:
        print("Employee details updated successfully.")

# Function to delete an employee's record
def delete_employee():
    employee_id = int(input("Enter Employee ID to delete: "))
    
    sql = "DELETE FROM employees WHERE employee_id = %s"
    values = (employee_id,)
    
    cursor.execute(sql, values)
    db.commit()
    
    if cursor.rowcount == 0:
        print("No employee found with the provided ID.")
    else:
        print("Employee record deleted successfully.")

# Function to add a new fee record
def add_fee():
    student_id = int(input("Enter Student ID: "))
    
    # Check if income certificate is submitted
    cursor.execute("SELECT income_certificate FROM students WHERE student_id = %s", (student_id,))
    result = cursor.fetchone()
    
    if result and result[0] == "submitted":
        print("Income certificate submitted. No fee required.")
        return
    
    amount = float(input("Enter Amount: "))
    date = input("Enter Date (DD-MM-YYYY): ")
    
    sql = "INSERT INTO fees (student_id, amount, date) VALUES (%s, %s, %s)"
    values = (student_id, amount, date)
    
    cursor.execute(sql, values)
    db.commit()
    
    print("Fee record added successfully.")

# Function to display all fee records
def display_fees():
    cursor.execute("SELECT * FROM fees")
    fees = cursor.fetchall()
    
    if fees:
        print("Fee ID\tStudent ID\tAmount\tDate")
        print("--------------------------------")
        for fee in fees:
            print(f"{fee[0]}\t{fee[1]}\t\t{fee[2]}\t{fee[3]}")
    else:
        print("No fee records found.")

# Function to add a new exam record
def add_exam():
    exam_id = int(input("Enter Exam ID: "))
    subject = input("Enter Subject: ")
    date = input("Enter Date (YYYY-MM-DD): ")
    
    sql = "INSERT INTO exams (exam_id, subject, date) VALUES (%s, %s, %s)"
    values = (exam_id, subject, date)
    
    cursor.execute(sql, values)
    db.commit()
    
    print("Exam record added successfully.")

# Function to display all exam records
def display_exams():
    cursor.execute("SELECT * FROM exams")
    exams = cursor.fetchall()
    
    if exams:
        print("Exam ID\tSubject\t\tDate")
        print("--------------------------")
        for exam in exams:
            print(f"{exam[0]}\t{exam[1]}\t\t{exam[2]}")
    else:
        print("No exam records found.")

# Function to update an exam record
def update_exam():
    exam_id = int(input("Enter Exam ID to update: "))
    field = input("Enter the field to update (subject/date): ")
    new_value = input("Enter the new value: ")
    
    sql = f"UPDATE exams SET {field} = %s WHERE exam_id = %s"
    values = (new_value, exam_id)
    
    cursor.execute(sql, values)
    db.commit()
    
    if cursor.rowcount == 0:
        print("No exam found with the provided ID.")
    else:
        print("Exam details updated successfully.")

# Function to delete an exam record
def delete_exam():
    exam_id = int(input("Enter Exam ID to delete: "))
    
    sql = "DELETE FROM exams WHERE exam_id = %s"
    values = (exam_id,)
    
    cursor.execute(sql, values)
    db.commit()
    
    if cursor.rowcount == 0:
        print("No exam found with the provided ID.")
    else:
        print("Exam record deleted successfully.")
# Function to add a new hostel record
def add_hostel():
    house = input("Enter House (Shivalik/Aravali/Neelgiri/Udaygiri): ")
    gender = input("Enter Gender (G/SJ/SB): ")
    capacity = int(input("Enter Capacity: "))
    
    sql = "INSERT INTO hostels (house, gender, capacity) VALUES (%s, %s, %s)"
    values = (house, gender, capacity)
    
    cursor.execute(sql, values)
    db.commit()
    
    print("Hostel added successfully.")

# Function to display all hostel records
def display_hostels():
    cursor.execute("SELECT * FROM hostels")
    hostels = cursor.fetchall()
    
    if hostels:
        print("Hostel ID\tHouse\t\tGender\tCapacity")
        print("----------------------------------------")
        for hostel in hostels:
            print(f"{hostel[0]}\t\t{hostel[1]}\t{hostel[2]}\t\t{hostel[3]}")
    else:
        print("No hostel records found.")

# Function to update a hostel record
def update_hostel():
    hostel_id = int(input("Enter Hostel ID to update: "))
    field = input("Enter the field to update (house/gender/capacity): ")
    new_value = input("Enter the new value: ")
    
    sql = f"UPDATE hostels SET {field} = %s WHERE hostel_id = %s"
    values = (new_value, hostel_id)
    
    cursor.execute(sql, values)
    db.commit()
    
    if cursor.rowcount == 0:
        print("No hostel found with the provided ID.")
    else:
        print("Hostel details updated successfully.")

# Function to delete a hostel record
def delete_hostel():
    hostel_id = int(input("Enter Hostel ID to delete: "))
    
    sql = "DELETE FROM hostels WHERE hostel_id = %s"
    values = (hostel_id,)
    
    cursor.execute(sql, values)
    db.commit()
    
    if cursor.rowcount == 0:
        print("No hostel found with the provided ID.")
    else:
        print("Hostel record deleted successfully.")

# our main program starts from here

while True:
    print("\nSchool Management System")
    print ("JAWAHAR NAVODAYA VIDYALAYA  KANPUR DEHAT")
    print("------------------------")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Student")
    print("4. Delete Student")
    
    print("\nEmployee Management System")
    print("--------------------------")
    print("5. Add Employee")
    print("6. Display Employees")
    print("7. Update Employee")
    print("8. Delete Employee")


    print("\nFee Management System")
    print("---------------------")
    print("9. Add Fee")
    print("10. Display Fees")

   

    
   
    print("\nExam Management System")
    print("----------------------")
    print("11. Add Exam")
    print("12. Display Exams")
    print("13. Update Exam")
    print("14. Delete Exam")
 

    print("\nHostel Management System")
    print("------------------------")
    print("15. Add Hostel")
    print("16. Display Hostels")
    print("17. Update Hostel")
    print("18. Delete Hostel")
    print("19. Exit")


    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
  
       
        
    if choice == 5:
        add_employee()
    elif choice == 6:
        display_employees()
    elif choice == 7:
        update_employee()
    elif choice == 8:
        delete_employee()
    if choice == 9:
        add_fee()
    elif choice == 10:
        display_fees()
    if choice == 11:
        add_exam()
    elif choice == 12:
        display_exams()
    elif choice == 13:
        update_exam()
    elif choice == 14:
        delete_exam()
    if choice == 15:
        add_hostel()
    elif choice == 16:
        display_hostels()
    elif choice == 17:
        update_hostel()
    elif choice == 18:
        delete_hostel()
    elif choice == 19:
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
db.close()


   



