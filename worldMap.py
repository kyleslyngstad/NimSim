import pygame
from math import sqrt

class WorldMap():
    def __init__(self, rectSettings):
        self.screen = rectSettings.screen
        self.edgeColor = rectSettings.WHITE
        self.rectSize = rectSettings.sidebarRect
        self.mapLoc = (0,0)
        self.hexRadius = rectSettings.hexRadius
        self.hexList = []

    def drawWorldMap(self):
        for i in range(3):
            for j in range(4):
                self.hexList.append(Hexagon(self.hexRadius,i,j))
        for h in self.hexList:
            h.updatePointList()
            pygame.draw.lines(self.screen, self.edgeColor, True, h.pointList)

    def drawHex(self):
        pygame.draw.lines(self.screen, self.edgeColor, True, [(200,100),(400,300),(300,200)])

    def generateRandomMap(self):
        pass


class Hexagon():
    def __init__(self, hexRadius, hexRow, hexCol):
        self.circumRad = hexRadius
        self.inRad = self.circumRad * 2/sqrt(3)
        #if((hexRow + hexCol) % 2 == 1):
            #print('Error - Invalid Hexagon Placement')
        #else:
        self.row = hexRow
        self.col = hexCol
        self.pointList = None
        self.centerx = None
        self.centery = None

    def updatePointList(self):
        self.centerHex()
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
            self.centery = self.inRad*(self.row+1)*2

    def drawHex(self,x,y):
        pass
        #calculate 6 vertices
        #pygame.draw.lines()
        #draw angled line
        #draw angled line
        #draw angled line
        #draw angled line
        #draw straight top line
        #draw straight bottom line
