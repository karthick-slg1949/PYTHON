#6.Write a program to take a single digit number from the keyboard and print in english?

Number=input("Enter the single digit number:")

if Number.isdigit() and len(Number) == 1:
    Number=int(Number)
    digit_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    print("The number is :",digit_words[Number])
else:
    print("Invalid number!.Print the single digit number")
