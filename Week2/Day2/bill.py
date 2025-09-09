n = int(input("enter no of pairs: "))

d = {}

for i in range(n):
    key = input("Enter item name: ")
    value = float(input("Enter item price: "))
    d[key] = value

print(d)

total = 0
for item, price in d.items():
    total += price

print("Total bill amount: ", total)