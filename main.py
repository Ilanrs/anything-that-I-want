import pygame
import sys
import random
# import pandas as pd
from asteroid import Asteroid
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


def init():
    global AsteroidCount, Asteroids

    Player.reset((20, 200))
    Asteroids.empty()
    AsteroidCount += 3
    for i in range(AsteroidCount):
        Asteroids.add(Asteroid((random.randint(50, width -50), random.randint(50, height - 50)), random.randint(15, 60)))


def main():
    init()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Player.speed[0] = 10
            if event.key == pygame.K_LEFT:
                Player.speed[0] = -10
            if event.key == pygame.K_UP:
                Player.speed[1] = -10
            if event.key == pygame.K_DOWN:
                Player.speed[1] = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                Player.speed[0] = 0
            if event.key == pygame.K_LEFT:
                Player.speed[0] = 0
            if event.key == pygame.K_UP:
                Player.speed[1] = 0
            if event.key == pygame.K_DOWN:
                Player.speed[1] = 0

        Player.update()
        screen.fill(color)
        Asteroids.update()
        get_hits = pygame.sprite.spritecollide(Player, Asteroids, False)
        Asteroids.draw(screen)
        screen.blit(Player.image, Player.rect)
        pygame.display.flip()

        if Player.checkReset(width):
            init()
        elif get_hits:
            Player.reset((20, 200))


if __name__ == '__main__':
    main()