x = int(input())
n = x
b = c = 0
while(n > 0):
    a = n % 10
    b = a*a*a
    c = c + b
    n = n//10

if(c == x):
    print("yes")

else:
    print("no")