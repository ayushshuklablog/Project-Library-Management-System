import pandas as pd

def get_reports():

    books = pd.read_csv("books.csv")
    students = pd.read_csv("students.csv")
    issued = pd.read_csv("issued_books.csv")

    return {
        "total_books": len(books),
        "total_students": len(students),
        "issued_books": len(issued)
    }