def bill(n):
    
    if n <=100:
        print("price: ", n * 5)
    
    elif n <= 200:
        print("price: ", 500 + (n - 100) * 7)

    else:
        print("price: ", 1200 + (n - 300) * 10)


n = int(input("Enter number of units: "))
bill(n)
