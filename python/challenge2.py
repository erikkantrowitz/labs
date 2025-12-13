# Python Intermediate Challenge: Hangman Game
#
# Objective: Build a simple Hangman game where the computer picks a random word, and the player guesses letters
# one at a time. Display the word with blanks for unguessed letters, track wrong guesses, and end when the word
# is guessed or too many wrong guesses occur. Include a win/lose message and replay option.
#
# Requirements:
# - Use a list of words (hardcode 5-10 simple words).
# - Randomly select a word using random.choice().
# - Display the word as underscores initially, updating with correct guesses.
# - Track and display wrong guesses (up to 6 allowed, like hangman).
# - Handle invalid inputs (non-letters, already guessed, multiple chars).
# - Use functions to organize code (e.g., one for the game, one for display).
# - Implement replay logic.
#
# Hints:
# - Use a set for guessed letters to avoid duplicates.
# - Loop for guesses: while wrong_guesses < 6 and not word_guessed.
# - Check if letter in word: update display list.
# - For display: ''.join(display_list)
#
# Bonus: Add difficulty levels (easy/medium words), or ASCII art for hangman stages.
#
# Write your code below this comment block.

# Your code here
import random

# Global stuff 
HANGMAN_PICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

MAX_GUESSES = 6

WORD_BANK = ['void', 'faux', 'funny', 'tomb', 'fizz']

def play_game():
    secret = random.choice(WORD_BANK)
    current_guess = 0
    display_list = ['_'] * len(secret)
    
    while True:
        display_string = " ".join(display_list)
        if display_string.replace(" ","") == secret:
            break
        print(HANGMAN_PICS[current_guess])
        print(display_string)
        
        guessed_letters = set()
        guess = input('guess a letter: ').strip().lower()
        try:
            # some checks to validate guesses
            if len(guess) > 1:
                print('just guess one letter')
            if guess.isnumeric():
                print('That is a number, not a letter')
            if guess in guessed_letters:
                print(f'{guess} was already guessed, try again')
            # if the guess is valid, we check if the letter is present
            else:
                guessed_letters.add(guess)
                # string manipulation and state management
                if guess in secret:
                    print('Good guess')
                    print(secret.find(guess))
                    for i in range(len(secret)):
                        if secret[i] == guess:
                            display_list[i] = guess
                # handling a wrong guess, and game over
                else:
                    current_guess += 1
                    if current_guess == MAX_GUESSES:
                        print(HANGMAN_PICS[current_guess])
                        print("Out of guesses, Game Over")
                        break
        except:
            TypeError
            print('I didn\'t understand that')

# play and replay implementation
while True:
    play_game()
    play_again = input('play again y/n: ').strip().lower()
    if play_again == 'y':
        play_again()
    else:
        break