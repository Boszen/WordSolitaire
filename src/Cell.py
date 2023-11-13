import pygame
from src.constants import *

class Cell:
    def __init__(self, num, x, y):
        self.num = num
        self.occupied = 0
        self.turn_locked = False
        self.image = None
        self.special = 'none'

        self.x = x
        self.y = y
        self.width = CELL_SIZE
        self.height = CELL_SIZE

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
       #screen.blit(self.image, (self.x, self.y ))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x,self.y,self.width,self.height))