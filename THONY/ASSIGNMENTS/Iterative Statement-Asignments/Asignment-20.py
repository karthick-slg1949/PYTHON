import sys

def main():
    # Check if exactly 5 numbers are provided
    if len(sys.argv) != 6:
        print("Error: Please provide exactly 5 numbers.")
        return

    # Convert command-line arguments to integers
    try:
        numbers = [int(arg) for arg in sys.argv[1:]]
    except ValueError:
        print("Error: Please provide valid integers.")
        return

    # Print even numbers
    even_numbers = [num for num in numbers if num % 2 == 0]
    print("Even numbers:", even_numbers)

if __name__ == "__main__":
    main()
