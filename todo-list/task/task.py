from utils.show_tasks import show_user_tasks
from utils.get_user_information import user_information

def create_task(logged_user):
    task = input('Informe a descrição da tarefa: ')
    add_task_to_user(logged_user, task)
    return

def add_task_to_user(logged_user, task):
    user = user_information(logged_user)
    user['tasks'].append({
        'task': task,
        'status': 'Em andamento'
    })
    print('Tarefa adicionada com sucesso.')

def list_tasks(logged_user):
    user = user_information(logged_user)
    show_user_tasks(user['tasks'])

def mark_as_finished(logged_user, task_index):
    user = user_information(logged_user)
    user['tasks'][task_index]['status'] = 'Concluído'

def delete_from_list(logged_user, task_index):
    user = user_information(logged_user)
    del user['tasks'][task_index]

def edit_task_description(logged_user, task_index, description):
    user = user_information(logged_user)
    user['tasks'][task_index]['task'] = description