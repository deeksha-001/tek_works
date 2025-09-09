def bill():
    try:
        n = int(input("Enter number of units: "))
        if (n <= 100):
            print("Total Price: ", n * 5)
        
        elif (n <= 200):
            print("Total Price: ", 500 + (n - 100) * 7)
        
        else:
            print("Total Price: ", 1200 + (n - 200) * 10)
    
    except ValueError:
        print("Invalid Input")
    
    finally:
        print("Bill processing finished")

bill()