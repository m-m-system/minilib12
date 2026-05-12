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
