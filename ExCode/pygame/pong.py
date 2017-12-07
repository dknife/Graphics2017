import pygame
from pygame.locals import *
from sys import *
import random

WIDTH = 1200
HEIGHT = 640
PADDLEW = 20
PADDLEH = 80
BORDERMARGIN = 50


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
    global Screen, Font

    pygame.init()
    Screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    pygame.display.set_caption('Pong')

    Font = pygame.font.SysFont("freesansbold", 40)
    Logo = Font.render("MY PONG", True, (255, 255, 255))
    msg = Font.render("press any key to start", True, (255, 255, 255))
    Screen.blit(Logo, (WIDTH/2-70., HEIGHT/2-30.))
    Screen.blit(msg,  (WIDTH/2-130., HEIGHT/2+60.))

    while waitForKeyPress() == None:
        pygame.display.update()

def createObjects() :
    global Background, Paddle1, Paddle2, PaddleLoc, PaddleSpeed, \
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
    BallVelocity = [500., 500.]
    PaddleSpeed = 600.
    Scores = [0,0]

    imgBall = pygame.image.load("PokeBall.png")


def displayGameStatus(score, ballLoc, paddleLoc1, paddleLoc2) :
    global Background, Paddle1, Paddle2, Ball, imgBall
    scoreText0 = Font.render(str(score[0]), True, (255, 255, 255))
    scoreText1 = Font.render(str(score[1]), True, (255, 255, 255))
    msg = Font.render(str(ballLoc[0])+","+str(ballLoc[1]), True, (255, 255, 255))
    Screen.blit(Background, (0, 0))
    frame = pygame.draw.rect(Screen, (0, 255, 0), Rect((BORDERMARGIN,BORDERMARGIN), (WIDTH-BORDERMARGIN*2, HEIGHT-BORDERMARGIN*2)), 2)
    middle_line = pygame.draw.aaline(Screen, (255, 255, 255), (WIDTH/2, 5), (WIDTH/2, HEIGHT-5))
    Screen.blit(Paddle1, (paddleLoc1[0], paddleLoc1[1]))
    Screen.blit(Paddle2, (paddleLoc2[0], paddleLoc2[1]))
    Screen.blit(scoreText0, (WIDTH/4., HEIGHT/4.))
    Screen.blit(scoreText1, (WIDTH*3/4, HEIGHT/4))
    Screen.blit(msg, (WIDTH/2 - 200, 10))
    Screen.blit(imgBall,(ballLoc[0], ballLoc[1]))

def processInput() :
    global PlayerDirection

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

def getTimeSincePreviousFrame(clock) :
    # movement of circle
    # Clock.tick(framerate=0) -> milliseconds
    time_passed = clock.tick(150)
    time_sec = time_passed / 1000.0
    return time_sec

def MoveBall(ballPosition, velocity, dt) :
    ballPosition[0] += velocity[0]*dt
    ballPosition[1] += velocity[1]*dt


def MovePlayerPaddle(loc, updown, speed, dt) :
    loc[1] += updown*speed*dt

def MoveAI(loc, ballPos, speed, dt ):
    PaddleMove = PaddleSpeed * dt

    # AI of the computer.
    if ballPos[0] >= WIDTH/2.:
        if loc[1] < ballPos[1]:
            loc[1] += PaddleMove
        if loc[1] > ballPos[1] - PADDLEH:
            loc[1] -= PaddleMove

def restrictPaddle(loc) :
    minY = BORDERMARGIN
    maxY = HEIGHT - PADDLEH - BORDERMARGIN
    if loc[1] >= maxY : loc[1] = maxY
    if loc[1] <= minY : loc[1] = minY

def collisionHandle(player, computer, ballLoc, ballVel, scores) :

    ballWidth = 16

    # ball hits player paddle?
    if ballLoc[0] <= player[0] + PADDLEW:
        if ballLoc[1] >= player[1] - ballWidth and ballLoc[1] <= player[1] + PADDLEH:
            ballLoc[0] = player[0] + PADDLEW
            ballVel[0] = -ballVel[0]
    # ball hits computer's paddle?
    if ballLoc[0] >= computer[0] - ballWidth:
        if ballLoc[1] >= computer[1] - ballWidth and ballLoc[1] <= computer[1] + PADDLEH:
            ballLoc[0] = computer[0] - ballWidth
            ballVel[0] = -ballVel[0]

    # player missed the ball?
    if ballLoc[0] < BORDERMARGIN:
        scores[1] += 1
        ballLoc[0], ballLoc[1] = WIDTH / 2 - ballWidth / 2, HEIGHT / 2 - ballWidth / 2
        player[1] = HEIGHT/2-ballWidth/2
    elif ballLoc[0] > WIDTH-BORDERMARGIN:
        scores[0] += 1
        ballLoc[0], ballLoc[1] = WIDTH / 2 - ballWidth / 2, HEIGHT / 2 - ballWidth / 2
        computer[1] = HEIGHT/2-ballWidth/2

    # bounce at the bottom and up border
    if ballLoc[1] <= BORDERMARGIN :
        BallVelocity[1] = -BallVelocity[1]
        ballLoc[1] = BORDERMARGIN
    elif ballLoc[1] >= HEIGHT-BORDERMARGIN-ballWidth :
        BallVelocity[1] = -BallVelocity[1]
        BallLoc[1] = HEIGHT-BORDERMARGIN-ballWidth


def main() :
    global Background, Paddle1, Paddle2, PaddleLoc, PaddleSpeed, BallLoc, PlayerDirection, BallVelocity, Scores

    init()
    createObjects()

    # clock objects
    clock = pygame.time.Clock()

    PlayerDirection = 0.
    while True:  # Game Loop

        processInput()
        displayGameStatus(Scores, BallLoc, PaddleLoc[0], PaddleLoc[1])

        dt = getTimeSincePreviousFrame(clock)

        MoveBall(BallLoc, BallVelocity, dt)
        MovePlayerPaddle(PaddleLoc[0], PlayerDirection, PaddleSpeed, dt)

        MoveAI(PaddleLoc[1], BallLoc, PaddleSpeed, dt)

        restrictPaddle(PaddleLoc[0])
        restrictPaddle(PaddleLoc[1])

        collisionHandle(PaddleLoc[0], PaddleLoc[1], BallLoc, BallVelocity, Scores)


        pygame.display.update()


if __name__ == '__main__':
    main()