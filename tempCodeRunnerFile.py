from modules import login
from modules import book
from modules import student
from modules import issue
from modules import report

while True:

    print("\n====================================")
    print("   LIBRARY MANAGEMENT SYSTEM")
    print("====================================")
    print("1. Admin Login")
    print("2. Student Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        if login.admin_login():

            while True:

               print("\n========== ADMIN PANEL ==========")
               print("1. Book Management")
               print("2. Student Management")
               print("3. Issue Book")
               print("4. Return Book")
               print("5. Reports")
               print("6. Logout")

               admin_choice = input("Enter your choice: ")

               if admin_choice == "1":
                   book.book_menu()

               elif admin_choice == "2":
                     student.student_menu()

               elif admin_choice == "3":
                     issue.issue_book()

               elif admin_choice == "4":
                     issue.return_book()

               elif admin_choice == "5":
                     report.reports()

               elif admin_choice == "6":
                break

            else:
                print("Invalid Choice!")
                
    elif choice == "2":

        student_id = login.student_login()

        if student_id:

            while True:

              print("\n========== STUDENT PANEL ==========")
              print("Welcome :", student_id)
              print("1. View Books")
              print("2. Search Book")
              print("3. View My Details")
              print("4. Logout")

              student_choice = input("Enter your choice: ")

              if student_choice == "1":
                book.view_books()

              elif student_choice == "2":
                book.search_book()

              elif student_choice == "3":
                student.view_student(student_id)

              elif student_choice == "4":
                break

              else:
                print("Invalid Choice!")