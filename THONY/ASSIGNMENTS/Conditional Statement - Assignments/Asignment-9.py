#9.Program to check if a number is a 3-digit number or not?

Number=int(input("Enter the number :"))

if(Number>99 and Number<1000):
    print(Number,"is three digit number")
    
else:
    print(Number,"is not three digit number")