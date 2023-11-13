from src.states.BaseState import BaseState
from src.Game import Game
from src.Card import Card
from src.Alphabet import Alphabet
from src.Board import Board
from src.constants import *
from src.Dependency import *
import pygame, sys, math, random

class DiscardState(BaseState):
    def __init__(self, state_manager):
        super(DiscardState, self).__init__(state_manager)

        self.discard_image = pygame.image.load(discard_bg)
        self.discard_image_width ,self.discard_image_height = self.discard_image.get_size()
        
    
    def Exit(self):
        pass

    def Enter(self, params):
        self.game = params['game']
        self.number_to_discard = params['number_to_discard']
        self.card_draw = params['card_draw']
        self.card_discard = []
        

        i = 0
        for card in self.game.card_active:
            card.x = (300 * i) + 250
            card.y = HEIGHT/2 - 100
            card.image = pygame.transform.scale(card.image, (card.width *2, card.height*2 ))
            card.width = card.width*2
            card.height= card.height*2
            card.hover_width = card.width +10
            card.hover_height= card.height +10
            i += 1

    def render(self, screen):
        self.game.render(screen)
        screen.blit(self.discard_image, (WIDTH/2 - self.discard_image_width/2, HEIGHT/2 - self.discard_image_height/2))

        t_discard = gFonts['pixel_48'].render(f"Your hand is full, Discard {self.number_to_discard} card", False, (255, 255, 255))
        rect = t_discard.get_rect(center=(WIDTH / 2, HEIGHT / 5 - 30))
        screen.blit(t_discard, rect)
        
        i = 0
        t_card_draw = ""
        for draw in self.card_draw:
            if i == 0:
                t_card_draw += draw.name 
            else:
                t_card_draw += f", {draw.name}"
            i += 1

        t_draws = gFonts['pixel_32'].render(f"Your drawing contain : {t_card_draw}", False, (255, 255, 255))
        rect = t_draws.get_rect(center=(WIDTH / 2, HEIGHT / 4 - 10))
        screen.blit(t_draws, rect)

        for card in self.game.card_active:
            card.render(screen)
        
    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    for card in self.game.card_active:
                        if card.mouseCollide(event.pos):
                            if card in self.card_discard:
                                self.card_discard.remove(card)
                            else:  
                                self.card_discard.append(card)
                            
            elif event.type == pygame.MOUSEMOTION:
                for card in reversed(self.game.card_active):
                        if card.mouseCollide(event.pos) and not card.dragging:
                            card.hover = True
                        else:
                            card.hover = False
        for card in self.game.card_active:
            if card in self.card_discard:
                card.hover = True

        if len(self.card_discard) == self.number_to_discard:
            for card in self.card_discard:
                if card in self.game.card_active:
                    self.game.card_active.remove(card)
                card.image = pygame.transform.scale(card.image, (card.width/2, card.height/2 ))
                card.width = card.width/2
                card.height= card.height/2
                card.hover_width = card.width +10
                card.hover_height= card.height +10
                self.game.moveList(self.card_discard, self.game.card_used, card)

            for card in self.card_draw:
                self.game.moveList(self.game.card_deck, self.game.card_active, card)

            i = 0
            for card in self.game.card_active:
                card.x = i * 130 + 890
                card.y = 460
                card.x_default = card.x
                card.y_default = card.y
                if not card in self.card_draw:
                    card.image = pygame.transform.scale(card.image, (card.width/2, card.height/2 ))
                    card.width = card.width/2
                    card.height= card.height/2
                    card.hover_width = card.width +10
                    card.hover_height= card.height +10
                i += 1
             
            self.state_machine.Change('play', {
                'game': self.game
            })
        
        

        
                