class Dog():
    """Простая модель собаки"""

    def __init__(self, name, age):
        """Инициализирует атрибуты name и age"""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде"""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде"""
        print(f"{self.name.title()} rolled over.")

my_dog = Dog('charlie', 3)
print(f"Мою собаку зовут {my_dog.name.title()}, ему {my_dog.age} года (лет).")
my_dog.sit()
my_dog.roll_over()