import csv
import os


# Student CSV file location
FILE = "students.csv"



# ================= ADD STUDENT =================

def add_student(student_id, name, roll_no, department, year, mobile):

    file_exists = os.path.exists(FILE)


    with open(FILE, "a", newline="") as f:

        writer = csv.writer(f)


        writer.writerow([
            student_id,
            name,
            roll_no,
            department,
            year,
            mobile
        ])


    return "Student Added Successfully"



# ================= VIEW STUDENTS =================

def view_students():

    students = {}


    if not os.path.exists(FILE):

        return students


    with open(FILE, "r") as f:

        reader = csv.reader(f)


        for row in reader:

            if len(row) >= 6:

                students[row[0]] = row


    return students



# ================= SEARCH STUDENT =================

def search_student(student_id):

    students = view_students()


    if student_id in students:

        return students[student_id]


    return None



# ================= UPDATE STUDENT =================

def update_student(student_id, name, roll_no, department, year, mobile):

    students = view_students()


    if student_id not in students:

        return "Student Not Found"



    students[student_id] = [

        student_id,
        name,
        roll_no,
        department,
        year,
        mobile

    ]



    save_students(students)


    return "Student Updated Successfully"




# ================= DELETE STUDENT =================

def delete_student(student_id):

    students = view_students()


    if student_id not in students:

        return "Student Not Found"



    del students[student_id]


    save_students(students)


    return "Student Deleted Successfully"




# ================= SAVE DATA =================

def save_students(students):

    with open(FILE, "w", newline="") as f:

        writer = csv.writer(f)


        for student in students.values():

            writer.writerow(student)




# ================= STUDENT LOGIN =================

def student_login(student_id, mobile):

    students = view_students()


    if student_id in students:


        student = students[student_id]


        stored_mobile = str(student[5]).strip()

        entered_mobile = str(mobile).strip()



        if stored_mobile == entered_mobile:

            return True



    return False