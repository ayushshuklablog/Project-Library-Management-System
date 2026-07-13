import csv
import os

from modules import book


FILE="data/issue.csv"



# ---------------- ISSUE BOOK ----------------

def issue_book(student_id,book_id):


    if book.issue_book_update(book_id)==False:

        return "Book Not Available"



    os.makedirs("data",exist_ok=True)



    with open(FILE,"a",newline="") as f:


        writer=csv.writer(f)


        writer.writerow([

            student_id,
            book_id,
            "Issued"

        ])



    return "Book Issued Successfully"






# ---------------- VIEW ISSUES ----------------


def view_issue():


    issues=[]


    if not os.path.exists(FILE):

        return issues



    with open(FILE,"r") as f:


        reader=csv.reader(f)


        for row in reader:

            if row:

                issues.append(row)



    return issues





# ---------------- RETURN BOOK ----------------


def return_book(student_id,book_id):


    issues=[]

    found=False



    if not os.path.exists(FILE):

        return "No Issue Found"




    with open(FILE,"r") as f:


        reader=csv.reader(f)


        for row in reader:


            if row[0]==student_id and row[1]==book_id and row[2]=="Issued":


                row[2]="Returned"

                book.return_book_update(book_id)

                found=True



            issues.append(row)





    if found:


        with open(FILE,"w",newline="") as f:


            writer=csv.writer(f)


            writer.writerows(issues)



        return "Book Returned Successfully"



    return "Book Not Found"