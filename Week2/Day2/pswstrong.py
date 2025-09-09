psw = input("Enter a password: ")

if (len(psw) >= 8 and any(c.islower() for c in psw) and 
    any(c.isupper() for c in psw) and any(c.isdigit() for c in psw) and 
    any(c in '!@#$%^&*()-_+=' for c in psw)):
    print("Strong password")

else:
    print("Weak password")