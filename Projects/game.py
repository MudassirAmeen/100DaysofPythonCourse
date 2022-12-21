import pygame
from random import randint

#Initialise pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((400,600))

#Title and Icon
pygame.display.set_caption("Flappy Bird")
icon = pygame.image.load("flappy.png")
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("bird.png")
playerX = 50
playerY = 300
playerX_change = 0

#Pipe
pipeImg = pygame.image.load("pipe.png")
pipeX = 600
pipeY = randint(200,400)

#Score
score = 0

def player(x,y):
    screen.blit(playerImg,(x,y))

def pipe(x,y):
    screen.blit(pipeImg,(x,y))

def displayScore(score):
    font = pygame.font.Font("freesansbold.ttf",25)
    text = font.render("Score:" + str(score),True,(0,0,0))
    screen.blit(text,(10,10))

#Game loop
running = True
while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playerY_change = -3
        if event.type == pygame.KEYUP:
            playerY_change = 3

    #Check for collisions
    if playerY > 560 or playerY < 20:
        running = False
    if playerX > pipeX and playerX < pipeX + 50 and (playerY < pipeY or playerY > pipeY + 140):
        running = False

    #Movement of Bird
    playerY += playerY_change
    pipeX -= 5

    #Score
    if playerX > pipeX + 50:
        score += 1

    #Reset the pipe
    if pipeX == 0:
        pipeX = 600
        pipeY = randint(200,400)

    player(playerX,playerY)
    pipe(pipeX,pipeY)
    displayScore(score)
    pygame.display.update()