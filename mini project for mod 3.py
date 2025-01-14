import argparse

contacts = {}

def add_contact(identifier, name, phone, email, additional_info):
    contacts[identifier] = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Additional Info": additional_info
    }
    print(f"Added contact: {name}")

def edit_contact(identifier, name=None, phone=None, email=None, additional_info=None):
    if identifier in contacts:
        if name:
            contacts[identifier]["Name"] = name
        if phone:
            contacts[identifier]["Phone"] = phone
        if email:
            contacts[identifier]["Email"] = email
        if additional_info:
            contacts[identifier]["Additional Info"] = additional_info
        print(f"Updated contact: {identifier}")
    else:
        print(f"Contact {identifier} not found.")

def delete_contact(identifier):
    if identifier in contacts:
        del contacts[identifier]
        print(f"Deleted contact: {identifier}")
    else:
        print(f"Contact {identifier} not found.")

def search_contact(identifier):
    if identifier in contacts:
        print(f"Found contact: {contacts[identifier]}")
    else:
        print(f"Contact {identifier} not found.")

def display_contacts():
    if contacts:
        for identifier, details in contacts.items():
            print(f"{identifier}: {details}")
    else:
        print("No contacts found.")

def export_contacts(filename):
    with open(filename, 'w') as file:
        for identifier, details in contacts.items():
            file.write(f"{identifier},{details['Name']},{details['Phone']},{details['Email']},{details['Additional Info']}\n")
    print(f"Contacts exported to {filename}")

def import_contacts(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                identifier, name, phone, email, additional_info = line.strip().split(',')
                contacts[identifier] = {
                    "Name": name,
                    "Phone": phone,
                    "Email": email,
                    "Additional Info": additional_info
                }
        print(f"Contacts imported from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found.")

def main():
    while True:
        print("\nWelcome to the Contact Management System!")
        print("Menu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file *BONUS*")
        print("8. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            identifier = input("Enter unique identifier (phone/email): ")
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email address: ")
            additional_info = input("Enter additional information: ")
            add_contact(identifier, name, phone, email, additional_info)
        elif choice == '2':
            identifier = input("Enter unique identifier (phone/email): ")
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email address (leave blank to keep current): ")
            additional_info = input("Enter new additional information (leave blank to keep current): ")
            edit_contact(identifier, name, phone, email, additional_info)
        elif choice == '3':
            identifier = input("Enter unique identifier (phone/email): ")
            delete_contact(identifier)
        elif choice == '4':
            identifier = input("Enter unique identifier (phone/email): ")
            search_contact(identifier)
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            filename = input("Enter filename to export contacts: ")
            export_contacts(filename)
        elif choice == '7':
            filename = input("Enter filename to import contacts: ")
            import_contacts(filename)
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



