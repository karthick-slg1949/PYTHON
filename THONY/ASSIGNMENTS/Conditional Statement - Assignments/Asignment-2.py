#2.How to read multiple values from the keyboard in a single line?

Input_Number=input("Enter the multiple number:")
value=Input_Number.split()
numbers = [int(num) for num in value]
sum_of_numbers = sum(numbers)
print("The sum of the numbers is:", sum_of_numbers)