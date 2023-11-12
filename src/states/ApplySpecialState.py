from src.states.BaseState import BaseState
from src.Game import Game
from src.Card import Card
from src.Alphabet import Alphabet
from src.Board import Board
from src.constants import *
from src.Dependency import *
import pygame, sys, math

class ApplySpecialState(BaseState):
    def __init__(self, state_manager):
        super(ApplySpecialState, self).__init__(state_manager)
    
    def Exit(self):
        pass

    def Enter(self, params):
        self.game = params['game']
        self.card_type = params ['card_type']

        i = 0
        for card in self.game.card_active:
            card.x = i * 130 + 890
            card.y = 460
            card.x_default = card.x
            card.y_default = card.y
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
        if self.card_type == 'wild_draw':
            self.game.alphabet_active.append(Alphabet('wild',alphabet_image_list['wild']))
            self.state_machine.Change('play',{
                        'game': self.game
                    })
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state_machine.Change('play',{
                        'game': self.game
                    })
           