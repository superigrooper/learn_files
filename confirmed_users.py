unconfirmed_users = ['alice', 'brian', 'john']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Новый пользователь: {current_user.title()}")
    confirmed_users.append(current_user)

print(f"Эти пользователи прошли проверку:")
for user in confirmed_users:
    print(user.title())

animals = ['cat', 'dog', 'pig', 'cat', 'mouse', 'rabbit']
print(animals)

while 'cat' in animals:
    animals.remove('cat')

print(animals)

responses = {}
polling_active = True

while polling_active:
    name = input("Введи своё имя: ")
    respons = input("Автомобиль какой марки проедпочитаешь? Ответ: ")
    responses[name] = respons

    repeat = input("Продолжить опрос? yes / no ")
    if repeat == 'no':
        polling_active = False

print("--- Итог ---")
for name, res in responses.items():
    print(f"{name.title()} предпочитает марку {res.title()}")