prompt = "\nВведи любое сообщение и оно выведется на экран."
prompt += "\nВведи 'quit' для выхода: "
message = ""
while message != "quit":
    message = input(prompt)
    print(message)

number = 1
while number <= 5:
    print(number)
    number = number + 1