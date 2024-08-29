#18.Print min numbers in given 3 numbers - using Ternary Operator?

a=int(input("first number :"))
b=int(input("second number :"))
c=int(input("third number :"))
min_value = a if (a<b and a<c) else (b if b<c else c)

print('Minum number',min_value)
