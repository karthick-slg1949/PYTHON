# 19.Print max numbers in given 3 numbers- using Ternary Operator?

a=int(input("first number :"))
b=int(input("second number :"))
c=int(input("third number :"))

max_number=a if(a>b and a>c) else(b if b>c else c)
print("Max number :",max_number)