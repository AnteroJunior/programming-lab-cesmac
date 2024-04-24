import uuid
from utils.validate_user import validate_email, validate_password

users_list = []

def get_informations():
    
    email = input('Informe seu e-mail: ')
    password = input('Informe sua senha: ')
    
    print('\nÓtimo! Vamos verificar suas credenciais. Um minuto.\n')

    create_user(email, password)

def create_user(email, password):
    if validate_email(email) and validate_password(password) and not check_user_exists(email):
        users_list.append({
            'id': uuid.uuid4().hex,
            'email': email,
            'password': password,
            'tasks': []
        })

        print('\nUsuário cadastrado com sucesso! Faça login para cadastrar suas tarefas.\n')
    else:
        print('\nCredenciais com erro!\n')

def check_user_exists(email):
    exists = False
    for user in users_list:
        if user['email'] == email:
            print('\nE-mail já está sendo utilizado. Utilize outro.\n')
            exists = True
    return exists