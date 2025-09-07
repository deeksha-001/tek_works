Marks = list(map(int, input("Enter marks separated by space: ").split()))

print("Highest marks: ", max(Marks))
print("Lowest marks: ", min(Marks))
print("Average marks: ", sum(Marks)/len(Marks))