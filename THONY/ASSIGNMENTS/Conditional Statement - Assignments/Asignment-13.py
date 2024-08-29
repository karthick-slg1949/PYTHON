#13.Program to print the greatest number in given three numbers?

a=int(input("First number"))
b=int(input("Second number:"))
c=int(input("Third number:"))

if(a>b and a>c):
    print(a,"is greatest number")
    
elif(b>a and b>c):
    print(b,"is greatest number")
    
else:
    print(c,"is greatest number")