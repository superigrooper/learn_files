# обработка исключения ZeroDivisionError

print("Введи два числа  для деления певого на второе: ")
print("Или 'q' для выхода")

while True:
    f_num = input("\nПервое число: ")

    if f_num == 'q':
        break

    s_num = input("\nВторое число: ")

    if s_num == 'q':
        break

    try:
        answer = int(f_num) / int(s_num)
    except ZeroDivisionError:
        print("На ноль деление невозможно!")
    else:
        print(answer)

# обрботка исключения FileNotFoundError

def count_words(filename):
    """Подсчет приблизительного кол-ва слов"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"File {filename} not found.")
    else:
        words = contents.split()
        print(len(words))

files = ['confirmed_users.py', 'dictonaries.py', 'lottery.py', 'texx.txt']

for file in files:
    count_words(file)