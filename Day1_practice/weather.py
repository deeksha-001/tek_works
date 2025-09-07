temp = float(input("enter temperature: "))

if temp > 35:
    print("Too hot, stay indoors!")

elif temp >= 20 and temp <= 35:
    print("Nice weather, go out!")

else:
    print("It’s cold, wear warm clothes!")