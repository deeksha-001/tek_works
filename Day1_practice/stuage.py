#A cinema gives a 20% discount if the customer is a student and 10% discount if the customer is a senior citizen (age ≥ 60).
#Write a program that takes ticket price, age, and student status (yes/no) as input and prints the final ticket price.

ticket = float(input("enter ticket price: "))
age = int(input("enter age: "))
student = (input("Student?: (yes/no)"))

student = student.lower()

if (student == "yes"):
    discount = 0.20
    print("ticket price: ",ticket - (ticket * discount))
elif (age >= 60):
    discount = 0.10
    print("ticket price: ",ticket * discount)
else:
    print("ticket price: ",ticket)