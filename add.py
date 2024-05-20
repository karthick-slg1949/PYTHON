
n = int( input("Enter the no "))
c = 0
for i in range (1, n+1):
    t = n % i
    if t == 0:
       c +=  1
if c == 2:
    print("The number is prime no")
else:
    print("The number is not prime no")