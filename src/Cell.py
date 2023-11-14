import pygame
from src.constants import *
from src.Dependency import *

class Cell:
    def __init__(self, num, x, y):
        self.num = num
        self.occupied = 0
        self.turn_locked = False
        self.special = None
        self.image = None
        self.color = (255,255,255)

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
    
    def collide(self, target):
        return not(self.x + self.width < target.x or self.x > target.x + target.width or
                   self.y + self.height < target.y or self.y > target.y + target.height)
    
    def reset(self):
        self.occupied = 0
        self.turn_locked = False
        self.special = None
        self.color = (255,255,255)

    def update(self):
        if self.special != None:
            self.image = tile_image_list[self.special]
        else:
            self.image = None

    def render(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x,self.y,self.width,self.height))
        if self.special != None:
            screen.blit(self.image, (self.x + self.width/2 - 32, self.y + self.height/2 - 32 ))