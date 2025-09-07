f = 0
s = 1
n = int(input("Enter number of terms: "))
t = 0
for i in range(n):
    print(f)
    t = f + s
    f = s
    s = t
    