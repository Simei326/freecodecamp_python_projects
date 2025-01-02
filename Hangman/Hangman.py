import random
import string

from words import words

def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' 'in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word)  #convert the word into a set of unique letters
    alphabet = set(string.ascii_uppercase) # provide all uppercase English letters
    used_letters = set() #an empty set initialized to keep track of the letters that the player has already guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        #what current word is (ie W _ R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters: #computes the set difference, which creates a new set containing all elements that are in alphabet but not in used-letters
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives =lives - 1
                print('Letter is not in the word.')
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again')
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print(f'Congratulations! You guessed the word: {word}')
hangman()