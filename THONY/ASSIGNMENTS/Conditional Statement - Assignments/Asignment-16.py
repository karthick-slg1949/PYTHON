#16.Program to print min numbers in given 3 numbers ?

a=int(input("first number:"))
b=int(input("second number :"))
c=int(input("third number :"))

if(a<b and a<c):
    print("Minimum number is :",a)
    
elif(b<a and b<c):
    print("Minimum number is :",b)
    
else:
    print("Minimum number is",c)