def fact(n):
    if(n == 0 or n == 1):
        print(1)
    
    else:
        print(n) * fact(n-1)

def main():
    fact(4)