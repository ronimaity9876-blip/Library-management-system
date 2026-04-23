from utils import books,issued_books

def issue():
    book_name = input("Enter book name to issue: ").upper().strip()
    if book_name in books:
        if books[book_name] > 0:
            books[book_name] -= 1
            if book_name in issued_books:
                issued_books[book_name] += 1
            else:
                issued_books[book_name] = 1
            print(f"Book {book_name} issued successfully.")
        else:
            print(f"Sorry {book_name} is currently not available")
    else:
        print(f"this book is not available in library")
