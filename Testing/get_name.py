def get_formated_name(first, last, middle=''):
    """Возвращвает отформатированное имя"""
    if middle:
        return f"{first.title()} {middle.title()} {last.title()}"
    else:
        return f"{first.title()} {last.title()}"