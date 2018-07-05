from PIL import Image, ImageDraw
import turtle
import time
import random


class Chair:

    def __init__(self, name, black_pxs=None):
        self.name = name
        if black_pxs:
            self.black_pxs = black_pxs
        else:
            self.black_pxs = []
            im = Image.open(self.name, 'r')
            black = im.convert('RGB')
            width, height = im.size
            for x in range(width):
                for y in range(height):
                    if black.getpixel((x, y)) != (255, 255, 255):
                        self.black_pxs.append((x, y))
            with open('{}.txt'.format(self.name.split('.')[0]), 'w') as f:
                f.write('{} = {}\n'.format(self.name, self.black_pxs))

    @classmethod
    def from_str(cls, str):
        name, black_pxs = str.split(' = ')
        return cls(name, eval(black_pxs.rstrip()))

    # def brush_size(self, x, y, size):
    #     points = []
    #     for i in range(1, size+1):
    #         points.append((x+i, y))
    #         points.append((x-i, y))
    #         points.append((x, y))
    #         points.append((x+i, y+i))
    #         points.append((x-i, y+i))
    #         points.append((x, y+i))
    #         points.append((x+i, y-i))
    #         points.append((x-i, y-i))
    #         points.append((x, y-i))
    #     return points
    #
    def draw(self, mode='left'):
        screen = turtle.Screen()
        screen.title(self.name.title())
        screen.screensize(750, 1000)
        drawer = turtle.Turtle()
        drawer.speed(0)
        if mode == 'random':
            random.shuffle(self.black_pxs)
        for i in self.black_pxs:
            drawer.penup()
            drawer.goto((i[0]-350, 500-i[1]))
            drawer.pendown()
            drawer.dot(1.5)



def main():
    # for creating new chair coordinates
    # new = Chair('new.jpg')
    with open('new.txt') as f:
        info = f.read()
    chair = Chair.from_str(info)
    chair.draw(mode='random')
    quit = input('')


if __name__ == '__main__':
    main()
