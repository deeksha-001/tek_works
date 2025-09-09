class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_average(self):
        return sum(self.marks) / len(self.marks)
    
    def add_mark(self, mark):
        self.marks.append(mark)
        print(self.marks)
    
    def get_highest(self):
        return max(self.marks)
    
    def get_lowest(self):
        return min(self.marks)

s1 = Student("Deeksha", [85, 90, 78, 92])
print("Avg marks:", s1.get_average())
s1.add_mark(88)
print("Highest marks:", s1.get_highest())
print("Lowest marks:", s1.get_lowest())
