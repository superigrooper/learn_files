import json

def get_stored_username():
    """Получает имя пользователя, если оно существует."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Запрашивает имя и сохряняет в "БД" """
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username:
        answer = input(f"Your name - {username}? y/n ")
        if answer == 'y':
            print(f"Hello, {username}")
        else:
            username = get_new_username()
            print(f"{username} saved")

greet_user()