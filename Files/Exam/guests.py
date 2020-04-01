list_of_guest = 'guests.txt'

print("Enter your name or 'q' for exit:")
while True:
    guest_name = input()
    if guest_name == 'q':
            break
    with open(list_of_guest, 'a') as file_object:
        file_object.write(f"{guest_name}\n")
        