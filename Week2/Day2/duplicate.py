names = list(input("Enter names sep by space: ").split())

unique = []
duplicates = set()

for name in names:
    if name in unique:
        duplicates.add(name)
    else:
        unique.append(name)

print("Duplicate names: ", list(duplicates))