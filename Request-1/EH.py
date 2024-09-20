try:
    a=int(input('Enter the first number :'))
    b=int(input('Enter the second  number :'))
    print(a/b)
except ZeroDivisionError as e:
    print('can not divide zero')
except ValueError as  e:
    print('can not convert string to integer')