l = list(map(int, input("Enter numbers: ").split()))

largest = l[0]
for i in l:
    if i > largest:
        largest = i

print("Largest number is:", largest)