from user.user_signup import users_list

def user_information(logged_user):
     for user in users_list:
        if user['id'] == logged_user:
            return user