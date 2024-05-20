import random

def guess_the_number():
    print("Welcome to Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess:"))
        attempts += 1
        if guess < secret_number:
            print("Too low. Try again!")
        elif guess > secret_number:
            print("To high. Try again!")
        else:
            print(f"congratulations! you guessed the number in {attempts} attempts.")
            break

def main():
    play_again = "yes"

    while play_again.lower() == "yes":
        guess_the_number()
        play_again = input("Do you want to play again ? (yes/no): ")
    print("Thanks for playing Guess the Number Game!")

if __name__ == "__main__":
    main()
    