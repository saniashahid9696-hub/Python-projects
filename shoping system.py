class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    # Add to cart
    def add_to_cart(self, product):
        self.items.append(product)
        print(f"{product.name} added to cart.")

    # Remove from cart
    def remove_from_cart(self, product_name):
        for product in self.items:
            if product.name == product_name:
                self.items.remove(product)
                print(f"{product_name} removed from cart.")
                return
        print(f"{product_name} not found in cart.")

    # Calculate total
    def calculate_total(self):
        total = sum(product.price for product in self.items)
        return total

    # Checkout
    def checkout(self):
        if not self.items:
            print("Cart is empty. Cannot checkout.")
            return
        
        total = self.calculate_total()
        print("\n----- Checkout -----")
        for product in self.items:
            print(f"{product.name} - ${product.price}")
        print(f"Total Amount: ${total}")
        print("Thank you for your purchase!")
        self.items.clear()


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()



p1 = Product("Laptop", 800)
p2 = Product("Headphones", 150)
p3 = Product("Mouse", 40)

customer = Customer("John")

customer.cart.add_to_cart(p1)
customer.cart.add_to_cart(p2)
customer.cart.add_to_cart(p3)

customer.cart.remove_from_cart("Mouse")
customer.cart.checkout()