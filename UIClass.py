import pygame

class UI_Image(pygame.sprite.Sprite):

    def __init__(self, x, y, imgName):
        self.x = x
        self.y = y
        self.imgPath = 'Assets/UI/'
        self.imgName = imgName
        self.image = pygame.image.load(self.imgPath + self.imgName)
        self.win = pygame.display.get_surface()
        
    def setPos(self, x, y):
        self.x = x
        self.y = y
    
    def update(self):
        self.win.blit(self.image, (self.x, self.y))
        
        
class UI_Text(pygame.sprite.Sprite):
       
    def __init__(self, x, y, fontName, text, fontSize):
        self.x = x
        self.y = y
        self.fontPath = 'Assets/Font/'
        self.fontName = fontName
        self.fontSize = fontSize
        self.font = pygame.font.Font(self.fontPath + self.fontName, self.fontSize)
        self.text = self.font.render(text, True, (255, 255, 255))
        self.win = pygame.display.get_surface()
        
    def setPos(self, x, y):
        self.x = x
        self.y = y
        
    def setText(self, text):
        self.text = self.font.render(text, True, (255, 255, 255))
    
    def update(self):
        self.win.blit(self.text, (self.x, self.y))
        