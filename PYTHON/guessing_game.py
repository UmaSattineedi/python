import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    # Get the user's guess
    guess = int(input("Guess the number (between 1 and 100): "))
    attempts += 1

    # Provide hints
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        break
