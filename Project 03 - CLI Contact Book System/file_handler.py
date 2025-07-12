import os
import json

contact_file = "contacts.json"

def load_contact():
    if not os.path.exists(contact_file):
        return []
    with open(contact_file, "r") as file:
        return json.load(file)
        

def save_contact(newly_loaded_contact_file):
    with open(contact_file, "w") as file:
        json.dump(newly_loaded_contact_file, file, indent=4)
