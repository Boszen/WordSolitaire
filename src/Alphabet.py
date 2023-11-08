import pygame
from src.constants import *

class Alphabet:
    def __init__(self, type, image):
        self.type = type
        self.image = image

        self.dragging = False

        self.x = WIDTH / 2 
        self.y = HEIGHT /2 
        self.width ,self.height = image.get_size()

    def mouseCollide(self, target):
        if self.x < target[0] < self.x + self.width and self.y < target[1] < self.y + self.height:
            return True
        else:
            return False
        
    def centerPoint(self):
        center_x = self.x + self.width/2
        center_y = self.y + self.height/2
        return (center_x,center_y)


    def update(self, dt):
        pass

    def render(self, screen):
       screen.blit(self.image, (self.x, self.y ))