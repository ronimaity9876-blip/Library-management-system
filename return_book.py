from utils import books, issued_books

def return_book():
    book_name = input("Enter name of the book to return: ").upper().strip()
    
    if book_name in issued_books and issued_books[book_name] > 0:
        issued_books[book_name] -= 1
        if book_name in books:
            books[book_name] += 1
        else:
            books[book_name] = 1 
            
        print(f"Book '{book_name}' returned successfully.")
    else:
        print(f"book is not ours")
