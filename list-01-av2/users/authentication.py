from utils.menu import show_logged_menu
from products.register import register_product
from products.listing import list_products
from users.register import usersList

def login(email, password):
    authenticated = 0
    for user in usersList:
        if(user['email'] == email and user['password'] == password):
            authenticated = 1
    if authenticated:
        return True
    print('Login e/ou senha inválidos.')
    return False

def isLogged():
    while True:
        show_logged_menu()
        user_option = int(input('Informe a opção: '))

        match user_option:
            case 1:
                register_product()
            case 2:
                list_products()
            case 3:
                print('Deslogando usuário')
                break
    return