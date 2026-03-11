# Base class
class Vehicle:
    def __init__(self, price_per_day):
        self._price_per_day = price_per_day   # Encapsulation (protected variable)

    def calculate_rent(self, days):
        return self._price_per_day * days


# Car class
class Car(Vehicle):
    def calculate_rent(self, days):
        discount = 0.10   # 10% discount
        total = self._price_per_day * days
        return total - (total * discount)


# Bike class
class Bike(Vehicle):
    def calculate_rent(self, days):
        return self._price_per_day * days   # No discount


# Truck class
class Truck(Vehicle):
    def calculate_rent(self, days):
        extra_charge = 50   # extra daily charge
        return (self._price_per_day + extra_charge) * days


# Example 
car = Car(100)
bike = Bike(40)
truck = Truck(150)

days = 3

vehicles = [car, bike, truck]

for v in vehicles:
    print(f"Rent for {v.__class__.__name__} for {days} days: {v.calculate_rent(days)}")