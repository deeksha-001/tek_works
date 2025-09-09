def grade(marks):
    avg = sum(marks) / len(marks)

    if avg >= 90:
        return "Grade: A+"
    elif avg >= 80:
        return "Grade: A"
    elif avg >= 70:
        return "Grade: B"
    elif avg >= 60:
        return "Grade: C"
    elif avg >= 50:
        return "Grade: D"
    else:
        return "Grade: F"

marks = list(map(int, input("Enter the marks: ").split()))
print(grade(marks))
