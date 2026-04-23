from utils import books 

def  add():
    book_name = input("Enter book name: ").upper()
    quantity = int(input("enter book quantity:"))
    books.update({book_name:quantity})
    print(f"book added: {book_name}")