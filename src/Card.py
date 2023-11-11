import pygame
from src.constants import *

class Card:
    def __init__(self, type, image):
        self.type = type
        self.image = image

        self.dragging = False

        self.x = 0
        self.y = 0

        self.x_default = 0
        self.y_default = 0

        self.width ,self.height = image.get_size()

    def mouseCollide(self, target):
        if self.x < target[0] < self.x + self.width and self.y < target[1] < self.y + self.height:
            return True
        else:
            return False
    
    def collide(self, target):
        return not(self.x + self.width < target.x or self.x > target.x + target.width or
                   self.y + self.height < target.y or self.y > target.y + target.height)

    def update(self, dt):
        pass

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y ))