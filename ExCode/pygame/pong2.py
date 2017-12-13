import pygame
from pygame.locals import *
from sys import *
import math


PLAYER = 0
COMPUTER = 1

WIDTH = 1200
HEIGHT = 640
PADDLEW = 16
PADDLEH = 64


BORDERMARGIN = 50


class txtFx :
    msg = "none"
    life = 1.0
    loc = [0,0]
    vel = [0,0]
    gravity = [0,0]

    def set(self, msgStr, lifeTime, location, velocity=[0,0], g=[0,50]):
        self.msg = msgStr
        self.life = lifeTime
        self.loc = location
        self.gravity = g
        self.vel = velocity

    def show(self, screen, font, dt):
        txt = font.render(str(self.msg), True, (255, 255, 255))
        for i in range(2) :
            self.vel[i] += self.gravity[i] * dt
            self.loc[i] += self.vel[i]*dt

        screen.blit(txt, (self.loc[0], self.loc[1]))
        self.life -= dt



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
    global Screen, Font, BallSpin, Level, TextEffectSet, BallSpeed, PaddleSpeed, BoingSound, ComputerPaddleStalling, isBallMoving, TotalScore

    BallSpeed = 300
    PaddleSpeed = 200
    ComputerPaddleStalling = 1.0
    isBallMoving = True
    TotalScore = 100
    pygame.init()
    Screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    pygame.display.set_caption('Pong')

    Font = pygame.font.SysFont("freesansbold", 40)
    Logo = Font.render("MY PONG", True, (255, 255, 255))
    msg = Font.render("press any key to start", True, (255, 255, 255))
    Screen.blit(Logo, (WIDTH/2-70., HEIGHT/2-30.))
    Screen.blit(msg,  (WIDTH/2-130., HEIGHT/2+60.))
    BallSpin = 0
    Level = 1
    a = txtFx()
    a.set("Level 1: Lets Play!", 2.0, [WIDTH/2.0, HEIGHT/2.0], [0,-100], [0,300])
    print(a.msg)
    TextEffectSet = set([a])
    while waitForKeyPress() == None:
        pygame.display.update()

    BoingSound = pygame.mixer.Sound("boing_x.wav")


def createObjects() :
    global Background, Paddle1, Paddle2, previousPaddleLoc, PaddleLoc,  \
        BallLoc, BallVelocity, Scores, imgBall

    # Creating 2 Paddles, a ball and background.
    Background = pygame.Surface((WIDTH, HEIGHT))
    Background.fill((0, 0, 128))

    Paddle1 = pygame.image.load("paddle1.png")
    Paddle2 = pygame.image.load("paddle2.png")


    # some definitions
    previousPaddleLoc = [[BORDERMARGIN, HEIGHT / 2 - PADDLEH / 2.], [WIDTH - BORDERMARGIN - PADDLEW, HEIGHT / 2 - PADDLEH / 2.]]
    PaddleLoc = [[BORDERMARGIN, HEIGHT/2  - PADDLEH/2.],[WIDTH-BORDERMARGIN-PADDLEW, HEIGHT/2 - PADDLEH/2.]]
    BallLoc = [WIDTH/2-8, HEIGHT/2-8]
    BallVelocity = [BallSpeed, BallSpeed]
    Scores = [0,0]

    imgBall = pygame.image.load("PokeBall.png")


def displayGameStatus(score, ballLoc, paddleLoc1, paddleLoc2, dt) :
    global Background, Paddle1, Paddle2, imgBall, TextEffectSet, isBallMoving, Level, TotalScore

    levelText = Font.render("LEVEL: "+str(Level), True, (255, 255, 0))
    scoreText = Font.render("SCORE: " + str(TotalScore), True, (255, 255, 0))
    scoreText0 = Font.render(str(score[PLAYER]), True, (255, 255, 255))
    scoreText1 = Font.render(str(score[COMPUTER]), True, (255, 255, 255))

    Screen.blit(Background, (0, 0))
    frame = pygame.draw.rect(Screen, (0, 255, 0), Rect((BORDERMARGIN,BORDERMARGIN), (WIDTH-BORDERMARGIN*2, HEIGHT-BORDERMARGIN*2)), 2)
    middle_line = pygame.draw.aaline(Screen, (255, 255, 255), (WIDTH/2, 5), (WIDTH/2, HEIGHT-5))
    if isBallMoving is False :
        Screen.blit(Font.render("Click Mouse to Play", True, (255, 0, 0)), (WIDTH/2.0-100, HEIGHT/2.0))

    Screen.blit(Paddle1, (paddleLoc1[0], paddleLoc1[1]))
    Screen.blit(Paddle2, (paddleLoc2[0], paddleLoc2[1]))
    Screen.blit(levelText, (WIDTH / 4., 20))
    Screen.blit(scoreText, (WIDTH *3 / 4., 20))
    Screen.blit(scoreText0, (WIDTH/4., HEIGHT/4.))
    Screen.blit(scoreText1, (WIDTH*3/4, HEIGHT/4))
    Screen.blit(imgBall,(ballLoc[0], ballLoc[1]))

    removableItems = set()
    for item in TextEffectSet :
        item.show(Screen, Font, dt)
        if item.life < 0  :
            removableItems.add(item)

    for item in removableItems :
        TextEffectSet.remove(item)



def setPlayer(y) :
    global previousPaddleLoc, PaddleLoc
    previousPaddleLoc[PLAYER][1] = PaddleLoc[PLAYER][1]
    PaddleLoc[PLAYER][1] = y

def processInput() :
    global isBallMoving

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION and isBallMoving:
            position = [event.pos[0], event.pos[1]]
            restrictPaddle(position)
            setPlayer(position[1])
        if event.type == pygame.MOUSEBUTTONDOWN :
            isBallMoving = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()


def getTimeSincePreviousFrame(clock) :
    # movement of circle
    # Clock.tick(framerate=0) -> milliseconds
    time_passed = clock.tick(150)
    time_sec = time_passed / 1000.0
    return time_sec

def MoveBall(ballPosition, velocity, dt) :
    global BallSpin, TextEffectSet, isBallMoving

    if isBallMoving is not True : return

    perpendicular = [-velocity[1], velocity[0]]
    velocity[0] += perpendicular[0]*BallSpin/12000
    velocity[1] += perpendicular[1]*BallSpin /12000
    #print(TextEffectSet)
    ballPosition[0] += (velocity[0])*dt
    ballPosition[1] += (velocity[1])*dt


def MovePlayerPaddle(loc, updown, speed, dt) :
    loc[1] += updown*speed*dt


def MoveAI(prevLoc, loc, ballPos, speed, dt ):
    global PaddleSpeed, ComputerPaddleStalling, isBallMoving

    if isBallMoving is False : return

    PaddleMove = ComputerPaddleStalling*PaddleSpeed * dt

    # AI of the computer.
    prevLoc[1] = loc[1]
    if ballPos[0] >= WIDTH/2.:
        if loc[1] > ballPos[1]:
            loc[1] -= PaddleMove
        if loc[1] < ballPos[1] - PADDLEH:
            loc[1] += PaddleMove

def restrictPaddle(loc) :
    minY = BORDERMARGIN
    maxY = HEIGHT - PADDLEH - BORDERMARGIN
    if loc[1] >= maxY : loc[1] = maxY
    if loc[1] <= minY : loc[1] = minY

def increaseScore(scores, who) :
    global Level, BallSpeed, PaddleSpeed, ComputerPaddleStalling

    scores[who] += 1
    ComputerPaddleStalling = 1.0

    if who is PLAYER and scores[who]%5 is 0 :
        Level += 1
        BallSpeed *= 1.2
        PaddleSpeed *= 1.5
        if PaddleSpeed > 2.0*BallSpeed : PaddleSpeed = 2.0*BallSpeed
        levelIncreaseMsg = txtFx()
        levelIncreaseMsg.set("Level"+str(Level), 3, [WIDTH/2.0-100, HEIGHT/2.0], [0,300], [0,-300])
        TextEffectSet.add(levelIncreaseMsg)



def collisionHandle(previousPlayer, player, previousComputer, computer, ballLoc, ballVel, scores) :
    global BallSpin, BallVelocity, BoingSound, TextEffectSet, ComputerPaddleStalling, isBallMoving, TotalScore

    ballWidth = 16


    playerMove = player[1] - previousPlayer[1]
    computerMove = computer[1] - previousComputer[1]
    # ball hits player paddle?
    if ballLoc[0] < player[0] + PADDLEW:
        if ballLoc[1] >= player[1] - ballWidth and ballLoc[1] <= player[1] + PADDLEH:
            ballLoc[0] = player[0] + PADDLEW
            ballVel[0] = -ballVel[0]
            ballVel[0] *= 1.1
            BallSpin -= playerMove
            BoingSound.play()
            msg = txtFx()
            msg.set("+"+str(Level*10), 3, [ballLoc[0], ballLoc[1]], [0,100], [0,-300])
            TextEffectSet.add(msg)
            TotalScore += 10*Level
    # ball hits computer's paddle?
    if ballLoc[0] > computer[0] - ballWidth:
        if ballLoc[1] >= computer[1] - ballWidth and ballLoc[1] <= computer[1] + PADDLEH:
            ballLoc[0] = computer[0] - ballWidth
            ballVel[0] = -ballVel[0]
            ComputerPaddleStalling *= 0.8
            BallSpin += computerMove
            BoingSound.play()

    # player missed the ball?
    if ballLoc[0] < BORDERMARGIN:
        increaseScore(Scores, COMPUTER)
        ballLoc[0], ballLoc[1] = player[0]+PADDLEW, player[1]+PADDLEH/2.0
        isBallMoving = False
        BallVelocity = [BallSpeed, BallSpeed]
        BallSpin = 0.
        #player[1] = HEIGHT/2-ballWidth/2
    elif ballLoc[0] > WIDTH-BORDERMARGIN:
        increaseScore(Scores, PLAYER)
        msg = txtFx()
        msg.set("+"+str(Level*100), 3, [WIDTH/2., HEIGHT/3.0], [0,100], [0,-300])
        TextEffectSet.add(msg)
        TotalScore += Level*100
        ballLoc[0], ballLoc[1] = computer[0]-ballWidth, computer[1]+PADDLEH/2.0
        isBallMoving = False
        BallVelocity = [-BallSpeed, BallSpeed]
        BallSpin = 0.
        #computer[1] = HEIGHT/2-ballWidth/2

    # bounce at the bottom and up border
    if ballLoc[1] <= BORDERMARGIN :
        BallVelocity[1] = -BallVelocity[1]
        ballLoc[1] = BORDERMARGIN
        msg = txtFx()
        msg.set("+5", 3, [ballLoc[0], ballLoc[1]], [0, 100], [0, -300])
        TextEffectSet.add(msg)
        TotalScore += 5
    elif ballLoc[1] >= HEIGHT-BORDERMARGIN-ballWidth :
        BallVelocity[1] = -BallVelocity[1]
        BallLoc[1] = HEIGHT-BORDERMARGIN-ballWidth
        msg = txtFx()
        msg.set("+5", 3, [ballLoc[0], ballLoc[1]], [0, 100], [0, -300])
        TextEffectSet.add(msg)
        TotalScore += 5


def main() :
    global Background, Paddle1, Paddle2, previousPaddleLoc, PaddleLoc, BallLoc, BallVelocity, Scores

    init()
    createObjects()

    # clock objects
    clock = pygame.time.Clock()

    while True:  # Game Loop

        dt = getTimeSincePreviousFrame(clock)

        processInput()
        displayGameStatus(Scores, BallLoc, PaddleLoc[PLAYER], PaddleLoc[COMPUTER], dt)



        MoveBall(BallLoc, BallVelocity, dt)
        MoveAI(previousPaddleLoc[COMPUTER], PaddleLoc[COMPUTER], BallLoc, PaddleSpeed, dt)

        restrictPaddle(PaddleLoc[PLAYER])
        restrictPaddle(PaddleLoc[COMPUTER])

        collisionHandle(previousPaddleLoc[PLAYER], PaddleLoc[PLAYER], previousPaddleLoc[COMPUTER],  PaddleLoc[COMPUTER],
                        BallLoc, BallVelocity, Scores)

        pygame.display.update()


if __name__ == '__main__':
    main()