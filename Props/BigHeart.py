import pygame


class BigHeart(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.imgPath = 'Assets/Big_Heart/'
        self.imgName = 'Big_Heart.png'
        self.image = pygame.image.load(self.imgPath + self.imgName)
        self.win = pygame.display.get_surface()
        self.state = True
        self.colliding = False
        self.rect = self.image.get_rect()
        self.pickedUp = False
        self.heartValue = 5
        self.floor = 1000
        
    def checkCollision(self):
        if self.y >= self.floor:
            self.colliding = True
        
    def getHeartValue(self):
        return self.heartValue
        
    def getPickedUpState(self):
        return self.pickedUp
        
    def getPos(self):
        array = [self.x, self.y]
        return array
    
    def getRect(self):
        array = [self.rect.width, self.rect.height]
        return array
    
    def getState(self):
        return self.state
    
    def pickUp(self):
        if self.pickedUp == False:
            self.pickedUp = True
    
    def setPos(self, x, y):
        self.x = x
        self.y = y
        
    def setFloor(self, floor):
        self.floor = floor
        
    def setState(self, state):
        self.state = state
        
        if self.state == False:
            self.setPos(-100, -100)
        
    def update(self):
        self.checkCollision()
        
        if self.colliding == False and self.state:
            self.y += 2
            
        if self.state:
            self.win.blit(self.image, (self.x, self.y))
        
        