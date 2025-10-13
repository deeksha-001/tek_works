marks = map(int, input("Enter the marks in C, C++, Java: ").split())

total = sum(marks)
print("Total marks:", total)

avg = total / 3
print("Average marks:", round(avg,2))


if avg >= 90:
    print("Result: Pass")
    print("Grade: A")

elif avg >= 80:
    print("Result: Pass")
    print("Grade: B")

elif avg >= 70:
    print("Result: Pass")
    print("Grade: C")

elif avg >= 60:
    print("Result: Fail")
    print("Grade: F")
    