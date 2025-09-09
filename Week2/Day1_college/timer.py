import time

def timer(n):
    for i in range(n, 0, -1):
        print(i)
        time.sleep(1)
    print("Time's up!")

num = int(input("Enter number of seconds: "))
timer(num)