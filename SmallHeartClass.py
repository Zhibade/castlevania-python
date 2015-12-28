import pygame

from BigHeartClass import BigHeart


class SmallHeart(BigHeart):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.iX = x
        self.iY = y
        self.imgPath = 'Assets/Small_Heart/'
        self.imgName = 'Small_Heart.png'
        self.image = pygame.image.load(self.imgPath + self.imgName)
        self.win = pygame.display.get_surface()
        self.state = True
        self.colliding = False
        self.moveR = 0
        self.rect = self.image.get_rect()
        self.pickedUp = False
        self.heartValue = 1
        self.floor = 1000
    
    def update(self):
        self.checkCollision()
        
        if self.colliding == False and self.state:
            self.y += 1
            
            if self.moveR == 1:
                self.x += 1
            else:
                self.x -= 1
                
            if self.x > self.iX + 10:
                self.moveR = 0
            elif self.x < self.iX - 10:
                self.moveR = 1
            
        if self.state:
            self.win.blit(self.image, (self.x, self.y))