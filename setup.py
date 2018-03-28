import pygame
from settings import RectSettings, Master
from worldMap import WorldMap

pygame.init()

#Game Caption
pygame.display.set_caption("NimSim")

#Set Game Loop
endGameLoop = False

#Pygame Clock
clock = pygame.time.Clock()

#Initialize Settings Objects
rectSettings = RectSettings()

#Initialize Master Object to maintain game state.
master = Master()

#Initialize WorldMap Object
worldMap = WorldMap(rectSettings)
worldMap.generateRandomMap()
