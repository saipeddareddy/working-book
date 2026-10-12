
# Book Management Application

books = []

print("Welcome to Book Management System")

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_name = input("Enter book name: ")
        books.append(book_name)
        print("Book added successfully!")

    elif choice == "2":
        print("\nAvailable Books:")

        if len(books) == 0:
            print("No books available.")
        else:
            for book in books:
                print("-", book)

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
