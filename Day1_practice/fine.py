days = int(input("enter days: "))

if days >= 1 and days <= 5:
    print("fine: 10")
elif days >= 6 and days <= 10:
    print("fine: 50")
elif days > 10:
    print("fine: 100")
else:
    print("no fine")