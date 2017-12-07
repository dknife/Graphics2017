import pygame
from pygame.locals import *
from sys import *
import math

WIDTH = 1200
HEIGHT = 640
PADDLEW = 20
PADDLEH = 80
BALLSPEED = 300
PADDLESPEED = 500
BORDERMARGIN = 50


def waitForKeyPress():
    for event in pygame.event.get(QUIT):  # get all the QUIT events
        pygame.quit()
        exit()
    for event in pygame.event.get(KEYUP):  # get all the KEYUP events
        if event.key == K_ESCAPE:
            pygame.quit()
            exit()
        else:
            return event.key
    return None


def init():
    global Screen, Font

    pygame.init()
    Screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    pygame.display.set_caption('Pong')

    Font = pygame.font.SysFont("freesansbold", 40)
    Logo = Font.render("MY PONG", True, (255, 255, 255))
    msg = Font.render("press any key to start", True, (255, 255, 255))
    Screen.blit(Logo, (WIDTH / 2 - 70., HEIGHT / 2 - 30.))
    Screen.blit(msg, (WIDTH / 2 - 130., HEIGHT / 2 + 60.))

    while waitForKeyPress() == None:
        pygame.display.update()




def main():
    global Background, Paddle1, Paddle2, PaddleLoc, BallLoc, PlayerDirection, BallVelocity, Scores

    init()

    while True:  # Game Loop

        pygame.quit()
        exit()

        pygame.display.update()


if __name__ == '__main__':
    main()