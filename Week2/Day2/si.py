p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

def si(p, r, t):
    si = (p * r * t) / 100
    return si

print("Simple Interest is:", si(p,r,t))
print("Total amount is:", p + si(p,r,t))



