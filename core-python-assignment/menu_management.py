def add_item(menu, item):
    if item not in menu:
        menu.append(item)

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)

def check_item(menu, item):
    return item in menu

menu = ["Pizza", "Burger", "Pasta", "Salad"]

add_item(menu, "Tacos")
remove_item(menu, "Salad")
print("Updated menu:", menu)

print("Pizza is available" if check_item(menu, "Pizza") else "Pizza is not available")
