#Decided to rewrite hangman to based off pseudocode

'''
get word, hidden_form, lives

show hidden and lives left
get guess from user
check to see if in word
update hidden and lives
repeat until word is completely guessed or lives = 0

ask to play again
'''


import random
import string


def setup():
    with open('words.txt') as f:
        words = f.readlines()
    word = random.choice(words).strip()
    hidden = '_'*len(word)
    return word, hidden, 10

def show_status(hidden, lives):
    print('\nThe word is: {}'.format(' '.join(hidden)))
    print(f'You currently have {lives} lives left.\n')

def get_guess():
    guess = input('Guess a letter: ')
    if len(guess) == 1 and guess in string.ascii_letters:
        return guess
    print('\nGuess a LETTER\n')
    return get_guess()

def update_status(word, guess, hidden, lives):
    if guess in word:
        places = [i for i, j in enumerate(word) if j==guess]
        hidden = list(hidden)
        for i in places:
            hidden[i] = guess
    else:
        print("That letter isn't in the word")
        lives -= 1
    return ''.join(hidden), lives

def main():
    word, hidden, lives = setup()
    print(word)
    while word != hidden and lives:
        show_status(hidden, lives)
        guess = get_guess()
        hidden, lives = update_status(word, guess, hidden, lives)
    if lives == 0:
        print('You lose. The word was: {}'.format(word))
    else:
        print('You win! The word was: {}'.format(word))
    again = input('\nWould you like to play again? (y/n)')
    if again.lower() == 'y':
        main()

if __name__ == '__main__':
    main()
