import pygame
from setup import endGameLoop, master

#Receive event inputs from player
def eventQueue():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endGameLoop = True
            return endGameLoop
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            master.mousePos = pygame.mouse.get_pos()

#include click events here...

#Allow 'WASD' keys to move along the WorldMap
