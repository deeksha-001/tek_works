class Order:
    def __init__(self):
        self.items = {}
    
    def add(self, item, price):
        self.items[item] = price
    
    def remove(self, item):
        if item in self.items:
            del self.items[item]
    
    def calculate_total(self):
        return sum(self.items.values())
    
    def show_items(self):
        for item, price in self.items.items():
            print(f"{item}: {price}")

order = Order()
order.add("Shirt", 500)
order.add("Shoes", 1500)
order.show_items()
print("Total =", order.calculate_total())
order.remove("Shirt")
order.show_items()
print("Total =", order.calculate_total())
