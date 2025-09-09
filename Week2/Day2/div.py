def div(a,b):
    try:
        return a/b
    except Exception as e:
        print("Undefined. Division by zero.")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(div(a,b))