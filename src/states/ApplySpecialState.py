from src.states.BaseState import BaseState
from src.Game import Game
from src.Card import Card
from src.Alphabet import Alphabet
from src.Board import Board
from src.constants import *
from src.Dependency import *
import pygame, sys, math, random

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
            wild_alphabet = Alphabet('wild',alphabet_image_list['wild'])
            wild_alphabet.sequence = len(self.game.alphabet_active)
            self.game.alphabet_active.append(wild_alphabet)
            self.state_machine.Change('play',{
                        'game': self.game
                    })
        elif self.card_type == 'random_draw':
            random_alphabet = random.choice(self.game.alphabet_deck)
            random_alphabet.sequence = len(self.game.alphabet_active)
            self.game.moveList(self.game.alphabet_deck, self.game.alphabet_active, random_alphabet)
            self.state_machine.Change('play',{
                        'game': self.game
                    })
        elif self.card_type == 'con_draw':
            con_alphabet = []
            for alphabet in self.game.alphabet_deck:
                if not alphabet.type in ['a', 'e', 'i', 'o', 'u']:
                    con_alphabet.append(alphabet)
            random_con_alphabet = random.choice(con_alphabet)
            random_con_alphabet.sequence = len(self.game.alphabet_active)
            self.game.moveList(self.game.alphabet_deck, self.game.alphabet_active, random_con_alphabet)
            self.state_machine.Change('play',{
                        'game': self.game
                    })
        elif self.card_type == 'vowel_draw':
            vowel_alphabet = []
            for alphabet in self.game.alphabet_deck:
                if alphabet.type in ['a', 'e', 'i', 'o', 'u']:
                    vowel_alphabet.append(alphabet)
            random_vowel_alphabet = random.choice(vowel_alphabet)
            random_vowel_alphabet.sequence = len(self.game.alphabet_active)
            self.game.moveList(self.game.alphabet_deck, self.game.alphabet_active, random_vowel_alphabet)
            self.state_machine.Change('play',{
                        'game': self.game
                    })
        elif self.card_type == 'card_draw':
            card_draw = []
            for i in range (0,2):
                random_card = random.choice(self.game.card_deck)
                card_draw.append(random_card)

            if len(self.game.card_active) + len(card_draw) > 3:
                number_to_discard = len(self.game.card_active) + len(card_draw) - 3
                self.state_machine.Change('discard', {
                    'game': self.game,
                    'number_to_discard': number_to_discard,
                    'card_draw': card_draw
                })
            else:
                for card in card_draw:
                    self.game.moveList(self.game.card_deck, self.game.card_active, card)
                self.state_machine.Change('play', {
                    'game': self.game
                })
        elif self.card_type == 'redraw':
            pass
                



        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state_machine.Change('play',{
                        'game': self.game
                    })
           