
months = int(input("enter months: "))
if months < 6:
    print("total price: ", 500 * months)

elif months >= 6 and months < 12:
    print("total price: ", 2700 + (500 * (months - 6)))

elif months >= 12:
    print("total price: ", 5000 + (2700 * ((months - 12) // 6)) + (500 * ((months - 12) % 6)))