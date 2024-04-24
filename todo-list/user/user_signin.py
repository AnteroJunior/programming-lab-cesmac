from user.user_signup import users_list
from utils.show_menu import show_logged_menu
from task.task import *

def user_login():

    email = input('Digite seu e-mail: ')
    password = input('Digite sua senha: ')
    logged_user = None

    for user in users_list:
        if user['email'] == email and user['password'] == password:
            logged_user = user['id']
            print('\nUsuário logado com sucesso!\n')
            break

    if logged_user == None:
        print('\nCredenciais incorretas.\n')
        return
        
    user_logged(logged_user)
    
def user_logged(logged_user):
    while True:
        show_logged_menu()

        try:
            user_option = int(input('Informe a opção desejada: '))

            match user_option:
                case 1:
                    create_task(logged_user)
                
                case 2:
                    id_task = int(input('Informe o id da tarefa: '))
                    mark_as_finished(logged_user, id_task)
                
                case 3:
                    id_task = int(input('Informe o id da tarefa: '))
                    delete_from_list(logged_user, id_task)

                case 4:
                    id_task = int(input('Informe o id da tarefa: '))
                    description = input('Agora informe a nova descrição: ')
                    edit_task_description(logged_user, id_task, description)
                
                case 5:
                    list_tasks(logged_user)
                
                case 6:
                    logged_user = None
                    print('Até logo! \o')
                    break
                
                case _:
                    print('Por favor, informe uma opção válida.')
        except:
            print('Erro inesperado. Observe a opção escolhida.')
