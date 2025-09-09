def count(s):
    vc = 0
    cc = 0
    for char in s:
        if char.lower() in 'aeiou':
            vc += 1
        elif char.isalpha():
            cc += 1

    print("Vowels:", vc)
    print("Consonants:", cc)


string = input("Enter a string: ")
count(string)