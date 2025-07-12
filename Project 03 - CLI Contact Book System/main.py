import sys
from file_handler import load_contact
from contact_manager import add_contact, view_contact, delete_contact, search_by
from validation import name_validity, email_validity, phone_validity

def show_menu():
    print("\n" + "="*10 + " MENU " + "="*10)
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Exit")
    print("="*26)


if __name__ == "__main__":
    print("\nWelcome to the Contact Book CLI System!")
    print("Loading contacts from contacts.csv...", end = " ")
    loaded_contacts = load_contact()
    print("Done!")
    

    while True:    
        show_menu()
        user_choice = input("Enter Your Choice: ").strip()
        print("="*26)
        
        if user_choice == "1":
            name = input("Enter Name: ").strip().lower().title()
            
            if not name_validity(name):
                print("\nError: Invalid name input! Name must contain alphabets")
                continue
            
            email = input("Enter Email: ").strip()
            
            if not email_validity(email):
                print("\nError: Invalid email input! Email must contain a valid address with valid domain")
                continue
            
            phone = input("Enter Phone Number: ").strip().replace(" ", "").replace("-", "")
            
            if not phone_validity(phone):
                print("\nError: Invalid phone number input! Phone number must contain exactly 11 digits and start with a valid Bangladeshi carrier prefix")
                continue
            
            address = input("Enter Address: ").strip().title()
            
            new_contact = {
                "name": name,
                "email": email,
                "phone": phone,
                "address": address
            }
            
            add_contact(loaded_contacts, new_contact)
            
        elif user_choice == "2":
            view_contact(loaded_contacts)
        
        elif user_choice == "3":
            entity = input("Enter search term (name/email/phone): ").strip()
            results = search_by(loaded_contacts, entity)
            if not results:
                print("\nContact not found!")
            if results:
                print("\nSearch Result:\n")
                for result in results:
                    print(f"Name: {result['name']},\nPhone: {result['phone']},\nEmail: {result['email']},\nAddress: {result['address']}\n")

        elif user_choice == "4":
            to_be_deleted = input("Enter the phone number of the contact to delete: ").strip()
            if not phone_validity(to_be_deleted):
                print("\nError: Invalid phone number input! Phone number must contain exactly 11 digits and start with a valid Bangladeshi carrier prefix")
                continue
            
            delete_contact(loaded_contacts,to_be_deleted)
                             
        elif user_choice == "5":
            sys.exit("\nThank you for using the Contact Book CLI System. Goodbye!")
        else:
            print("\nInvalid input! Try again.")