from utils.show_menu import show_start_menu
from user.user_signup import get_informations
from user.user_signin import user_login

def main():
    
    while True:
        show_start_menu()
        try:
            user_option = int(input('Selecione o que você deseja fazer: '))
            match user_option:
                case 1:
                    print('Informe as suas credenciais, por favor!\n')
                    get_informations()
                case 2:
                    user_login()
                case 3:
                    print('Sistema encerrando.')
                    break
                case _:
                    print('Selecione uma opção válida e tente novamente.\n')
        except:
            print('Por favor, digite somente número. Sistema encerrando.\n')
            break

main()