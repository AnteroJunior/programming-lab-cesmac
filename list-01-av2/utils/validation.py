import re

def validate_name(name):
    if(len(name) >= 3):
        return True
    return False

def validate_phone(phone):
    regex = r'\(?\d{2}\)?\s?\d{4,5}-\d{4}'
    
    if re.match(regex, phone):
        return True
    return False
    
def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(regex, email):
        return True
    return False

def checkIfEmailIsRegistered(email, users_list):
    for user in users_list:
        if(user[email] == email):
            print('Este email já está cadastrado. Tente com outro')
            return True
    return False