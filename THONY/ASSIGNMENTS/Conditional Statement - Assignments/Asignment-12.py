#12.Program to print the least/small number is given two numbers?

a=int(input("First number:"))
b=int(input("Second number:"))

if(a<b):
    print(a,"is small number")
    
elif(b<a):
    print(b,"is small number")
    
else:
    print("both are equal")