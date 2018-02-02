import random
import time


def main():
    with open("words.txt") as f_obj:
        words = [i.strip() for i in f_obj.readlines()]
    start = time.time()
    correct, total = 0, 0
    while time.time() - start < 10:
        word = random.choice(words)
        user_word = input('{}: '.format(word))
        total += 1
        if word == user_word: correct += 1
    print('You got {}/{}'.format(correct, total))
        
if __name__ == "__main__":
    main()