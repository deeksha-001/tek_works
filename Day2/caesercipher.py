message = input("Enter message: ")   
shift = int(input("Enter shift value: "))   

encrypted_message = ""

for char in message:
    if char.isupper():

        encrypted_message += chr((ord(char) - 65 + shift) % 26 + 65)

    elif char.islower():
        encrypted_message += chr((ord(char) - 97 + shift) % 26 + 97)

    else:
        encrypted_message += char

print("Encrypted Message:", encrypted_message)

