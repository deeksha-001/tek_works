distance = int(input("Enter distance in feet: "))

feet = float(distance)
inches = feet * 12
yards = feet / 3
miles = 1760 * yards

print("Distance in feet: ", round(feet,2))
print("Distance in inches:", round(inches,2))
print("Distance in yards:", round(yards,2))
print("Distance in miles:", round(miles,2))