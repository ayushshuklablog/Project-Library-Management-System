import csv
import os


FILE = "books.csv"



def load_books():

    books = {}


    if not os.path.exists(FILE):

        return books


    with open(FILE,"r") as f:

        reader = csv.reader(f)


        for row in reader:

            if row:

                books[row[0]] = row


    return books




def save_books(books):

    with open(FILE,"w",newline="") as f:

        writer = csv.writer(f)


        for book in books.values():

            writer.writerow(book)




# ---------------- ADD BOOK ----------------

def add_book(book_id,title,author,category,quantity):

    books = load_books()


    if book_id in books:

        return "Book Already Exists"



    books[book_id]=[

        book_id,
        title,
        author,
        category,
        quantity

    ]


    save_books(books)


    return "Book Added Successfully"





# ---------------- VIEW BOOKS ----------------

def view_books():

    return load_books()




# ---------------- SEARCH BOOK ----------------

def search_book(book_id):

    books=load_books()


    return books.get(book_id)




# ---------------- UPDATE BOOK ----------------

def update_book(book_id,title,author,category,quantity):

    books=load_books()


    if book_id not in books:

        return "Book Not Found"



    books[book_id]=[

        book_id,
        title,
        author,
        category,
        quantity

    ]


    save_books(books)


    return "Book Updated Successfully"




# ---------------- DELETE BOOK ----------------

def delete_book(book_id):

    books=load_books()


    if book_id not in books:

        return "Book Not Found"



    del books[book_id]


    save_books(books)


    return "Book Deleted Successfully"





# ---------------- REDUCE QUANTITY ----------------

def issue_book_update(book_id):

    books=load_books()


    if book_id not in books:

        return False



    quantity=int(books[book_id][4])


    if quantity <= 0:

        return False



    books[book_id][4]=str(quantity-1)


    save_books(books)


    return True





# ---------------- INCREASE QUANTITY ----------------

def return_book_update(book_id):

    books=load_books()


    if book_id not in books:

        return False



    quantity=int(books[book_id][4])


    books[book_id][4]=str(quantity+1)


    save_books(books)


    return True