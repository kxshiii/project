from .menu import print_main_menu, get_menu_choice
from contact_book_orm.models.password import PasswordManager

contacts = []
groups = []

def list_all_contacts():
    print("Listing all contacts...")
    if not contacts:
        print("No contacts found.")
    else:
        for idx, c in enumerate(contacts, 1):
            group_name = c.get("group", "None")
            print(f"{idx}. {c['first_name']} {c['last_name']} - {c['email']} - {c['phone']} - Group: {group_name}")

def add_new_contact():
    print("Adding a new contact...")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    set_password = input("Do you want to set a password for this contact? (y/n): ").strip().lower()
    if set_password == 'y':
        password = input("Enter password: ")
    else:
        password = PasswordManager.generate_password()
        print(f"Auto-generated password: {password}")
    salt, pwd_hash = PasswordManager.hash_password(password)
    contact = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
        "group": None,
        "password_salt": salt.hex(),
        "password_hash": pwd_hash.hex()
    }
    contacts.append(contact)
    print(f"Contact added: {first_name} {last_name}, Email: {email}, Phone: {phone}")

def edit_contact():
    print("Editing a contact...")
    if not contacts:
        print("No contacts to edit.")
        return
    list_all_contacts()
    try:
        idx = int(input("Enter the number of the contact to edit: ")) - 1
        if 0 <= idx < len(contacts):
            contact = contacts[idx]
            print("Leave blank to keep current value.")
            first_name = input(f"First name [{contact['first_name']}]: ") or contact['first_name']
            last_name = input(f"Last name [{contact['last_name']}]: ") or contact['last_name']
            email = input(f"Email [{contact['email']}]: ") or contact['email']
            phone = input(f"Phone [{contact['phone']}]: ") or contact['phone']
            contact.update({
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone": phone
            })
            print("Contact updated.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

def delete_contact():
    print("Deleting a contact...")
    if not contacts:
        print("No contacts to delete.")
        return
    list_all_contacts()
    try:
        idx = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= idx < len(contacts):
            removed = contacts.pop(idx)
            print(f"Deleted contact: {removed['first_name']} {removed['last_name']}")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

def list_all_groups():
    print("Listing all groups...")
    if not groups:
        print("No groups found.")
    else:
        for idx, g in enumerate(groups, 1):
            print(f"{idx}. {g['name']} - {g.get('description', '')}")

def add_new_group():
    print("Adding a new group...")
    name = input("Group name: ")
    description = input("Description: ")
    group = {
        "name": name,
        "description": description
    }
    groups.append(group)
    print(f"Group added: {name}")

def assign_contact_to_group():
    print("Assigning contact to group...")
    if not contacts:
        print("No contacts available.")
        return
    if not groups:
        print("No groups available.")
        return
    list_all_contacts()
    try:
        c_idx = int(input("Enter the number of the contact to assign: ")) - 1
        if 0 <= c_idx < len(contacts):
            list_all_groups()
            g_idx = int(input("Enter the number of the group: ")) - 1
            if 0 <= g_idx < len(groups):
                contacts[c_idx]["group"] = groups[g_idx]["name"]
                print(f"Assigned {contacts[c_idx]['first_name']} {contacts[c_idx]['last_name']} to group {groups[g_idx]['name']}.")
            else:
                print("Invalid group number.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

def main():
    while True:
        print_main_menu()
        choice = get_menu_choice()
        if choice == 1:
            list_all_contacts()
        elif choice == 2:
            add_new_contact()
        elif choice == 3:
            edit_contact()
        elif choice == 4:
            delete_contact()
        elif choice == 5:
            list_all_groups()
        elif choice == 6:
            add_new_group()
        elif choice == 7:
            assign_contact_to_group()
        elif choice == 8:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()