'''
Primitive simulaton of a voting thing
Chalie & Menny Wung
'''
import webbrowser
import json
import time
from photo import Photo

def get_photos():
    with open('photos.txt') as f:
        photos = [i.strip() for i in f.readlines()]
    return [Photo.from_str(i) for i in photos]

def intro():
    print('-----------------------------------')
    print('Welcome to the Primitive Photo Reviewer.')
    print('Using this program you can vote a rating for some photos.')
    print('You will be shown some photos, one a time through your chrome.')
    print('Then you will be asked to give a rating (on a scale 1- 10).')
    print('The ratings will be stored locally and can be viewed after you have finished voting.')
    print('Note, when the picture is shown do not be startled.')
    print('It will open up a new tab in your chrome.')
    print('-----------------------------------')
    input('Enter any key to continue: ')
    print()

def main():
    photos = get_photos()
    intro()
    for photo in photos:
        photo.print_description()
        photo.show_image()
        rating = photo.get_rating()
        photo.store_rating(rating)
    print('Ratings:')
    for photo in photos:
        print('\t{}: {}'.format(photo.name, round(photo.rating)))

if __name__ == '__main__':
    main()
