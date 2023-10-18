class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}")
            print(f"Phone Number: {contact.phone_number}")
            print(f"Email: {contact.email}")
            print("---")

    def search_contacts(self, query):
        for contact in self.contacts:
            if query.lower() in contact.name.lower():
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print("---")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add a contact")
        print("2. View contacts")
        print("3. Search contacts")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone_number = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            contact = Contact(name, phone_number, email)
            contact_book.add_contact(contact)
            print("Contact added successfully!")

        elif choice == "2":
            print("\nContacts:")
            contact_book.view_contacts()

        elif choice == "3":
            query = input("Enter a name to search for: ")
            print("\nSearch Results:")
            contact_book.search_contacts(query)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()