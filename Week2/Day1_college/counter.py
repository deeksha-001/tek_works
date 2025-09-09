from collections import Counter

def count(s):

    words = s.split()

    word_count = dict(Counter(words))
    print("Word frequencies:", word_count)

string = input("Enter a string: ")
count(string)