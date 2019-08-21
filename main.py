import pygame
import sys
import random
# import pandas as pd
from ship import *
# from asteroid import Asteroid
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w* 0.5), int(screen_info.current_h* 0.5))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (192, 192, 192)
screen.fill(color)

# df = pd.read_csv('game_info.csv')

Asteroids = pygame.sprite.Group()
NumLevels = 4
Level = 1
AsteroidCount = 3
Player = Ship((20, 200))


def main():
    global Level

    while Level <= NumLevels:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            screen.fill(color)
            screen.blit(Player.image, Player.rect)
            pygame.display.flip()


if __name__ == '__main__':
    main()