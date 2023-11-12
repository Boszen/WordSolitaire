from src.states.BaseState import BaseState
from src.Game import Game
from src.Card import Card
from src.Alphabet import Alphabet
from src.Board import Board
from src.constants import *
from src.Dependency import *
import pygame, sys, math, random

class DrawState(BaseState):
    def __init__(self, state_manager):
        super(DrawState, self).__init__(state_manager)
        self.game = Game()
        
        
    
    def Exit(self):
        pass

    def Enter(self, params):
        self.game.round += 1
        self.previous_row = 0
        self.row = 0
        self.column = 0

        if self.game.alphabet_active == []:
            for i in range(0,self.game.alphabet_draw_amount):
                self.row = math.floor(i/3)
                if self.row == self.previous_row and i !=0:
                    self.column +=1
                else:
                    self.column = 0 
                random_alphabet = random.choice(self.game.alphabet_deck)
                random_alphabet.x = (self.column*100) + 935
                random_alphabet.y = 370 - (self.row * 65)
                random_alphabet.x_default = random_alphabet.x
                random_alphabet.y_default = random_alphabet.y
                self.game.moveList(self.game.alphabet_deck, self.game.alphabet_active, random_alphabet)
                self.previous_row = self.row

        if len(self.game.card_active) < 3 :
            random_card = random.choice(self.game.card_deck)
            #random_card = Card('wild_draw',card_image_list['wild_draw'])
            random_card.x = len(self.game.card_active) * 130 + 890
            random_card.y = 460
            random_card.x_default = random_card.x
            random_card.y_default = random_card.y
            self.game.moveList(self.game.card_deck, self.game.card_active, random_card)
            #self.game.card_active.append(random_card)
            self.state_machine.Change('play',{
                        'game': self.game
            })
        else:
            self.state_machine.Change('discard',{
                        'game': self.game
                })
        

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