#Mouse Accuracy Trainer

import pygame
import random
import time
import math


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
screen_width, screen_height = pygame.display.get_surface().get_size()
green = (0, 128, 0)

class Dot(pygame.sprite.Sprite):

    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.color = green
        self.x = random.randint(size, screen_width - size)
        self.y = random.randint(size, screen_height - size)
        self.coordinates = (self.x, self.y)
        self.start = time.time()

    def draw(self):
        pygame.draw.circle(screen, self.color, self.coordinates, self.size)

def menu():
    pass

def game_loop(size, length):
    game_start = time.time()
    time_left = length
    spawn_time = 0
    score = 0
    sidebar_font = pygame.font.SysFont('Arial', 30)
    dots = []
    while time_left > 0:
        print(time_left)
        time_left = length - (time.time() - game_start)
        #makes screen black
        screen.fill((0, 0, 0))

        #creates dot every second
        if time.time() - game_start - 1 > spawn_time:
            spawn_time += 1
            dots.append(Dot(size))

        #draws dots
        for dot in dots:
            if time.time() - dot.start <= 4:
                dot.draw()
            elif time.time() - dot.start <= 5:
                dot.color = (255, 0, 0)
                dot.draw()
            else:
                dots.remove(dot)
                score -= 1

        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                #not my algorithm
                for dot in dots:
                    x_check = (pygame.mouse.get_pos()[0] - dot.x) ** 2
                    y_check = (pygame.mouse.get_pos()[1] - dot.y) ** 2
                    if math.sqrt(x_check + y_check) < size:
                        score += 2
                        dots.remove(dot)
                        break
                    else:
                        if dots.index(dot) == len(dots) - 1:
                            score -= 1

        #shows sidebar
        score_surface = sidebar_font.render('Score: {}'.format(score), False, green)
        time_surface = sidebar_font.render('Time Left: {}'.format(round(time_left, 1)), False, green)
        screen.blit(score_surface, (10, 10))
        screen.blit(time_surface, (10, 40))
        pygame.display.flip()

def outro():
    pass

def main():
    menu()
    game_loop(8, 60)
    outro()
    
if __name__ == '__main__':
    main()
