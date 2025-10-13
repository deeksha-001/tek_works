BASE = 50
PER_KM = 10

def fare(distance):
    return BASE + distance * PER_KM

def total_fare(trips):
    total = 0
    for i, d in enumerate(trips, 1):
        f = fare(d)
        total += f
        print(f"Trip {i}: ${f}")
    print("Total Fare: $", total)

trips = [5, 10, 3]
total_fare(trips)
