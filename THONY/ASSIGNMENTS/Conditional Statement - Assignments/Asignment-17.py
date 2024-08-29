# 17.Program to print max numbers in given 3 numbers ?

a=int(input("first number :"))
b=int(input("second number :"))
c=int(input("third number :"))

if(a>b and a>c):
    print("Maximum number is :",a)
    
elif(b>a and b>c):
    print("Maximum number :",b)
    
else:
    print("Maximum number is :",c)