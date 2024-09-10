#21. Program to print Fibonacci number series up to a given number Expected Out 17: - 0 1 1 2 3 5 8 13


num=int(input("Enter the number :"))
 
n1,n2=0,1
print("Fibonacci Series:")
for i in range(1,num+1):
    print(n1)
    nextTerm=n1+n2
    n1=n2
    n2=nextTerm

       

        
    