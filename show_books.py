from utils import books

def show():
    if len(books) == 0:
        print("No books available")
    else:
        print(books)