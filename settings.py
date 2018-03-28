import pygame

class RectSettings():
    def __init__(self):
        #Color Codes
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.BLUE = (0,0,255)
        self.GREEN = (0,255,0)
        self.RED = (255,0,0)
        self.BEIGE = (183,149,11)

        #Screen details
        self.size = (1024,768)
        self.screenRect = pygame.Rect((0,0), self.size)
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill(self.BLACK)
        self.screenRectFill = self.screen.subsurface(self.screenRect).convert_alpha()

        #Rect details
        self.sidebarWidth = 224
        self.sidebarRect = pygame.Rect((self.screenRect.width - self.sidebarWidth, 0),(self.sidebarWidth,self.screenRect.height))
        self.sidebarRosterRowHeight = 100


class Master():
    def __init__(self):
        self.mousePos = None
        self.dayCount = 1
        self.mapScrollLeft = False
        self.mapScrollRight = False
        self.mapScrollUp = False
        self.mapScrollDown = False
