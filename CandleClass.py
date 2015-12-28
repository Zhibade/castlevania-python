import pygame, random
from pygame.locals import *

from BigHeartClass import BigHeart
from SmallHeartClass import SmallHeart

class Candle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.imgPath = 'Assets/Candle/'
        self.imgName = 'Candle_0'
        self.image = pygame.image.load(self.imgPath + self.imgName + "1.png")
        self.frameMod = 0
        self.frame = 0
        self.win = pygame.display.get_surface()
        self.state = True
        self.spawned = False
        self.rect = self.image.get_rect()
        self.spawnedItem = 0

        self.frameArray = self.loadImages(2)
        
    def loadImages(self, num):
        array = []
        for x in range(0, num):
            numImage = x + 1
            array.append(pygame.image.load(self.imgPath + self.imgName + str(numImage) + '.png'))
        return array
    
    def getPos(self):
        array = [self.x, self.y]
        return array
    
    def getRect(self):
        array = [self.rect.width, self.rect.height]
        return array
    
    def getSpawnedItem(self):
        return self.spawnedItem
    
    def getState(self):
        return self.state
    
    def setActive(self, state):
        self.state = state
        
        if self.state == False and self.spawned == False:
            self.spawnItem()
            self.spawned = True
        
    def spawnItem(self):
        rnd = random.randint(0,3)
        
        if rnd == 0:
            self.spawnedItem = BigHeart(self.x, self.y)
    
        if rnd > 0:
            self.spawnedItem = SmallHeart(self.x, self.y)
    
    def playAnim(self):
        mod = self.frameMod%5

        if mod == 0:
            self.frame += 1
                
        if (self.frame > 1):
            self.frame = 0

        self.frameMod += 1
        self.image = self.frameArray[self.frame]
    
    def update(self):
        if self.state:
            self.playAnim()
            self.win.blit(self.image, (self.x, self.y))
        elif self.spawned:
            self.spawnedItem.update()