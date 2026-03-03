class Employee:
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def display_info(self):
        print("\nEmployee Details:")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.calculate_salary()}")


class Manager(Employee):
    def __init__(self, name, employee_id, base_salary, bonus):
        super().__init__(name, employee_id, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


class Developer(Employee):
    def __init__(self, name, employee_id, base_salary, overtime_hours, overtime_rate):
        super().__init__(name, employee_id, base_salary)
        self.overtime_hours = overtime_hours
        self.overtime_rate = overtime_rate

    def calculate_salary(self):
        overtime_pay = self.overtime_hours * self.overtime_rate
        return self.base_salary + overtime_pay



manager = Manager("Ali", 101, 5000, 1500)
developer = Developer("Sara", 102, 4000, 20, 50)

manager.display_info()
developer.display_info()