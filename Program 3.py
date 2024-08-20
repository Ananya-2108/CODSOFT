import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from the JSON file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")
    
    if name in contacts:
        print(f"Contact with the name {name} already exists.")
    else:
        contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        save_contacts(contacts)
        print(f"Contact {name} added successfully.")

def view_contacts(contacts):
    """Display all contacts."""
    if not contacts:
        print("No contacts available.")
        return
    
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"  Phone: {details['phone']}")
        print(f"  Email: {details['email']}")
        print(f"  Address: {details['address']}")
        print()

def search_contacts(contacts):
    """Search for contacts by name or phone number."""
    search_term = input("Enter name or phone number to search: ")
    found = False
    
    for name, details in contacts.items():
        if search_term in name or search_term in details['phone']:
            print(f"Name: {name}")
            print(f"  Phone: {details['phone']}")
            print(f"  Email: {details['email']}")
            print(f"  Address: {details['address']}")
            print()
            found = True
    
    if not found:
        print("No contacts found.")

def update_contact(contacts):
    """Update contact details."""
    name = input("Enter the name of the contact to update: ")
    
    if name in contacts:
        print("Leave field empty if you don't want to update it.")
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ")
        email = input(f"Enter new email (current: {contacts[name]['email']}): ")
        address = input(f"Enter new address (current: {contacts[name]['address']}): ")
        
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
        
        save_contacts(contacts)
        print(f"Contact {name} updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ")
    
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")

def main():
    """Main function to run the contact management system."""
    contacts = load_contacts()
    
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ") 
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
