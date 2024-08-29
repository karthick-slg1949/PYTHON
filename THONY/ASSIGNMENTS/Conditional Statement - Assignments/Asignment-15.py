#15.Program to print given 3 numbers in descending order?

a=int(input("first number :"))
b=int(input("second number :"))
c=int(input("third number "))

if(a>=b and a>=c):
    if(b>=c):
        print(a,b,c)
        
    else:
        print(a,c,b)
elif(b>=a and b>=c):
    if(a>=c):
        print(b,a,c)
        
    else:
        print(b,c,a)
        
else:
    if(b>=a):
        print(c,a,b)
    
    else:
        print(c,b,a)