def show_user_tasks(tasks):

    print('+----------------------------------------------+')
    for index, task in enumerate(tasks):
        print(f'| {index} {task["task"]} ({task["status"]})')
    print('+----------------------------------------------+')