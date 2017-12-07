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


def createObjects() :
    global Background, Paddle1, Paddle2, PaddleLoc,  \
        BallLoc, PlayerDirection, BallVelocity, Scores, imgBall

    # Creating 2 Paddles, a ball and background.
    Background = pygame.Surface((WIDTH, HEIGHT))
    Background.fill((0, 0, 255))
    Paddle = pygame.Surface((PADDLEW, PADDLEH))
    Paddle1 = Paddle.convert()
    Paddle1.fill((255, 255, 0))
    Paddle2 = Paddle.convert()
    Paddle2.fill((255, 0, 0))

    # some definitions
    PaddleLoc = [[BORDERMARGIN, HEIGHT/2  - PADDLEH/2.],[WIDTH-BORDERMARGIN-PADDLEW, HEIGHT/2 - PADDLEH/2.]]
    BallLoc = [WIDTH/2-8, HEIGHT/2-8]
    BallVelocity = [BALLSPEED, BALLSPEED]
    Scores = [0,0]

    imgBall = pygame.image.load("PokeBall.png")


def displayGameStatus(score, ballLoc, paddleLoc1, paddleLoc2):
    global Background, Paddle1, Paddle2, imgBall
    scoreText0 = Font.render(str(score[0]), True, (255, 255, 255))
    scoreText1 = Font.render(str(score[1]), True, (255, 255, 255))

    Screen.blit(Background, (0, 0))
    frame = pygame.draw.rect(Screen, (0, 255, 0),
                             Rect((BORDERMARGIN, BORDERMARGIN), (WIDTH - BORDERMARGIN * 2, HEIGHT - BORDERMARGIN * 2)),
                             2)
    middle_line = pygame.draw.aaline(Screen, (255, 255, 255), (WIDTH / 2, 5), (WIDTH / 2, HEIGHT - 5))
    Screen.blit(Paddle1, (paddleLoc1[0], paddleLoc1[1]))
    Screen.blit(Paddle2, (paddleLoc2[0], paddleLoc2[1]))
    Screen.blit(scoreText0, (WIDTH / 4., HEIGHT / 4.))
    Screen.blit(scoreText1, (WIDTH * 3 / 4, HEIGHT / 4))

    Screen.blit(imgBall, (ballLoc[0], ballLoc[1]))


def restrictPaddle(loc) :
    minY = BORDERMARGIN
    maxY = HEIGHT - PADDLEH - BORDERMARGIN
    if loc[1] >= maxY : loc[1] = maxY
    if loc[1] <= minY : loc[1] = minY

def setPlayer(y) :
    global PaddleLoc
    PaddleLoc[0][1] = y

def processInput() :
    global PlayerDirection

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            position = [event.pos[0], event.pos[1]]
            restrictPaddle(position)
            setPlayer(position[1])
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()


def main():
    global Background, Paddle1, Paddle2, PaddleLoc, BallLoc, BallVelocity, Scores

    init()
    createObjects()

    while True:  # Game Loop

        processInput()
        displayGameStatus(Scores, BallLoc, PaddleLoc[0], PaddleLoc[1])


        pygame.display.update()


if __name__ == '__main__':
    main()