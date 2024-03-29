from utils.validation import validate_name, validate_email, validate_phone

usersList = []

def register_user():
    name = None
    phone = None
    email = None
    password = None

    while(name == None or not validate_name(name)):
        name = input('Informe o seu nome: ')
    
    while(phone == None or not validate_phone(phone)):
        phone = input('Informe o seu telefone: ')

    while(email == None or not validate_email(email)):
        email = input('Informe o seu email: ')

    while(password == None or len(password) < 3):
        password = input('Informe a sua senha (3 ou mais caracteres): ')

    else:
        usersList.append({
            'name': name,
            'password': password,
            'email': email,
            'phone': phone
        })
        print('Usuário cadastrado com sucesso!')