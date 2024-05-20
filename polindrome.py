def ispolindrome(s):
    return s == s[::-1]
s = "malayalam"
ans = ispolindrome(s)
if ans:
    print("Yes")
else:
        print("No")