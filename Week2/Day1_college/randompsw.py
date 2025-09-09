def psw(n):
    import random
    import string

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(n))
    print("Generated password:", password)

length = int(input("Enter psw length: "))
psw(length)