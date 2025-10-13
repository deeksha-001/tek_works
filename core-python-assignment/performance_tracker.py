def averages(students):
    avg_marks = {}
    for name, marks in students.items():
        if len(marks) > 0:
            avg_marks[name] = sum(marks) / len(marks)
        else:
            avg_marks[name] = 0
    return avg_marks
def top_performer(avg):
    return max(avg, key=avg.get)

students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}

avg = averages(students)
print("Average Marks:", avg)
print("Top Performer:", top_performer(avg))
