
def fib(n):
    f = 0
    s = 1
    l = []
    for i in range(n):
        l.append(f)
        t = f + s
        f = s
        s = t
    return l
    
n = int(input("Enter a integer: "))
print(fib(n))