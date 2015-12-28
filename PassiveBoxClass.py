import pygame

from AttackBoxClass import AttackBox

class PassiveBox(AttackBox):

    def __init__(self, x, y, sizeX, sizeY):
        self.x = x
        self.y = y
        self.sX = sizeX
        self.sY = sizeY
        self.color = pygame.Color(0,0,255)
        self.win = pygame.display.get_surface()
        self.state = True
        self.surface = pygame.Surface((self.sX, self.sY))
        self.surface.fill(self.color)
        
    def changeSize(self, x, y):
        self.sX = x
        self.sY = y
        self.surface = pygame.Surface((self.sX, self.sY))
        self.surface.fill(self.color)        

    def getHit(self, tx, ty, sX, sY, obj):
        right = self.x + self.sX
        bottom = self.y + self.sY
        
        tRight = tx + sX
        tBottom = ty + sY
        
        if self.x <= tRight and right >= tx and self.y <= tBottom and bottom >= ty:
            if self.state:
                obj.setState(False)
                
    def getPos(self):
        array = [self.x, self.y]
        return array
            
    def update(self):
        pass
        #if self.state:
            #self.win.blit(self.surface, (self.x, self.y))