
marks = int(input("enter marks: "))

if marks >= 90 and marks <= 100:
    print("grade: A")
elif marks >= 75 and marks <= 89:
    print("grade: B")
elif marks >= 50 and marks <= 74:
    print("grade: C")
else:
    print("grade: Fail")