

# ----------------validity checking for user input----------------
def name_validity(name):
    cleaned = name.replace(" ", "").replace(".", "").replace("-", "")
    
    if not cleaned.isalpha():
        return False
    
    if "--" in name or ".." in name or "-." in name or ".-" in name:
        return False
    if name.startswith((".", "-")) or name.endswith(("-")):
        return False
        
    return True
        

def email_validity(email):
    if email.count("@") == 1:
        user, domain = email.split("@")
        valid_suffix_for_email = (".com", ".net", ".org", ".edu", ".gov", ".io", ".co", ".us")
        if user and domain.endswith(valid_suffix_for_email) and not domain.startswith("."):
            return True
    return False
    

def phone_validity(phone):
    phone = phone.replace(" ", "").replace("-", "")
    valid_prefix_for_bangladesh = ("013", "014", "015", "016", "017", "018", "019")
    return (len(phone) == 11 and phone.isdigit() and phone.startswith(valid_prefix_for_bangladesh))



# ------------------validity for contact operation--------------------
def contact_existance(loaded_contact, new_contact):
    for existing_contact in loaded_contact:
        if existing_contact["phone"] == new_contact["phone"]:
            return True
    return False
