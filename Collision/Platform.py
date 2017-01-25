import pygame

from Passive import PassiveBox

class PlatformBox(PassiveBox):

    def __init__(self, x, y, sizeX, sizeY):
        self.x = x
        self.y = y
        self.sX = sizeX
        self.sY = sizeY
        self.color = pygame.Color(0,255,0)
        self.win = pygame.display.get_surface()
        self.state = True
        self.playerHit = False
        self.surface = pygame.Surface((self.sX, self.sY))
        self.surface.fill(self.color)

    def getCollision(self):
        return self.playerHit

    def getHit(self, tx, ty, sX, sY):
        right = self.x + self.sX
        bottom = self.y + self.sY

        tRight = tx + sX
        tBottom = ty + sY

        if self.x <= tRight and right >= tx and self.y <= tBottom and bottom >= ty:
            if self.state:
                self.playerHit = True
                return self.y
        else:
            self.playerHit = False

    def getPos(self):
        array = [self.x, self.y]
        return array

    def getRect(self):
        array = [self.sX, self.sY]
        return array

    def update(self):
        pass
        #if self.state:
            #self.win.blit(self.surface, (self.x, self.y))
