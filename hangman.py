import random
from words import words
import string
#get the computer to generate a word randomly
def get_valid_word(words):
    word = random.choice(words)  #computer will choose a random word from list "words" we imported
    #since some words have spaces and dashes within the word, this while loop will keep going until it finds a word without those
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  #letters in a word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  #what users has already guessed
    lives = 6
    #getting user input
    while len(word_letters) > 0 and lives >0:
        #tell the user what letter have been used. The " " is the space between the joined letters.
        print("You have ", lives, "lives left and have used these letters: ", " ".join(used_letters))

        #tell the user what the current status of the word
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 #take away a life if wrong
                print("Letter is not in the word.")
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
        else:
            print("You have enter an invalid character. Please try again.")

        #gets her is len(word_letter) == ) OR lives == 0
        if lives == 0:
            print("You died. The word was" , word)
        else:
            print("You guessed the word", word, "!")

hangman()