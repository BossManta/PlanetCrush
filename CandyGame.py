from Board import Board
from Scoreboard import Scoreboard
import pygame
import math
import constants

pygame.init()

#Vars
screen = pygame.display.set_mode((constants.SCREENSIZE + int(constants.SCOREBOARDSIZE),constants.SCREENSIZE))
pygame.display.set_caption(constants.GAMENAME)
pygame.display.set_icon(constants.JUPITAR)
clock = pygame.time.Clock()
scoreBoard = Scoreboard()
currentBoard = Board(scoreBoard)
currentBoard.randomize()
running = True
clickPos = (0,0)

def update():
    global running
    global clickPos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif (event.type==1025):
            if (event.pos[0]<constants.SCREENSIZE):
                xPos = math.floor(event.pos[0]/constants.CELLSIZE)
                yPos = math.floor(event.pos[1]/constants.CELLSIZE)
                clickPos = (xPos, yPos)
        elif (event.type==1026 and currentBoard.swap1 == -1):
            if (event.pos[0]<constants.SCREENSIZE):
                xPos = math.floor(event.pos[0]/constants.CELLSIZE)
                yPos = math.floor(event.pos[1]/constants.CELLSIZE)
                xOff = xPos-clickPos[0]
                yOff = yPos-clickPos[1]
                dist = math.hypot(xOff, yOff)
                if (dist>0.5):
                    if (abs(xOff)>abs(yOff)):
                        if (xOff>0):
                            currentBoard.startSwap(clickPos[0], clickPos[1], clickPos[0]+1, clickPos[1], True)
                        else:
                            currentBoard.startSwap(clickPos[0]-1, clickPos[1], clickPos[0], clickPos[1], True)
                    else:
                        if (yOff>0):
                            currentBoard.startSwap(clickPos[0], clickPos[1], clickPos[0], clickPos[1]+1, False)
                        else:
                            currentBoard.startSwap(clickPos[0], clickPos[1]-1, clickPos[0], clickPos[1], False)

    currentBoard.update()

def draw():
    screen.fill(constants.BGCOLOR)
    currentBoard.draw(screen)
    scoreBoard.draw(screen)



while running:
    clock.tick(constants.FPS)
    update()
    draw()
    pygame.display.update()
pygame.quit()
