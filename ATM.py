class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def verify_pin(self, entered_pin):
        if entered_pin == self.pin:
            return True
        else:
            return False

    def check_balance(self):
        print(f"Your balance is: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")



atm = ATM(1234, 1000)

if atm.verify_pin(1234):
    atm.check_balance()
    atm.deposit(500)
    atm.withdraw(300)
    atm.check_balance()
else:
    print("Incorrect PIN")