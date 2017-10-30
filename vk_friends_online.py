import vk
import getpass

APP_ID = 6238133  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    return input('Введите ваш логин VK: ')


def get_user_password():
    return getpass.getpass('Введите пароль: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='offline, friends'
    )
    api = vk.API(session)
    online_users = api.friends.getOnline()
    return api.users.get(user_ids=online_users)


def output_friends_to_console(friends_online):
    print('Пользователи онлайн: ')
    for user in friends_online:
        print(user['first_name'], user['last_name'])

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
