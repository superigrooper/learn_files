target = 'rec.txt'

with open(target) as f:
    file = f.read()

print(file.count(' take '))