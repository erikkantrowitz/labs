# Python Beginner Challenge: Number Guessing Game
#
# Objective: Create a simple number guessing game where the computer picks a random number
# between 1 and 100, and the user has to guess it. Provide feedback like "Too high" or "Too low"
# until they guess correctly. Count the number of guesses and display it at the end.
#
# Requirements:
# - Use the random module to generate a random number.
# - Use a loop to keep asking for guesses until correct.
# - Use input() to get user guesses.
# - Convert input to integer.
# - Handle invalid inputs (non-numbers) gracefully.
#
# Hints:
# - Import random: import random
# - Generate number: secret = random.randint(1, 100)
# - Loop: while True:
# - Get guess: guess = int(input("Guess a number: "))
# - Compare and print messages.
# - Break when correct.
#
# Bonus: Add a limit on guesses, or ask if they want to play again.
#
# Write your code below this comment block.

# Your code here
import random

# game loop
def play_game():
    # generates the random number
    secret = random.randint(1,100)

    # counter for the number of guesses state
    counter = 0
    while True:
        guess = input('Guess the number from 1 - 100: ')
        try:
            guess = int(guess)
            # check for a valid guess
            if guess < 1 or guess > 100:
                print('invalid guess, try again')
                continue
            # increment guessses here
            counter += 1
            if counter > 10:
                print(f"Too many guesses, the number was {secret}")
                break
            if guess == secret:
                print(f"You got it! in {counter} tries")
                break
            elif guess > secret:
                print('Too high')
            elif guess < secret:
                print('Too low')
            # Exit if guesses are over 10

        except ValueError:
            print('I didn\'t understand that, try again')


# # Game play and replay implementation
while True:
    play_game()
    play_again = input("play again y/n: ").lower()
    if play_again == 'y':
        play_game()
    else:
        break
