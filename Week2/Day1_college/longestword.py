def longest_word(s):
    words = s.split()
    longest = max(words, key=len)
    print("The longest word is:", longest)


string = input("Enter a string: ")
longest_word(string)