import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word ]
        print('Current word: ', ''.join(word_list))

        user_letter = input('Guess a letter Baby:').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 # take away a life if wrong
                print('Oh no! That letter is not in the word. Try again')

        elif user_letter in used_letters:
            print('You have already used that charater mia pom pom. Please try again.')

        else:
            print('Invalid character. Please try again.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('Uh oh, You ran out of lives. The word was', word, 'better luck next time Baby')
    else:
        print ('YES BABY YOU DID IT! You have guessed the word', word, 'Well done!')

hangman()