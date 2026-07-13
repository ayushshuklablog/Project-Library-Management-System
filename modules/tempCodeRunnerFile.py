ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def admin_login():

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Login Successful")
        return True

    else:
        print("Invalid Username or Password")
        return False
    
import pandas as pd

def student_login():

    library_id = input("Enter Library ID: ")

    try:
        df = pd.read_csv("students.csv")

        if library_id in df["LibraryID"].values:
            print("\n✅ Login Successful")
            return library_id
        else:
            print("\n❌ Invalid Library ID")
            return None

    except FileNotFoundError:
        print("students.csv not found.")
        return None