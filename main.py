#####
# v. 0.0.1
# 03/26/2018
#####
import pygame
from setup import master, clock, endGameLoop, rectSettings, worldMap
from event import eventQueue

while not endGameLoop:
    #Draw current scene.
    worldMap.drawWorldMap()
    #master.sceneDict[master.sceneId].drawScene(master, rectSettings)
    #Run event and end if user quits.
    endGameLoop = eventQueue()
    #Update current scene.
    #master.sceneDict[master.sceneId].update(master, rectSettings, seasonSettings)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
