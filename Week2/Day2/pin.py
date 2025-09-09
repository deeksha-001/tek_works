def pin(c,l):
    count = 0
    for i in l:
        count += 1
        if i == c:
            print("Correct PIN")
            break
        else:
                if count == 3:
                    print("Account locked")
                else:
                    print("Incorrect PIN. Try again.")
            

correct = 1234
attempts = list(map(int, input("Enter pin 3 times: ").split()))

pin(correct,attempts)