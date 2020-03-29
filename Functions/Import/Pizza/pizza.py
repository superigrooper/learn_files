def make_pizza(size=12, *toppings):
    """Выводит описание пиццы"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")