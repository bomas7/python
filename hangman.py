import random
import string


def get_guess(word):
    guess = input('Guess a letter or a word: ')
    for i in guess:
        if i not in string.ascii_letters:
            print('Guess a LETTER or a WORD.\n')
            return get_guess(word)
    return guess

def check(guess, word):
    if guess.lower() == word:
        return 'win'
    elif len(guess) > 1:
        print('That is not the word.')
        return False
    elif guess not in word:
        print('That letter is not in the word.')
        return False
    else:
        return True

def fill_word(guess, masked_word, word):
    for i in range(word.count(guess)):
        masked_word = list(masked_word)
        masked_word[''.join(word).find(guess) + i] = guess 
        masked_word = ''.join(masked_word)
        word.remove(guess)
        print(word)
    return masked_word

def main():
    lives = 10
    with open('words.txt') as f:
        word = random.choice(f.readlines()).strip()
    masked_word = '_'*len(word)
    while True:
        if '_' not in masked_word:
            print('The word was: {}'.format(word))
            print('You win!')
            return
        print(f"The word is: {' '.join(list(masked_word))}")
        print('You currently have {} lives\n'.format(lives))
        guess = get_guess(word)
        checker = check(guess, word)
        if not checker:
            lives -= 1
        elif checker:
            masked_word = fill_word(guess, masked_word, list(word))
        if lives == 0:
            print('The word was: {}'.format(word))
            print('You lose.')
            return
        print()
        

if __name__ == '__main__':
    main()