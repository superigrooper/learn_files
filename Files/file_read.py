# чтение всего файла

with open('pi_digit.txt') as file_object:
    contents = file_object.read()

print(contents)

# чтение по строкам

file_name = '../Classes/dog.py'

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

# создание списка из содержимого файла

lottery = '../lottery.py'

with open(lottery) as file_object:
    lines = file_object.readlines()

print(lines)
for line in lines:
    print(line.rstrip())

# создание одной строки из файла
 
with open('pi_bill.txt') as file:
     pi_line = file.readlines()

pi_str  = ''

for line in pi_line:
    pi_str += line.strip()

birthday = input("Enter date: ")
if birthday in pi_str:
    print("Yes")
else:
    print("No")