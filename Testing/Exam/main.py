from employee import Employee

vital = Employee('vital', 'biostar', 10000)
vital.show_info()
rust = Employee('rust', 'chnael', 8000)
rust.show_info()
vital.raise_salary()
vital.show_info()
rust.raise_salary(3000)
rust.show_info()