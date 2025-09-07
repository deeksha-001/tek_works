
amount = float(input("enter bill: "))
if amount < 500:
    tip = 0.05
    print("tip: ", amount * tip)

elif amount >= 500 and amount <= 1000:
    tip = 0.10
    print("tip: ", amount * tip)

else:
    tip = 0.15
    print("tip: ", amount * tip)