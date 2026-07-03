library = []


def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    isbn = input("Enter isbn number")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "issued": False
    }

    library.append(book)
    print("Book added successfully!\n")

def view_books():
    if not library:
        print("No books available.\n")
        return

    print("\nLibrary Books")
    print("-" * 50)

    for book in library:
        status = "Issued" if book["issued"] else "Available"
        print(f"ID: {book['id']}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Status: {status}")
        print("-" * 50)

def search_book():
    title = input("Enter book title to search: ")

    for book in library:
        if book["title"].lower() == title.lower():
            print("\nBook Found")
            print(book)
            return

    print("Book not found.\n")

def issue_book():
    book_id = input("Enter Book ID to issue: ")

    for book in library:
        if book["id"] == book_id:
            if not book["issued"]:
                book["issued"] = True
                print("Book issued successfully.\n")
            else:
                print("Book is already issued.\n")
            return

    print("Book not found.\n")

def return_book():
    book_id = input("Enter Book ID to return: ")

    for book in library:
        if book["id"] == book_id:
            if book["issued"]:
                book["issued"] = False
                print("Book returned successfully.\n")
            else:
                print("Book was not issued.\n")
            return

    print("Book not found.\n")

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        print("Thank you for using Library Management System.")
        break
    else:
        print("Invalid choice! Please try again.")
