file = 'learning_python.txt'

with open(file) as file_obj:
    data = file_obj.read()
    print(data)

with open(file) as file_obj:
    for line in file_obj:
        print(line.replace('python', 'C'))

with open(file) as file_obj:
    list_data = file_obj.readlines()

print(list_data)

# запись в файл
script = 'hello.py'

with open(script, 'w') as file_object:
    file_object.write('print("hello, world")')