import math
def maths(n):
    print("Square root of", n, "is", math.sqrt(n))
    print("Factorial of", n, "is", math.factorial(n))
    print("Sine of", n, "is", math.sin(n))
    print("Cosine of", n, "is", math.cos(n))

num = int(input("Enter a number: "))
maths(num)