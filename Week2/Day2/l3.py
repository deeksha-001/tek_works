def l3(a,b,c):
    if(a>b and a>c):
        print(a," is largest")
    elif(b > a and b > c):
        print(b," is largest")
    else:
        print(c," is largest")

a = int(input("enter 1st no: "))
b = int(input("enter 2nd no: "))
c = int(input("enter 3rd no: "))

l3(a,b,c)
