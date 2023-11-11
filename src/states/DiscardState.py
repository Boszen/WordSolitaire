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
        i = 0
        for card in self.game.card_active:
            card.x = (300 * i) + 250
            card.y = HEIGHT/2 - 100
            card.image = pygame.transform.scale(card.image, (card.width *2, card.height*2 ))
            card.width = card.width*2
            card.height= card.height*2
            i += 1

    def render(self, screen):
        self.game.render(screen)
        screen.blit(self.discard_image, (WIDTH/2 - self.discard_image_width/2, HEIGHT/2 - self.discard_image_height/2))

        t_discard = gFonts['pixel_48'].render("Your hand is full, Discard 1 card", False, (255, 255, 255))
        rect = t_discard.get_rect(center=(WIDTH / 2, HEIGHT / 5))
        screen.blit(t_discard, rect)

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
                            self.game.moveList(self.game.card_active, self.game.card_used, card)
                            random_card = random.choice(self.game.card_deck)
                            self.game.moveList(self.game.card_deck, self.game.card_active, random_card)
                            i = 0
                            for card in self.game.card_active:
                                card.x = i * 130 + 890
                                card.y = 460
                                card.x_default = card.x
                                card.y_default = card.y
                                if card != random_card:
                                    card.image = pygame.transform.scale(card.image, (card.width/2, card.height/2 ))
                                    card.width = card.width/2
                                    card.height= card.height/2
                                i += 1

                            self.state_machine.Change('play', {
                                'game': self.game
                            })
                            break