import pygame
from math import sqrt
import random

class MapLocation():
    def __init__(self):
        self.x = 0
        self.y = 0

class WorldMap():
    def __init__(self, rectSettings):
        self.screen = rectSettings.screen
        self.edgeColor = rectSettings.WHITE
        self.backgroundColor = rectSettings.BLACK
        self.rectSize = rectSettings.sidebarRect
        self.mapLoc = MapLocation()
        self.hexList = []

    def drawWorldMap(self, master):
        #Clear Screen
        self.screen.fill(self.backgroundColor)

        if master.mapScrollLeft:
            self.mapLoc.x -= 1
        if master.mapScrollRight:
            self.mapLoc.x += 1
        if master.mapScrollUp:
            self.mapLoc.y -= 1
        if master.mapScrollDown:
            self.mapLoc.y += 1
        for h in self.hexList:
            self.drawTile(self.mapLoc, h)

    def drawTile(self, mapLoc, hexagon):
        hexagon.updatePointList()
        adjustedHex = []
        for i in range(6):
            tempx = hexagon.pointList[i][0] - mapLoc.x
            tempy = hexagon.pointList[i][1] - mapLoc.y
            adjustedHex.append((tempx,tempy))
        pygame.draw.lines(self.screen, self.edgeColor, True, adjustedHex)

    def generateRandomMap(self):
        numRows = random.randrange(3,5) #Generate 3-5 Rows
        numCols = random.randrange(3,5) #Generate 3-5 Cols
        for i in range(numRows):
            for j in range(numCols):
                self.hexList.append(Hexagon(i,j))

    def generateRandomTile(self):
        pass


class Hexagon():
    def __init__(self, hexRow, hexCol):
        self.circumRad = 80
        self.inRad = self.circumRad * 2/sqrt(3)
        #if((hexRow + hexCol) % 2 == 1):
            #print('Error - Invalid Hexagon Placement')
        #else:
        self.row = hexRow
        self.col = hexCol
        self.pointList = None
        self.centerHex()

    def updatePointList(self):
        self.centerLeft = (self.centerx - self.circumRad, self.centery)
        self.topLeft = (self.centerx - self.circumRad/2, self.centery - self.inRad)
        self.topRight = (self.centerx + self.circumRad/2, self.centery - self.inRad)
        self.centerRight = (self.centerx + self.circumRad, self.centery)
        self.bottomLeft = (self.centerx - self.circumRad/2, self.centery + self.inRad)
        self.bottomRight = (self.centerx + self.circumRad/2, self.centery + self.inRad)

        self.pointList = [self.centerLeft,self.topLeft,self.topRight,self.centerRight,self.bottomRight,self.bottomLeft]

    def centerHex(self):
        if(self.col % 2 == 0):
            self.centerx = self.circumRad + self.circumRad*self.col*1.5
            self.centery = self.inRad + self.inRad*self.row*2
        else:
            self.centerx = self.circumRad + self.circumRad*1.5*self.col
            self.centery = self.inRad*(self.row)*2
