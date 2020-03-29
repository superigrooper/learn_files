# позиционные аргументы передаются в порядке объявления
def animals(animal_type, animal_name):
    """Вывод информации о животном"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name.title()}.")

animals('Guinea pig', 'kansas')

# именованные аргументы
animals(animal_type='dog', animal_name='charlie')

# значения по умолчанию
def cars(brand, type='sedan'):
    print(f"This car a {brand.title()}, type {type.title()}.")

cars('Lada', 'Coupe')
cars('Lada')

# простая передача списка

def users(list):
    for user in list:
        print(f"Hello, {user.title()}")

list_of_users = ['ivan', 'jack', 'michael']

users(list_of_users)

# возвращаемое значение - словарь
def build_person(first_name, last_name, age=None):
    """Возвращает словарь"""
    person = {'first' : first_name, 'last' : last_name}
    if age:
        person['age'] = age
    return person

print(build_person('Jimi', 'Hendrix'))
print(build_person('Jimi', 'Hendrix', 27))

# форматированное имя

def get_formatted_name(first_name, last_name):
    """Возвращает аккуратно отформатированное имя"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("\n(enter 'q' at any time to quit)")

    first = input("First name: ")
    if first == 'q':
        break

    last = input("Last name: ")
    if last == 'q':
        break

    print(get_formatted_name(first, last))

