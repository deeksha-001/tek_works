def F(c):
    f = (c * 9/5) + 32
    return f

c = float(input("Enter temperature in Celsius: "))
print("Temperature in Fahrenheit:", round(F(c),2))

def C(f):
    c = (f - 32) * 5/9
    return c


f = float(input("Enter temperature in Fahrenheit: "))
print("Temperature in Celsius:", round(C(f),2))