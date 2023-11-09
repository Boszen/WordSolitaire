from src.states.BaseState import BaseState
from src.Game import Game
from src.Card import Card
from src.Alphabet import Alphabet
from src.Board import Board
from src.constants import *
import pygame, sys, math

class PlayState(BaseState):
    def __init__(self, state_manager):
        super(PlayState, self).__init__(state_manager)
        self.dragging_obj = None
    
    def Exit(self):
        pass

    def Enter(self, params):
        self.game = params['game']
        self.game.moveList(self.game.alphabet_deck,self.game.alphabet_active,'a')
        self.game.moveList(self.game.alphabet_deck,self.game.alphabet_active,'a')
        print(self.game.alphabet_deck)
        self.game.moveList(self.game.card_deck,self.game.card_active,1)
        self.game.moveList(self.game.card_deck,self.game.card_active,2)
        print(self.game.card_active)

    def render(self, screen):
        self.game.render(screen)

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    for card in reversed(self.game.card_active):
                        if card.mouseCollide(event.pos):
                            if not self.dragging_obj:
                                # Only allow 1 instance dragging
                                self.dragging_obj = card
                                card.dragging = True
                                self.game.card_active.remove(self.dragging_obj)
                                self.game.card_active.append(self.dragging_obj)
                                print(self.dragging_obj.type)
                                card.offset_x = card.x - event.pos[0]
                                card.offset_y = card.y - event.pos[1]

                    for alphabet in reversed(self.game.alphabet_active):
                        if alphabet.mouseCollide(event.pos):
                            if not self.dragging_obj:
                                # Only allow 1 instance dragging
                                self.dragging_obj = alphabet
                                alphabet.dragging = True
                                self.game.alphabet_active.remove(self.dragging_obj)
                                self.game.alphabet_active.append(self.dragging_obj)
                                print(self.dragging_obj.type)
                                alphabet.offset_x = alphabet.x - event.pos[0]
                                alphabet.offset_y = alphabet.y - event.pos[1]
                    
                    for cell in self.game.board.cell:
                        if cell.mouseCollide(event.pos):
                            cell.occupied = 0
                                
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    if self.dragging_obj:
                        if isinstance(self.dragging_obj, Alphabet):
                            collided_cell = []
                            for cell in self.game.board.cell:
                                if self.dragging_obj.collide(cell):
                                    collided_cell.append(cell)
                            if collided_cell != []:
                                nearest_cell = collided_cell[0]
                                for cell in collided_cell:
                                    if math.dist(cell.centerPoint(), self.dragging_obj.centerPoint()) < math.dist(nearest_cell.centerPoint(), self.dragging_obj.centerPoint()) :
                                        nearest_cell = cell
                                self.dragging_obj.x = nearest_cell.centerPoint()[0] - self.dragging_obj.width/2
                                self.dragging_obj.y = nearest_cell.centerPoint()[1] - self.dragging_obj.height/2
                                nearest_cell.occupied = self.dragging_obj.type

                        self.dragging_obj.dragging = False
                        self.dragging_obj = None

                    for cell in self.game.board.cell: 
                        self.game.alphabet_matrix[cell.num[0]][cell.num[1]] = cell.occupied
                    print(self.game.alphabet_matrix)

        for card in self.game.card_active:
            if card.dragging:
                new_x, new_y = pygame.mouse.get_pos()
                new_x += card.offset_x
                new_y += card.offset_y
                card.x = new_x
                card.y = new_y
        
        for alphabet in self.game.alphabet_active:
            if alphabet.dragging:
                new_x, new_y = pygame.mouse.get_pos()
                new_x += alphabet.offset_x
                new_y += alphabet.offset_y
                alphabet.x = new_x
                alphabet.y = new_y