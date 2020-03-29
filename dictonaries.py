# dictonaries (словарь)
# тип данных типа ключ-значение

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}

language = favorite_languages['jen'].title()
print(f"Jen's favorite language is {language}.")

# Если попытаться вызвать несуществующее значение
# то будет ошибка. Для этого есть метод get()
# В первом аргументе передается ключ, во необязательном втором аргументе
# сообщение, которое будет возвращено, если запрашиваемого  ключа нет

not_found_key = favorite_languages.get('test_key', 'Test key not found!')
print(f"Поиск несуществующего ключа: {not_found_key}.")

# Перебор словаря целиком item() через цикл for in

print("In favorite language:\n")
for user, lang in favorite_languages.items():
    print(f"Key: {user.title()}.\nValue: {lang.title()}\n")

# перебор только ключей keys()

for keys in favorite_languages.keys():
    print(f"Dictonary keys: {keys.title()}.")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(f"{name.title()} love {favorite_languages[name].title()}.")

# проверка наличия элемента

if 'vital' not in favorite_languages.keys():
    print('Vital, take our poll!')

# перебор только значений

for val in favorite_languages.values():
    print(val.title())

# исключение повторяющихся элементов set()

for val in set(favorite_languages.values()):
    print(val.title())

# ВЛОЖЕНИЯ

# список словарей

alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 10}
alien_2 = {'color' : 'red', 'points' : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#пустой список
new_aliens = []

# создание 30-ти пришельцев
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    new_aliens.append(new_alien)

# вывод первых 5-ти
for alien in new_aliens[:5]:
    print(alien)
print("...")
print(f"Общее кол-во пришельцев: {len(new_aliens)}.")

# список в словаре

pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese']
}

print(f"Your ordered a {pizza['crust']}-crust pizza"
    " with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

languages = {
    'phil' : ['python', 'ruby'],
    'sarah' : ['c'],
    'jen' : ['python', 'javascript'],
    'den' : ['haskel']
}

for name, lang in languages.items():
    if len(lang) == 1:
        print(f"\n{name.title()} favorite language \n\t{lang[0].title()}.")
    else:
        print(f"\n{name.title()} favorite languages are:")
        for list_lang in lang:
            print(f"\t{list_lang.title()}")


# словарь в словаре

users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'prinston'
    },

    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris'
    }
}

for user, info in users.items():
    print(f"\nUsername: {user}")
    full_name = f"{info['first'].title()} {info['last'].title()}"
    location = f"{info['location'].title()}"
    print(f"\tFullname: {full_name}")
    print(f"\tLocation: {location}")

# словарь о городах

cities = {
    'saint-petersburg' : {
        'country' : 'russia',
        'population' : 5500000
        'river' : 'neva',
        'mayor' : 'beglov'
    },

    'moscow' : {
        'country' : 'russia',
        'population' : 15000000,
        'river' : 'moscow-river',
        'mayor' : 'sobyanin'
    },

    'new-york' : {
        'country' : 'usa',
        'population' : 8500000,
        'river' : 'gudson'
    }
}

