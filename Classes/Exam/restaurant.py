class Restaurant():
    """Модель описания ресторана"""
    
    def __init__(self, rest_name, cuisine_type):
        self.rest_name = rest_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_rest(self):
        """Краткое описание ресторана"""
        print(f"This is restaurant {self.rest_name.title()}.")
        print(f"It offers {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Статус работы ресторана"""
        print(f"{self.rest_name.title()} открыт.")

    def show_bumber_served(self):
        """Показывает кол-во обслуженных гостей"""
        print(f"Guest were served: {self.number_served}")

    def set_number_served(self, number):
        """Обновление кол-ва обслуженных гостей"""
        if number > 0:
            self.number_served = number
        else:
            print("Error")

    def increment_number_served(self, value_of_increment):
        """Увеличивает на заданную величину"""
        if value_of_increment > 0:
            self.number_served += value_of_increment
        else:
            print("Error")


class IceCreamStand(Restaurant):
    """Модель киоска с мороженным"""

    def __init__(self, rest_name, cuisine_type):
        """Инициализация атрибутов родителя"""
        super().__init__(rest_name, cuisine_type)
        self.flavors = [
            'cherry',
            'lemon',
            'orange',
            'banana'
        ]

    def get_flavors(self):
        """Выводит список вкусов мороженного"""
        for flavor in self.flavors:
            print(f"- {flavor}")

ice_cream = IceCreamStand('Happy Kid', 'Nice')
ice_cream.get_flavors()