import time

def show(text, n=1):
    """Prints out a string character by character"""
    for i in text:
        print(i, end='')
        time.sleep(.05)
    if n == 1:
        print()

def ask(text):
    """Asks for an input character by character"""
    show(text, n=0)
    return input()
