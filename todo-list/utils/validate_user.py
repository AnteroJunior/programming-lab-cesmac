import re

def validate_email(email):
    if(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)):
        return True
    print('Verifique o formato do e-mail informado.')
    return False

def validate_password(password):
    if(len(password) > 6):
        return True
    print('Senha deve ter mais de 6 caracteres!')
    return False