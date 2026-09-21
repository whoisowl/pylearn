from mylibrary.library import Library


if __name__ == "__main__":
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add book")
        print("2. Remove book")
        print("3. Search book")
        print("4. Show all books")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")

            library.add_book(title, author)
            print("Book added successfully!")

        elif choice == "2":
            title = input("Enter the title to remove: ")

            library.remove_book(title)
            print("Book removed successfully!")

        elif choice == "3":
            title = input("Enter the title to search: ")

            book = library.search_book(title)

            if book:
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")

        elif choice == "4":
            books = library.show_books()

            if books:
                for book in books:
                    print(f"Title: {book['title']} | Author: {book['author']}")
            else:
                print("The library is empty.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")