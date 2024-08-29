#11.Program to print the greatest number in given two numbers?

a=int(input("first number:"))
b=int(input("second number:"))

if(a>b):
    print(a,"is greatest number")
    
elif(b>a):
    print(b,"is greatest number")
    
else:
    print("both are equal")