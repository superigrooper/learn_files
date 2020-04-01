from get_name import get_formated_name

print("Нажми 'q' для выхода." )
while True:
    first = input("Введи имя: ")
    if first == 'q':
        break
    last = input("Введи фамилию: ")
    if last == 'q':
        break

    full_name = get_formated_name(first, last)
    print(full_name.title())