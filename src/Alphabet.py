import pygame
from src.constants import *

class Alphabet:
    def __init__(self, name, image):
        self.name = name
        self.image = image

        self.dragging = False
        self.hover = False
        self.docked = False
        self.sequence = 0

        self.x = 0
        self.y = 0 

        self.x_default = 0
        self.y_default = 0
        
        self.width ,self.height = image.get_size()
        self.hover_width = self.width + 5
        self.hover_height = self.height + 5

    def mouseCollide(self, target):
        if self.x < target[0] < self.x + self.width and self.y < target[1] < self.y + self.height:
            return True
        else:
            return False
    
    def collide(self, target):
        return not(self.x + self.width < target.x or self.x > target.x + target.width or
                   self.y + self.height < target.y or self.y > target.y + target.height)
        
    def centerPoint(self):
        center_x = self.x + self.width/2
        center_y = self.y + self.height/2
        return (center_x,center_y)


    def update(self, dt):
        pass

    def render(self, screen):
       if self.hover:
            pygame.draw.rect(screen, (255,0,0), (self.x + self.width/2 - self.hover_width/2 , self.y + self.height/2 - self.hover_height/2, self.hover_width, self.hover_height))
       screen.blit(self.image, (self.x, self.y ))