sentence = input("Enter a sentence: ")

words = sentence.split()

no = len(sentence)

vowels = "aeiouAEIOU"

vc = 0

for char in sentence:
    if char in vowels:
        vc += 1

print("Total Words: ", len(words))
print("Total Characters: ", no)
print("Vowel count: ", vc)