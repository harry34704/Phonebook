class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, message=None):
        if name not in self.contacts:
            self.contacts[name] = {'phone_number': phone_number, 'message': message, 'diary': ''}
            print(f"Contact {name} added successfully.")
        else:
            print(f"Contact {name} already exists. Use update to modify details.")

    def search_contact(self, name):
        if name in self.contacts:
            contact_details = self.contacts[name]
            print(f"Name: {name}\nPhone Number: {contact_details['phone_number']}")
            if contact_details['message']:
                print(f"Message: {contact_details['message']}")
            if contact_details['diary']:
                print(f"Diary:\n{contact_details['diary']}")
        else:
            print(f"Contact {name} not found.")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} removed successfully.")
        else:
            print(f"Contact {name} not found.")

    def update_contact(self, name, phone_number, message=None, diary=None):
        if name in self.contacts:
            self.contacts[name] = {'phone_number': phone_number, 'message': message, 'diary': diary}
            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact {name} not found. Use add to create a new contact.")

    def delete_all_contacts(self):
        self.contacts = {}
        print("All contacts deleted successfully.")

    def display_contacts(self):
        if not self.contacts:
            print("Phone book is empty.")
        else:
            for name, details in self.contacts.items():
                print(f"Name: {name}\nPhone Number: {details['phone_number']}")
                if details['message']:
                    print(f"Message: {details['message']}")
                if details['diary']:
                    print(f"Diary:\n{details['diary']}")
                print("---------------")


# Welcome Message
print("Welcome to My Phone Book!")

# Main loop
phone_book = PhoneBook()

while True:
    print("\nPhone Book Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Remove Contact")
    print("4. Update Contact")
    print("5. Delete All Contacts")
    print("6. Display All Contacts")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        name = input("Enter the name: ")
        phone_number = input("Enter the phone number: ")
        message = input("Enter an optional message: ")
        diary = input("Enter an optional diary entry: ")
        phone_book.add_contact(name, phone_number, message)
        phone_book.update_contact(name, phone_number, message, diary)

    elif choice == '2':
        name = input("Enter the name to search: ")
        phone_book.search_contact(name)

    elif choice == '3':
        name = input("Enter the name to remove: ")
        phone_book.remove_contact(name)

    elif choice == '4':
        name = input("Enter the name to update: ")
        phone_number = input("Enter the new phone number: ")
        message = input("Enter the new message: ")
        diary = input("Enter an optional new diary entry: ")
        phone_book.update_contact(name, phone_number, message, diary)

    elif choice == '5':
        phone_book.delete_all_contacts()

    elif choice == '6':
        phone_book.display_contacts()

    elif choice == '7':
        print("Exiting Phone Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
