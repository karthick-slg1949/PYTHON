#8.Write a program to find the biggest of given 3 numbers from the command prompt?
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
c=int(input("Enter the third number :"))

if(a>b and a>c):
    print(a,"is biggest number")
    
elif(b>a and b>c):
    print(b,"is biggest number")
    
else:
    print(c,"is biggest number")