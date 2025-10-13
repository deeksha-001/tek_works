def calculate_total(items):
    if not items:
        return 0
    total = sum(items.values())
    if len(items) > 5:
        total *= 0.9
    return total

cart = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
total = calculate_total(cart)

print("Total Price:" if total else "Cart is empty", total)