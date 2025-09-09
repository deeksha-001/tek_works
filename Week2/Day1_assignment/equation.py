import math

def eq(a,b,c):
    d = b**2 - 4*a*c
    if d > 0:
        r1 = (-b + math.sqrt(d)) / (2*a)
        r2 = (-b - math.sqrt(d)) / (2*a)
        return (r1, r2)
    elif d == 0:
        r = -b / (2*a)
        return (r,)
    else:
        return None
    
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
print(eq(a,b,c))