def string_palindrome(s):
    
    #clean_s = s.replace(" ", "").lower()
    if s == s[::-1]:
        print(s,"is a palindrome")
    else:
        print(s,"is not a palindrome")

string_palindrome("Never odd or even")