class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price
        return f"{name} added"

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            return f"{name} removed"
        return f"{name} not found"

    def update_price(self, name, new_price):
        if name in self.items:
            self.items[name] = new_price
            return f"{name} price updated to {new_price}"
        return f"{name} not found"

    def show_menu(self):
        print(f"Menu: {self.items}")


menu = Menu()

print(menu.add_item("Burger", 100))
print(menu.add_item("Pizza", 200))
print(menu.update_price("Pizza", 250))
print(menu.remove_item("Burger"))
menu.show_menu()
