#print all prime numbers up to n

def prime(n):
    l = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            l.append(num)
            
    print(l)

num = int(input("Enter number of terms: "))
prime(num)