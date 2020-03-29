class User():
    """Простая модель пользователя"""

    def __init__(self, first, last, age, gender):
        self.first = first
        self.last = last
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        """Описание профиля пользователя"""
        print(f"Имя пользователя: {self.first.title()}.")
        print(f"Фамилия пользователя: {self.last.title()}.")
        print(f"Возраст: {self.age}.\nПол: {self.gender.title()}.")

    def greet_user(self):
        """Индивидуальное приветствие пользователя"""
        print(f"Приветствую, {self.first.title()}!")

    def show_login_attempts(self):
        print(f"Number logins: {self.login_attempts}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():
    """Список привелегий администратора"""

    def __init__(self):
        self.list_of_privileges = [
            'разрешено добавить сообщения',
            'разрешено удалять пользователя',
            'разрешено банить пользователя'
        ]

    def show_privileges(self):
        for item in self.list_of_privileges:
            print(f"- {item.title()}")

class Admin(User):
    """Модель администратора"""

    def __init__(self, first, last, age, gender):
        super().__init__(first, last, age, gender)
        self.privileges = Privileges()

admin = Admin('vital', 'ter', 33, 'male')
admin.describe_user()
print(admin.privileges.show_privileges())
