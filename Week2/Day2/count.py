l = list(map(int, input("Enter all kinds of no's: ").split()))

def count(l): 
    p = 0
    z = 0
    n = 0
    for i in l:
        if i > 0:
            p += 1
        elif i < 0:
            n += 1
        else:
            z += 1
    
    print("Positive numbers:", p)
    print("Negative numbers:", n)
    print("Zeroes:", z)

count(l)