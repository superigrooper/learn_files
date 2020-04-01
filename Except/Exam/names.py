cat = 'cat.txt'
dog = 'dog.txt'

try:
    with open(cat) as f:
        names = f.readlines()
except FileNotFoundError:
    print(f"Файл {cat} не найден.")
else:
    print(names)
    print(f"В файле {cat} есть следующие имена: ")
    for name in names:
        print(name)