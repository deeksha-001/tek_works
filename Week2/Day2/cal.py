def cal(a,b):
    print("Addition:", a+b)
    print("Subtraction:", a-b)
    print("Multiplication:", a*b)
    if b != 0:
        print("Division:", a/b)
    else:
        print("Division: Undefined (division by zero)")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

cal(a,b)