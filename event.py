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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                master.mapScrollLeft = True
            if event.key == pygame.K_RIGHT:
                master.mapScrollRight = True
            if event.key == pygame.K_UP:
                master.mapScrollUp = True
            if event.key == pygame.K_DOWN:
                master.mapScrollDown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                master.mapScrollLeft = False
            if event.key == pygame.K_RIGHT:
                master.mapScrollRight = False
            if event.key == pygame.K_UP:
                master.mapScrollUp = False
            if event.key == pygame.K_DOWN:
                master.mapScrollDown = False
#include click events here...

#Allow 'WASD' keys to move along the WorldMap
