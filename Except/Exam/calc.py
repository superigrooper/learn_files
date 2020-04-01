print("Введи два числа или 'q' для выхода: ")

while True:
    num_1 = input()
    if num_1 == 'q':
        break

    num_2 = input()
    if num_2 == 'q':
        break

    try:
        res = int(num_1) + int(num_2)
    except ValueError:
        print("Введено не число.")
    else:
        print(res)