import pygame
from pygame.locals import *
from sys import *
import random



def waitForKeyPress():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        pygame.quit()
        exit()
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            pygame.quit()
            exit()
        else :
            return event.key
    return None

def init() :
    global SCREEN, FONT

    pygame.init()
    SCREEN = pygame.display.set_mode((640, 480), 0, 32)
    pygame.display.set_caption('Pong')

    FONT = pygame.font.SysFont("freesansbold", 40)
    Logo = FONT.render("MY PONG", True, (255, 255, 255))
    msg = FONT.render("press any key to start", True, (255, 255, 255))
    SCREEN.blit(Logo, (250., 210.))
    SCREEN.blit(msg, (190., 240.))

    while waitForKeyPress() == None:
        pygame.display.update()

def createObjects() :
    global Background, Paddle1, Paddle2, PaddleLoc, PaddleSpeed, \
        BallLoc, PlayerDirection, BallSpeed, Scores, imgBall

    # Creating 2 Paddles, a ball and background.
    Background = pygame.Surface((640, 480))
    Background.fill((0, 0, 255))
    Paddle = pygame.Surface((10, 50))
    Paddle1 = Paddle.convert()
    Paddle1.fill((255, 255, 0))
    Paddle2 = Paddle.convert()
    Paddle2.fill((255, 0, 0))

    # some definitions
    PaddleLoc = [[10., 215.],[620., 215.]]
    BallLoc = [307.5, 232.5]
    BallSpeed = [250., 250.]
    PaddleSpeed = 400.
    Scores = [0,0]

    imgBall = pygame.image.load("PokeBall.png")


def displayGameStatus(score, ballLoc, paddleLoc1, paddleLoc2) :
    global Background, Paddle1, Paddle2, Ball, imgBall
    scoreText0 = FONT.render(str(score[0]), True, (255, 255, 255))
    scoreText1 = FONT.render(str(score[1]), True, (255, 255, 255))
    SCREEN.blit(Background, (0, 0))
    frame = pygame.draw.rect(SCREEN, (0, 255, 0), Rect((5, 5), (630, 470)), 2)
    middle_line = pygame.draw.aaline(SCREEN, (255, 255, 255), (330, 5), (330, 475))
    SCREEN.blit(Paddle1, (paddleLoc1[0], paddleLoc1[1]))
    SCREEN.blit(Paddle2, (paddleLoc2[0], paddleLoc2[1]))
    SCREEN.blit(scoreText0, (250., 210.))
    SCREEN.blit(scoreText1, (380., 210.))
    SCREEN.blit(imgBall,(ballLoc[0], ballLoc[1]))

def main() :
    global Background, Paddle1, Paddle2, PaddleLoc, PaddleSpeed, BallLoc, PlayerDirection, BallSpeed, Scores

    init()
    createObjects()

    # clock objects
    clock = pygame.time.Clock()


    PlayerDirection = 0.
    while True:  # Game Loop

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == K_UP:
                    PlayerDirection = -1.
                elif event.key == K_DOWN:
                    PlayerDirection = 1.
            elif event.type == KEYUP:
                PlayerDirection = 0.

        displayGameStatus(Scores, BallLoc, PaddleLoc[0], PaddleLoc[1])



        # movement of circle
        # Clock.tick(framerate=0) -> milliseconds
        time_passed = clock.tick(50)
        time_sec = time_passed / 1000.0

        BallLoc[0] += BallSpeed[0] * time_sec
        BallLoc[1] += BallSpeed[1] * time_sec
        PaddleMove = PaddleSpeed * time_sec
        PaddleLoc[0][1] += PlayerDirection*PaddleMove

        # AI of the computer.
        if BallLoc[0] >= 305.:
            if not PaddleLoc[1][1] == BallLoc[1] + 7.5:
                if PaddleLoc[1][1] < BallLoc[1] + 7.5:
                    PaddleLoc[1][1] += PaddleMove
                if PaddleLoc[1][1] > BallLoc[1] - 42.5:
                    PaddleLoc[1][1] -= PaddleMove
            else:
                PaddleLoc[1][1] == BallLoc[1] + 7.5

        if PaddleLoc[0][1] >= 420.:
            PaddleLoc[0][1] = 420.
        elif PaddleLoc[0][1] <= 10.:
            PaddleLoc[0][1] = 10.
        if PaddleLoc[1][1] >= 420.:
            PaddleLoc[1][1] = 420.
        elif PaddleLoc[1][1] <= 10.:
            PaddleLoc[1][1] = 10.
        # since i don't know anything about collision, ball hitting Paddles goes like this.
        if BallLoc[0] <= PaddleLoc[0][0] + 10.:
            if BallLoc[1] >= PaddleLoc[0][1] - 7.5 and BallLoc[1] <= PaddleLoc[0][1] + 42.5:
                BallLoc[0] = 20.
                BallSpeed[0] = -BallSpeed[0]
        if BallLoc[0] >= PaddleLoc[1][0] - 15.:
            if BallLoc[1] >= PaddleLoc[1][1] - 7.5 and BallLoc[1] <= PaddleLoc[1][1] + 42.5:
                BallLoc[0] = 605.
                BallSpeed[0] = -BallSpeed[0]
        if BallLoc[0] < 5.:
            Scores[1] += 1
            BallLoc[0], BallLoc[1] = 320., 232.5
            PaddleLoc[0][1], Paddle_2_y = 215., 215.
        elif BallLoc[0] > 620.:
            Scores[0] += 1
            BallLoc[0], BallLoc[1] = 307.5, 232.5
            PaddleLoc[0][1], PaddleLoc[1][1] = 215., 215.
        if BallLoc[1] <= 10.:
            BallSpeed[1] = -BallSpeed[1]
            BallLoc[1] = 10.
        elif BallLoc[1] >= 457.5:
            BallSpeed[1] = -BallSpeed[1]
            BallLoc[1] = 457.5

        pygame.display.update()


if __name__ == '__main__':
    main()