# переменное кол-во аргументов
def make_pizza(*toppings):
    """
    Данный синтаксис (*param) создает пустой кортеж
    и помещает в него переданное кол-во аргументов
    """
    print("\nYour pizza with:")
    for topping in toppings:
        print(f"- {topping}")
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'cheese')

# произвольный набор именованных аргументов
def build_person(first, last, **user_info):
    """
    Синтаксис (**param) создает словарь
    и помещает в него все переданные аргументы
    """
    user_info['first'] = first
    user_info['last'] = last

    return user_info

user_profile = build_person('Vital', 'Terentev-Suchkov',
            location='Saint-Petersburg',
            guitar='Gibson')

print(user_profile)
