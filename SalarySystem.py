class Employee:
    def __init__(self, name):
        self._name = name   # Encapsulation (protected attribute)

    def calculate_salary(self):
        pass


# Full-time employee
class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self._monthly_salary = monthly_salary

    def calculate_salary(self):
        return self._monthly_salary


# Part-time employee
class PartTimeEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name)
        self._hours_worked = hours_worked
        self._hourly_rate = hourly_rate

    def calculate_salary(self):
        return self._hours_worked * self._hourly_rate


# Contract employee
class ContractEmployee(Employee):
    def __init__(self, name, contract_amount):
        super().__init__(name)
        self._contract_amount = contract_amount

    def calculate_salary(self):
        return self._contract_amount


# Example usage
employees = [
    FullTimeEmployee("Ali", 5000),
    PartTimeEmployee("Sara", 80, 20),
    ContractEmployee("Aslam", 3000)
]

for emp in employees:
    print(f"{emp._name}'s Salary: {emp.calculate_salary()}")