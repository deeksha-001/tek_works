def sl(l):
    largest = l[0]
    for i in l:
        if i > largest:
            sl = largest
            largest = i

    return sl

l = list(map(int, input("Enter numbers: ").split()))
print(sl(l))