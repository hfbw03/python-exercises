# hangman.py

import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words) # randomly chooses word from the list
    while "-" in word or " " in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_letters)
    used_letters = set() # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:

        # letters used
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

        # what current word is (ie. W - R D)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ")
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1

        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print("You died!")
    else:
        print("You guessed the word,", word, "!")

hangman()