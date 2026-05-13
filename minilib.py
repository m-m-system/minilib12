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
    

