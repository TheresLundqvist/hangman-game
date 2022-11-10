import random
from words import words
import string


def get_valid_word(words):
    """
    Get words from list of words in words.py and only use words
    without whitespaces or dash symbols.
    """
    # chooses a random word from words.py
    word = random.choice(words)
    while " " in word or "-" in word:
        word = random.choice(words)

    # returns word without - and/or whitspace
    return word.upper()


def play_game():
    """
    Main game function.
    """
    word = get_valid_word(words)
    # letters in the word saved to a set
    letters_in_word = set(word)
    alphabet = set(string.ascii_uppercase)
    # which letters the user has guessed
    guessed_letters = set()

    attempts = 10

    # get input from user as long as letters_in_word is greater then 0
    while len(letters_in_word) > 0:
        # each used letter shown as a string seperated by whitespace
        print("You have used these letters: ", " ".join(guessed_letters))

        # show correctly guessed letters in word otherwise hide letters with *
        word_list = [letter if letter in guessed_letters else "*" for letter
                     in word]
        print("The current word is: ", " ".join(word_list))

        user_input = input("Guess a letter: ").upper()
        # if user input is a valid letter and has not been used yet
        # then add the guessed letter to guessed_letter set.
        if user_input in alphabet - guessed_letters:
            guessed_letters.add(user_input)
            # if user input is correct then remove letter from letters_in_word
            if user_input in letters_in_word:
                letters_in_word.remove(user_input)

            else:
                # reduces attempts by one
                attempts = attempts - 1
                print("Letter is not in this word.")

        elif user_input in guessed_letters:
            print("Letter has already been used. Please try a new letter")

        else:
            print("Invalid character. Please try again.")

    # while loop ends here when letters_in_words == 0
