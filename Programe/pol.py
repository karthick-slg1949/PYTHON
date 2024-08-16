def  is_polindrome(s):
    return s == s[::-1]
word = input("Enter the word")
if is_polindrome(word):
    print("yes, it's a polindrome!")
else:
    print("No, it's not a polindrome.")