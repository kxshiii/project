def print_main_menu():
    print("\nContact Book Main Menu")
    print("1. List all contacts")
    print("2. Add a new contact")
    print("3. Edit a contact")
    print("4. Delete a contact")
    print("5. List all groups")
    print("6. Add a new group")
    print("7. Assign contact to group")
    print("8. Exit")

def get_menu_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-8): "))
            if 1 <= choice <= 8:
                return choice
            else:
                print("Invalid choice. Please select a number between 1 and 8.")
        except ValueError:
            print("Invalid input. Please enter a number.")