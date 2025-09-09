n = int(input("Enter number of pairs:"))

d = {}

for i in range(n):
    key = input("Enter name: ")
    value = float(input("Enter attendance %: "))
    d[key] = value

print(d)

for name, attendance in d.items():
    if attendance < 75:
        print(name, "is a defaulter with attendance", attendance)