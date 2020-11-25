# Daily Python Practise

# Hangman Game, inspired by a tutorial from Kylie Ying
# Her link ^ (https://www.youtube.com/channel/UCKMjvg6fB6WS5WrPtbV4F5g)

import random
from words_file import words
import string


def validate_word(words):
    word = random.choice(words)  # Chooses a random word in the list

    while '-' in word or ' ' in word:  # Continues until it finds a word without '-' and ' '
        word = random.choice(words)

    return word.upper()


def hangman():
    word = validate_word(words)
    word_letters = set(word)  # Each letter in the word
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()  # What the user has guessed

    lives = 10

    # Getting user input
    while len(word_letters) > 0 and lives > 0:

        # What current word is (ie W - R D)
        word_list = [
            letter if letter in guessed_letters else '-' for letter in word]
        print("\nCurrent word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: \n").upper()

        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            print("\nYou have used these letters: ", ' '.join(guessed_letters))
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1  # takes away life
                print("\nLetter is not in word. You have {} lives left".format(lives))

        elif user_letter in guessed_letters:
            print("You have already guessed that letter.\n")

        else:
            print("\nInvalid character. Please try again.\n")

    # Gets to end of the loop when the length of word letters == 0 OR when lives == 0
    if lives == 0:
        print("Sorry you died. The word was ", word)
    else:
        print("\n{} was the correct word!\n\nYAY! You won!".format(word))


if __name__ == '__main__':
    hangman()
