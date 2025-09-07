pin = int(input("PIN = "))
balance = int(input("Balance = "))
withdraw = int(input("Withdraw = "))

if pin == 1234:
    if withdraw <= balance:
        balance -= withdraw
        print("PIN verified")
        print("Withdraw successful")
        print("Remaining balance = ", balance)


else:
    print("Invalid PIN")