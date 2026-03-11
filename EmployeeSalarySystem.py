class Employee:
    def __init__(self, name):
        self._name = name
        self._bonus = 0

    def add_bonus(self, amount):
        self._bonus += amount

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement this method")

    def apply_tax(self, salary):
        tax_rate = 0.10
        return salary - (salary * tax_rate)

    def get_name(self):
        return self._name


class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self._monthly_salary = monthly_salary

    def calculate_salary(self):
        salary = self._monthly_salary + self._bonus
        return self.apply_tax(salary)


class PartTimeEmployee(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self._hours = hours
        self._rate = rate

    def calculate_salary(self):
        salary = (self._hours * self._rate) + self._bonus
        return self.apply_tax(salary)


class ContractEmployee(Employee):
    def __init__(self, name, contract_amount):
        super().__init__(name)
        self._contract_amount = contract_amount

    def calculate_salary(self):
        salary = self._contract_amount + self._bonus
        return self.apply_tax(salary)


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def show_salaries(self):
        for emp in self.employees:
            print(f"{emp.get_name()} Salary: {emp.calculate_salary()}")


# Example 
emp1 = FullTimeEmployee("Ali", 5000)
emp2 = PartTimeEmployee("Sara", 80, 20)
emp3 = ContractEmployee("Aslam", 3000)

emp1.add_bonus(500)
emp2.add_bonus(200)
emp3.add_bonus(300)

system = EmployeeManagementSystem()

system.add_employee(emp1)
system.add_employee(emp2)
system.add_employee(emp3)

system.show_salaries()