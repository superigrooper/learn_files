from random import sample

stored = ['1', '4', 's', '3', '1', 'e', '0', '@', '2', 'Q', 'f', '&']
data = sample(stored, 4)

print(data)

my_ticket = ''
count = 0
while data != my_ticket:
    my_ticket = sample(stored, 4)
    count += 1
    print(my_ticket)

print(data, my_ticket, count)