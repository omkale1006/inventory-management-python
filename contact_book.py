# contact book(python)
def display_menu():
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Show All Contacts")
    print("6. Exit")

# Initial empty contact book
contacts = {}

# Infinite loop to keep the menu running
while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact for {name} added successfully!")

    elif choice == '2':
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"Name: {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Email: {contacts[name]['email']}")
        else:
            print("Contact not found!")

    elif choice == '3':
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            contacts[name] = {"phone": phone, "email": email}
            print(f"Contact for {name} updated successfully!")
        else:
            print("Contact not found!")

    elif choice == '4':
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact for {name} deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == '5':
        if not contacts:
            print("No contacts found.")
        else:
            print("\n--- All Contacts ---")
            for name, info in contacts.items():
                print(f"\nName: {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")

    elif choice == '6':
        print("Exiting Contact Book. Dhanyavaad!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 6.")
