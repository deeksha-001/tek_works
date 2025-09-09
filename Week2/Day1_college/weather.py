import random

def weather():
    conditions = ["Sunny", "Rainy", "Cloudy", "Windy", "Snowy"]
    forecast = random.choice(conditions)
    print("Today's weather is:", forecast)
    temp = random.randint(-10, 35)
    print("Temperature is:", temp, "°C")

weather()