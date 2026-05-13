# MINI LIBRARY SYSTEM


file_name = "Library.txt"

# Auto-initialize: create file if it doesn't exist
try:
    with open(file_name, "x") as f:
        pass  # Just create it silently
except FileExistsError:
    pass  # Already exists, no problem

while True:
    print("\n=== MINI LIBRARY ===")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Search Book")
    print("6. Exit")
    choice = input("Enter choice: ")

     # STUDENT B - Append multiple data entries (mode: a)
    if choice == "1":
        book = input("Enter book title: ")
        with open(file_name, "a") as f:
            f.write(book + "\n")
        print("Book added.") 

         # STUDENT A - Read file and print count of lines (mode: r)
    elif choice == "2":
        with open(file_name, "r") as f:
            books = f.readlines()
        if not books:
            print("Library is empty.")
        else:
            print("\nBooks in Library:")
            for i, b in enumerate(books, 1):
                print(f"  {i}. {b.strip()}")
            print(f"Total books: {len(books)}")

             # STUDENT B - Update content in the file (mode: r then w)
    elif choice == "3":
        with open(file_name, "r") as f:
            books = f.readlines()
        if not books:
            print("Library is empty.")
        else:
            for i, b in enumerate(books, 1):
                print(f"  {i}. {b.strip()}")
            try:
                num = int(input("Enter book number to update: "))
                new_book = input("Enter new title: ")
                books[num - 1] = new_book + "\n"
                with open(file_name, "w") as f:
                    f.writelines(books)
                print("Book updated.")
            except (ValueError, IndexError):
                print("Invalid number.")

                # ALL MEMBERS - Delete selected data
    elif choice == "4":
        with open(file_name, "r") as f:
            books = f.readlines()
        if not books:
            print("Library is empty.")
        else:
            for i, b in enumerate(books, 1):
                print(f"  {i}. {b.strip()}")
            try:
                num = int(input("Enter book number to delete: "))
                books.pop(num - 1)
                with open(file_name, "w") as f:
                    f.writelines(books)
                print("Book deleted.")
            except (ValueError, IndexError):
                print("Invalid number.")

    # ALL MEMBERS - Search functionality
    elif choice == "5":
        with open(file_name, "r") as f:
            books = f.readlines()
        keyword = input("Enter search keyword: ").lower()
        results = [(i + 1, b.strip()) for i, b in enumerate(books) if keyword in b.lower()]
        if results:
            print(f"\nResults for '{keyword}':")
            for num, title in results:
                print(f"  {num}. {title}")
            print(f"Found {len(results)} match(es).")
        else:
            print("No matches found.")

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")