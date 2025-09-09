from collections import Counter

def unique(s):
    words = s.split()
    d = {}

    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

s = input("Enter a string: ")
print(unique(s))