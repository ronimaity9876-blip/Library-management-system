# Build a Library Management System using dictionaries  project 1 for capegemini
from add_books import add
from issue_book  import issue
from return_book import return_book
from show_books import show

def library():
    while True:
        print("Library Management System ")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Show Books")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add()
        elif choice == 2:
            issue()
        elif choice == 3:
            return_book()
        elif choice == 4:
            show()
        elif choice == 5:
            print("Thank you ")
            break
        else: 
            print("Invalid response")

library()