a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

total = a + b + c + d + e
percentage = (total / 500) * 100

if percentage >= 90:
    grade = 'A'
elif percentage >= 75:
    grade = 'B'
elif percentage >= 50:
    grade = 'C'

else:
    grade = 'Fail'

print("grade: ", grade)