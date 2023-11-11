from src.states.BaseState import BaseState
from src.Game import Game
from src.Card import Card
from src.Alphabet import Alphabet
from src.Board import Board
from src.constants import *
from src.Dependency import gFonts
import pygame, sys, math

class ApplySpecialState(BaseState):
    def __init__(self, state_manager):
        super(ApplySpecialState, self).__init__(state_manager)
    
    def Exit(self):
        pass

    def Enter(self, params):
        self.game = params['game']

    def render(self, screen):
        self.game.render(screen)

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    i = 0
                    for card in self.game.card_active:
                        card.x = i * 130 + 890
                        card.y = 460
                        card.x_default = card.x
                        card.y_default = card.y
                        i += 1
                    self.state_machine.Change('play',{
                        'game': self.game
                    })
           