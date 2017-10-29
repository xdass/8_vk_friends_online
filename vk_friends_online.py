import vk
import getpass

APP_ID = 6238133  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    return input('Введите ваш логин VK: ')


def get_user_password():
    return getpass.getpass('Введите пароль: ')


def get_online_friends(login, password):
    code = """
    var online =  API.friends.getOnline({"user_id": ""});

    var result = [];
    var user = "";
    while (online.length > 0) {
        result.push(API.users.get({"user_ids": online.shift()}));
    };
    
    return result;
    """
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='offline, friends'
    )
    api = vk.API(session)
    return api.execute(code=code)


def output_friends_to_console(friends_online):
    print('Пользователи онлайн: ')
    for user in friends_online:
        print(user[0]['first_name'], user[0]['last_name'])

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
