def wd(w,b):
        if b < w:
            raise Exception("Insufficient balance")
        else:
            b = b - w
            print("Withdrawn amount: ",w)
            print("Remaining balance: ",b)
try:
    b = int(input("Enter balance: "))
    w = int(input("Enter withdraw amt: "))
    wd(w,b)

except Exception as e:
    print("error: ",e)

