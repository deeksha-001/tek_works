def error(a,b):
    try:
        c = a/b
        print("division is: ",int(c))
    
    except ZeroDivisionError as e:
        print("Undefined. Division by zero.")
    
    
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    error(a,b)

except ValueError as e:
    print("Invalid input")