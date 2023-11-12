from src.states.BaseState import BaseState
from src.Game import Game
from src.Card import Card
from src.Alphabet import Alphabet
from src.Board import Board
from src.constants import *
from src.Dependency import gFonts
import pygame, sys, math

class PlayState(BaseState):
    def __init__(self, state_manager):
        super(PlayState, self).__init__(state_manager)
        self.dragging_obj = None
    
    def Exit(self):
        pass

    def Enter(self, params):
        self.game = params['game']
        self.previous_row = 0
        self.row = 0
        self.column = 0

        i = 0
        for alphabet in self.game.alphabet_active:
            self.row = math.floor(i/3)
            if self.row == self.previous_row and i !=0:
                self.column +=1
            else:
                self.column = 0 
            alphabet.x = (self.column*100) + 935
            alphabet.y = 370 - (self.row * 65)
            alphabet.x_default = alphabet.x
            alphabet.y_default = alphabet.y

            self.previous_row = self.row
            i += 1


    def render(self, screen):
        self.game.render(screen)

        t_round = gFonts['pixel_48'].render(f"Round", False, (0,0,0))
        rect = t_round.get_rect(center=(WIDTH - 220, HEIGHT / 5 - 50))
        screen.blit(t_round, rect)
        t_round = gFonts['pixel_48'].render(f"Round", False, (255,255,255))
        rect = t_round.get_rect(center=(WIDTH - 222.5, HEIGHT / 5 - 48.5))
        screen.blit(t_round, rect)

        t_round = gFonts['pixel_48'].render(f"{self.game.round}", False, (255,255,255))
        rect = t_round.get_rect(center=(WIDTH - 220, HEIGHT / 4 - 30))
        screen.blit(t_round, rect)

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
                                #print(self.dragging_obj.type)
                                card.offset_x = card.x - event.pos[0]
                                card.offset_y = card.y - event.pos[1]
                                print(card.type)

                    for alphabet in reversed(self.game.alphabet_active):
                        if alphabet.mouseCollide(event.pos):
                            if not self.dragging_obj:
                                # Only allow 1 instance dragging
                                self.dragging_obj = alphabet
                                self.dragging_obj.dragging = True
                                self.dragging_obj.docked = False
                                self.game.alphabet_active.remove(self.dragging_obj)
                                self.game.alphabet_active.append(self.dragging_obj)
                                #print(self.dragging_obj.type)
                                alphabet.offset_x = alphabet.x - event.pos[0]
                                alphabet.offset_y = alphabet.y - event.pos[1]
                            #print(alphabet.docked)
                    
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
                                    if cell.occupied ==0:
                                        collided_cell.append(cell)
                            if collided_cell != []:
                                nearest_cell = collided_cell[0]
                                for cell in collided_cell:
                                    if math.dist(cell.centerPoint(), self.dragging_obj.centerPoint()) < math.dist(nearest_cell.centerPoint(), self.dragging_obj.centerPoint()) :
                                        nearest_cell = cell
                                self.dragging_obj.x = nearest_cell.centerPoint()[0] - self.dragging_obj.width/2
                                self.dragging_obj.y = nearest_cell.centerPoint()[1] - self.dragging_obj.height/2
                                self.dragging_obj.docked = True
                                nearest_cell.occupied = self.dragging_obj.type
                            else:
                                self.dragging_obj.x = self.dragging_obj.x_default
                                self.dragging_obj.y = self.dragging_obj.y_default
                                
                        elif isinstance(self.dragging_obj, Card):
                            for cell in self.game.board.cell:
                                if self.dragging_obj.collide(cell):
                                    self.game.moveList(self.game.card_active, self.game.card_used, self.dragging_obj)
                                    self.state_machine.Change('special',{
                                        'game': self.game,
                                        'card_type': self.dragging_obj.type
                                    })
                                    break
                            self.dragging_obj.x = self.dragging_obj.x_default
                            self.dragging_obj.y = self.dragging_obj.y_default

                            #print(self.dragging_obj.docked)

                        self.dragging_obj.dragging = False
                        self.dragging_obj = None

                    for cell in self.game.board.cell: 
                        self.game.alphabet_matrix[cell.num[0]][cell.num[1]] = cell.occupied
                        #print(self.game.alphabet_matrix)

                    all_alphabets_docked = True
                    for alphabet in self.game.alphabet_active:
                        if not alphabet.docked:
                            all_alphabets_docked = False
                            break

                    if all_alphabets_docked:
                        for alphabet in self.game.alphabet_active:
                            self.game.alphabet_board.append(alphabet)
                        self.game.alphabet_active = []
                        self.state_machine.Change('draw', {
                            'game': self.game
                        })

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