import pygame
from src.constants import *
from src.Dependency import *
from src.Cell import Cell

class Board:
    def __init__(self):
        self.image = pygame.image.load(board_graphics)
        self.x = 280
        self.y = 60

        self.cell = None
        self.gap = 14
        self.Generate_Cell()
        
        #self.width ,self.height = image.get_size()

    def Generate_Cell(self):
        cell_matrix = []
        for i in range(7):
            y_temp = (i) * (CELL_SIZE + self.gap) + self.y
            for j in range(7):
                x_temp = (j) * (CELL_SIZE + self.gap) + self.x
                cell = Cell((i,j), x_temp, y_temp)
                cell_matrix.append(cell)
        self.cell = cell_matrix

    def update(self, dt):
        for cell in self.cell:
            cell.update(dt)
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y ))
        for cell in self.cell:
            cell.render(screen)
