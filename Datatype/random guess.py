import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0
    
    print("Welcome to Guess the number!")
    print("I have selected a number between 1 and 100.")
    print("can you guess what it is?")
    
    while guess != number_to_guess:
        guess = int(input("Enter your guess:"))
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! you guessed the number in{attempts} attempts.")
            
if __name__ == "__main__":
                guess_the_number()