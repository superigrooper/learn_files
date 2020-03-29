from random import randint

class Die():
    """
    Имитация бросков кукбика.
    Side_def - количество граней
    """
    def __init__(self, sides_def=6):
        self.sides = sides_def

    def roll_die(self, number):
        """number - количество бросков"""
        while number:
            print(randint(1, self.sides))
            number -= 1

cube = Die(20)
cube.roll_die(5)