n = int(input())
x = n
rev = 0

while(n !=0):
    a = n % 10
    rev = rev*10 + a
    n = n//10

if(rev == x):
    print("y")

else:
    print("n")