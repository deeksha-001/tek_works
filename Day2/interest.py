principal = int(input("Principal = "))
rate = float(input("Rate = "))
time = float(input("Time = "))

intresttype = input("Simple or Compound (s/c)? ")

if intresttype == 's':
    intrest = (principal * rate * time) / 100
    amount = principal + intrest
    print("Simple Intrest = {interest:.2f}".format(interest=intrest))
    print("Amount = {amount:.2f}".format(amount=amount))

elif intresttype == 'c':
    amount = principal * (pow((1 + rate / 100), time))
    intrest = amount - principal
    print("Compound Intrest = {interest:.2f}".format(interest=intrest))
    print("Amount = {amount:.2f}".format(amount=amount))
else:
    print("Invalid Input")