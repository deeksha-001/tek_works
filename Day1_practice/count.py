name = input("Enter name: ")

uc = 0
lc = 0

for c in name:
    if c.isupper():
        uc += 1
    elif c.islower():
        lc += 1

print("Uppercase letters:", uc)
print("Lowercase letters:", lc)