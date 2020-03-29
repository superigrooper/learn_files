# имитация печати на 3-d принтере

def print_models(unprinted_design, completed_models):
    """
    Имитирует печать моделей
    пока список unprintered_design не пустой

    """
    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f"Curren design {current_design.title()}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Выводит готовые модели"""
    print("\nFollowing models has been complete: ")
    for curren_model in completed_models:
        print(f"{curren_model.title()}")

unprinted_design = ['guitar case', 'pen', 'gamepad']
completed_models = []

print_models(unprinted_design, completed_models)
show_completed_models(completed_models)

"""

Так же можно передать в функцию качестве аргумента
копию списка, для сохранения исходного:
print_models(unprinted_design[:]) 

"""