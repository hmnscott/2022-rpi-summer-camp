# Guess the number game
import random

guesses_taken = 0

print("")
print("Hello! What is your name?")
user_name = input()

number = random.randint(1, 20)

print(f"Let's play a game {user_name}.")
print("I am thinking of a number between 1 and 20. You have 6 chances to guess what it is.")

for guesses_taken in range(1, 7):
    if guesses_taken == 1:
        guess = input("Take a guess: ")
    else:
        guess = input("Take another guess: ")

    guess = int(guess)

    if guess < number:
        print("Your guess is too low.")
    
    if guess > number:
        print("Your guess is too high.")
    
    if guess == number:
        break

if guess == number:
    print(f"Good job {user_name}! You guessed my number in {guesses_taken} guesses!")

if guess != number:
    print(f"You did not guess my number. It was {number}.")