class Employee():
    """Модель работника."""

    def __init__(self, name, company, salary):
        """Инициализация имени, компании, оклада в год."""
        self.name = name
        self.company = company
        self.salary = salary

    def show_info(self):
        """Вывод информации о работнике."""
        name = f"{self.name.title()}"
        company = f"'{self.company.title()}'"
        salary = f"${self.salary}"
        full_info = f"Name: {name}\nCompany: {company}\nSalary: {salary}\n"
        print(full_info)

    def raise_salary(self, size_raise=5000):
        """Увеличение оклада"""
        self.salary += size_raise