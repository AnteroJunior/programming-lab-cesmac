from utils.menu import show_init_menu
from users.register import register_user
from users.authentication import login, isLogged

def main():
    user_option = 0

    while True:
        show_init_menu()
        user_option = int(input('Informe a opção que deseja: '))

        match user_option:
            case 1:
                register_user()
            case 2:
                # Fazer login
                email = input('Informe seu email: ')
                password = input('Informe a senha: ')
                if(login(email, password)):
                    isLogged()
            case 3:
                print("Saindo do sistema")
                return
main()