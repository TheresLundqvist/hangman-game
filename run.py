"""
importing from python libaries
"""
import os
import random
import string
from words import words


def username():
    """
    Welcome user and get username input
    """

    username = " "
    while True:
        username = input("Welcome! Please enter a username: \n")

        if username.isalnum() is not True:
            print("Invalid character. Only letters and numbers allowed.")
            continue
        else:
            print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
            print(f"Hello {username}, you have 6 attempts to guess the "
                  "secret word.")
            input("Press the Enter key when you are ready to start the game")
            return username

    print(f"Hello {username}, you have 6 attempts to guess the "
          "secret word.")
    input("Press the Enter key when you are ready to start the game")
    return username


def clear():
    """
    Function to clear the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


def get_valid_word(words):
    """
    Get words from list of words in words.py and only allow use of
    words without whitespaces or dash symbols.
    """
    # chooses a random word from words.py
    word = random.choice(words)
    while " " in word or "-" in word:
        word = random.choice(words)

    # returns word without - and/or whitspace
    return word.upper()


def play_game():
    """
    Main game function. Allows user 6 attempts at guessing the random selected
    word. User gets to see length of corrent word masked by *. When user is
    correct the * is replaced by the correct letter. Attempts reduces as user
    is wrong. The user gets to see the secret word at the end of the game
    regardless of forfeit or success.
    """
    word = get_valid_word(words)
    # letters in the word saved to a set
    letters_in_word = set(word)
    alphabet = set(string.ascii_uppercase)
    # which letters the user has guessed
    guessed_letters = set()

    attempts = 6

    # as long as letters_in_word and attempts is greater then 0 then keep
    # asking user for input
    while len(letters_in_word) > 0 and attempts > 0:
        # shows user how many attempts they have left
        # each used letter shown as a string seperated by whitespace
        print("You have", attempts, "attempts left. You have used these "
              "letters: ", " ".join(guessed_letters))
        print()

        # show correctly guessed letters in word otherwise hide letters with *
        word_list = [letter if letter in guessed_letters else "*" for letter
                     in word]
        print("The current word is: ", " ".join(word_list))
        print()

        user_input = input("Guess a letter: ").upper()
        print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
        # if user input is a valid letter and has not been used yet
        # then add the guessed letter to guessed_letter set.
        if user_input in alphabet - guessed_letters:
            guessed_letters.add(user_input)
            clear()
            # if user input is correct then remove letter from letters_in_word
            if user_input in letters_in_word:
                letters_in_word.remove(user_input)

            else:
                # reduces attempts by one
                attempts = attempts - 1
                clear()
                print(":::: The letter is not in this word ::::")
                print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

        elif user_input in guessed_letters:
            clear()
            print(":: Letter has already been used. Please try new letter ::")
            print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

        else:
            clear()
            print(":::: Invalid character. Please try again ::::")
            print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

    # while loop ends here when letters_in_words == 0 or attempts == 0.
    if attempts == 0:
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("Oh no! Your out of attempts. The word was", word)
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

    else:
        # if user guesses the word, then print:
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("That's right! The word was", word, "!!")
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")


if __name__ == "__main__":
    clear()
    username()
    clear()
    play_game()
    while True:
        question = input("Would you like to play again? Y/N \n")
        if question.lower() == "n":
            clear()
            print("Thank you for playing hangman :) ")
            break
        elif question.lower() != "y":
            clear()
            print(f"{question} is not valid. Try again")
        else:
            clear()
            play_game()
