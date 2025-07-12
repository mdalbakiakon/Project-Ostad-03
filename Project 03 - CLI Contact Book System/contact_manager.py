import json
from file_handler import save_contact
from validation import contact_existance

def add_contact(loaded_contacts, new_contact):
    if contact_existance(loaded_contacts, new_contact):
        print("\nAdding failed! This contact is already exist in the contacts! Try again with new one")
        return
    
    loaded_contacts.append(new_contact)
    save_contact(loaded_contacts)
    print("\nContact is added in the contact file successfully!")


def view_contact(loaded_contacts):
    if not loaded_contacts:
        print("\nFile is empty! No contact found!")
        return
    
    print("\n=======All Contacts=======\n")
    
    for i, enum_contact in enumerate(loaded_contacts, start=1):
        print(
            f"{i}.Name: {enum_contact['name']},\nPhone: {enum_contact['phone']},\nEmail: {enum_contact['email']},\nAddress: {enum_contact['address']}\n"
        )


def search_by(loaded_contacts, entity):
    found = []
    
    def search_by_name(entity):
        entity = entity.lower()
        for c in loaded_contacts:
            name_list = c["name"].lower().split(" ")
            if entity in name_list:
                found.append(c)
    
    def search_by_email(entity):
        for c in loaded_contacts:
            if c["email"] == entity:
                found.append(c)
                
    def search_by_phone(entity):
        for c in loaded_contacts:
            if c["phone"] == entity:
                found.append(c)
    

    if "@" in entity: 
        search_by_email(entity)
    elif entity.replace(" ","").replace("-", "").isdigit() and len(entity.replace(" ","").replace("-", ""))==11:
        search_by_phone(entity)
    else:
        search_by_name(entity)
            
    return found



def delete_contact(loaded_contacts, to_be_deleted):
    cleaned_to_be_deleted = to_be_deleted.replace(" ", "").replace("-", "")
    
    for i, contact in enumerate(loaded_contacts):
        cleaned_contact_phone = contact["phone"]
        
        if cleaned_contact_phone == cleaned_to_be_deleted:
            user_key = input(f"Are you sure you want to delete contact with number {to_be_deleted}? (y/n): ").lower()
            if user_key == "y":
                loaded_contacts.pop(i)
                save_contact(loaded_contacts)  
                print("\nContact deleted successfully!")
                return
            else:
                print("\nDeletion cancelled")
                return
    print("\nContact not found!")