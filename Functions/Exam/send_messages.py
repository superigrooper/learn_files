# ver 1
def send_messages(msg):
    for message in msg:
        print(message)

messages = [
    'Красота спасет мир',
    'Сила в правде, у кого правда, тот и сильней',
    'Скоро весна'
]

send_messages(messages)

# ver 2
def send_messages_ver_2(msg, sent_msg):
    while msg:
        current_msg = msg.pop()
        print(f"\nCurrent message: {current_msg}")
        sent_msg.append(current_msg)

sent_msg = []

send_messages_ver_2(messages[:], sent_msg)
print(messages)
print(sent_msg)