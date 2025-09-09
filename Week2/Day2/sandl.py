l = list(map(int, input("Enter numbers: ").split()))

def large(l):
    largest = l[0]
    for i in l:
        if i > largest:
            largest = i
    return largest

def small(l):
    smallest = l[0]
    for i in l:
        if i < smallest:
            smallest = i
    return smallest

print("Largest number is:", large(l))
print("Smallest number is:", small(l))