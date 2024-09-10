#22.Write a program to check if a given number is an Armstrong number or not

num=int(input("Enter the number :"))

Number=num
sum=0
while Number>0:
    digit=Number%10
    sum+=digit **3
    Number//=10
if sum==num:
    print(num," is an Armstrong number.")
else:
    print(num,"is not an Armstrong number.")

