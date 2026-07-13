from flask import Flask, render_template, request

from modules import login
from modules import book
from modules import student
from modules import issue
from modules import report


app = Flask(__name__)


# ================= HOME =================

@app.route("/")
def home():
    return render_template("index.html")



# ================= ADMIN LOGIN =================

@app.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin123":

            return render_template(
                "admin_dashboard.html"
            )

        else:
            return "<h2>Invalid Username or Password</h2>"


    return render_template("admin_login.html")



# =================================================
#                 BOOK MANAGEMENT
# =================================================


@app.route("/books")
def books():

    return render_template("books.html")



@app.route("/add_book", methods=["GET","POST"])
def add_book():

    message = ""


    if request.method == "POST":

        message = book.add_book(

            request.form["book_id"],
            request.form["title"],
            request.form["author"],
            request.form["category"],
            request.form["quantity"]

        )


    return render_template(
        "add_book.html",
        message=message
    )



@app.route("/view_books")
def view_books():

    books_data = book.view_books()


    return render_template(
        "view_books.html",
        books=books_data
    )



@app.route("/search_book", methods=["GET","POST"])
def search_book():

    result = None


    if request.method == "POST":

        result = book.search_book(
            request.form["book_id"]
        )


    return render_template(
        "search_book.html",
        result=result
    )



@app.route("/update_book", methods=["GET","POST"])
def update_book():

    message = ""


    if request.method == "POST":

        message = book.update_book(

            request.form["book_id"],
            request.form["title"],
            request.form["author"],
            request.form["category"],
            request.form["quantity"]

        )


    return render_template(
        "update_book.html",
        message=message
    )



@app.route("/delete_book", methods=["GET","POST"])
def delete_book():

    message = ""


    if request.method == "POST":

        message = book.delete_book(

            request.form["book_id"]

        )


    return render_template(
        "delete_book.html",
        message=message
    )



# =================================================
#              STUDENT MANAGEMENT
# =================================================


@app.route("/students")
def students():

    return render_template("students.html")



@app.route("/add_student", methods=["GET","POST"])
def add_student():

    message = ""


    if request.method == "POST":

        message = student.add_student(

            request.form["student_id"],
            request.form["name"],
            request.form["roll_no"],
            request.form["department"],
            request.form["year"],
            request.form["mobile"]

        )


    return render_template(
        "add_student.html",
        message=message
    )



@app.route("/view_students")
def view_students():

    students_data = student.view_students()


    return render_template(
        "view_students.html",
        students=students_data
    )



@app.route("/search_student", methods=["GET","POST"])
def search_student():

    result = None


    if request.method == "POST":

        result = student.search_student(
            request.form["student_id"]
        )


    return render_template(
        "search_student.html",
        result=result
    )



@app.route("/update_student", methods=["GET","POST"])
def update_student():

    message = ""


    if request.method == "POST":

        message = student.update_student(

            request.form["student_id"],
            request.form["name"],
            request.form["roll_no"],
            request.form["department"],
            request.form["year"],
            request.form["mobile"]

        )


    return render_template(
        "update_student.html",
        message=message
    )



@app.route("/delete_student", methods=["GET","POST"])
def delete_student():

    message = ""


    if request.method == "POST":

        message = student.delete_student(

            request.form["student_id"]

        )


    return render_template(
        "delete_student.html",
        message=message
    )



# =================================================
#              STUDENT LOGIN
# =================================================


@app.route("/student_login", methods=["GET","POST"])
def student_login():

    message = ""


    if request.method == "POST":

        success = student.student_login(

            request.form["student_id"],
            request.form["mobile"]

        )


        if success:

            return render_template(
                "student_dashboard.html"
            )

        else:

            message = "Invalid Library ID or Mobile Number"



    return render_template(
        "student_login.html",
        message=message
    )



# =================================================
#              STUDENT DASHBOARD
# =================================================


@app.route("/student_dashboard")
def student_dashboard():

    return render_template(
        "student_dashboard.html"
    )



# =================================================
#              MY ISSUED BOOKS
# =================================================


@app.route("/my_books")
def my_books():

    books = issue.view_issue()


    return render_template(
        "my_books.html",
        books=books
    )



# =================================================
#                 ISSUE BOOK
# =================================================


@app.route("/issue", methods=["GET","POST"])
def issue_book():

    message = ""


    if request.method == "POST":

        message = issue.issue_book(

            request.form["student_id"],
            request.form["book_id"]

        )


    return render_template(
        "issue.html",
        message=message
    )



# =================================================
#                 RETURN BOOK
# =================================================


@app.route("/return", methods=["GET","POST"])
def return_book():

    message = ""


    if request.method == "POST":

        message = issue.return_book(

            request.form["student_id"],
            request.form["book_id"]

        )


    return render_template(
        "return.html",
        message=message
    )



# =================================================
#                  REPORTS
# =================================================


@app.route("/reports")
def reports():

    data = report.get_reports()


    return render_template(
        "report.html",
        data=data
    )



# =================================================
#                  RUN APPLICATION
# =================================================


if __name__ == "__main__":

    app.run(debug=True)