class Employee:
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def bonus(self):
        if self.role.lower() == "manager":
            return self.salary * 0.20
        elif self.role.lower() == "developer":
            return self.salary * 0.10
        elif self.role.lower() == "intern":
            return self.salary * 0.05
        else:
            return 0


m = Employee("Alice", 50000, "Manager")
d = Employee("Bob", 40000, "Developer")
i = Employee("Charlie", 20000, "Intern")

print(m.bonus())  
print(d.bonus())  
print(i.bonus())  
