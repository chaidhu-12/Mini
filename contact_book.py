
import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added!")

# View all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")

# Search for a contact
def search_contact():
    keyword = input("Enter name to search: ").lower()
    found = [c for c in contacts if keyword in c['name'].lower()]
    if not found:
        print("No matching contacts.")
    else:
        for contact in found:
            print(f"{contact['name']} | {contact['phone']} | {contact['email']}")

# Delete a contact
def delete_contact():
    view_contacts()
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        removed = contacts.pop(index)
        save_contacts(contacts)
        print(f"Deleted: {removed['name']}")
    except (IndexError, ValueError):
        print("Invalid contact number.")

# Main menu
def menu():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
contacts = load_contacts()
menu()
