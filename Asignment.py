# numbers=[10,20,30,40,50,60,70,80,90]
# new_numbers=[]
# for num in numbers:
#     new_numbers.append(num*num)
# print(numbers)
# print(new_numbers)


# numbers=[10,20,30,40]
# def squreIt(num):
#     return num*num
# map_obj=map(squreIt,numbers)
# print(type(map_obj))
# print(map_obj)
# print(list(map_obj))

number=[1020,30,40,50]
new_numbers=list(map(lambda num:num*num))
print(new_numbers)