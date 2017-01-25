import pygame

class Stage(pygame.sprite.Sprite):

    def __init__(self, x, y, stage):
        self.x = x
        self.y = y
        self.stage = stage
        self.imgPath = 'Assets/Stage/'
        self.imgName = 'Level_0'
        self.image = pygame.image.load(self.imgPath + self.imgName + str(stage) + ".png")
        self.win = pygame.display.get_surface()
        
    def update(self):
        self.win.blit(self.image, (self.x, self.y))