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
        
    
    def Exit(self):
        pass

    def Enter(self, params):
        self.game = params['game']
        self.game.round += 1
        
        for cell in self.game.board.cell:
            if cell.occupied != 0:
                cell.turn_locked = True

        if self.game.alphabet_active == []:
            for i in range(self.game.alphabet_draw_amount):
                random_alphabet = random.choice(self.game.alphabet_deck)
                #random_alphabet = Alphabet('a',alphabet_image_list['a'])

                random_alphabet.sequence = i
                self.row = math.floor(random_alphabet.sequence/3)
                self.column = random_alphabet.sequence % 3
                random_alphabet.x = (self.column*100) + 935
                random_alphabet.y = 370 - (self.row * 65)
                random_alphabet.x_default = random_alphabet.x
                random_alphabet.y_default = random_alphabet.y

                self.game.moveList(self.game.alphabet_deck, self.game.alphabet_active, random_alphabet)
                #self.game.alphabet_active.append(random_alphabet)

        random_card = random.choice(self.game.card_deck)
        #random_card = Card('copy_it',card_image_list['copy_it'])
        #random_card.type = 'event'
        if random_card.type == 'event':
            self.state_machine.Change('event', {
                'game': self.game,
                'card_name': random_card.name
            })

        else:
            random_card.x = len(self.game.card_active) * 130 + 890
            random_card.y = 460
            random_card.x_default = random_card.x
            random_card.y_default = random_card.y

            if len(self.game.card_active) < 3 :
                self.game.moveList(self.game.card_deck, self.game.card_active, random_card)
                #self.game.card_active.append(random_card)
                self.state_machine.Change('play',{
                            'game': self.game
                })
            else:
                self.state_machine.Change('discard',{
                            'game': self.game,
                            'number_to_discard': 1,
                            'card_draw': [random_card]

                    })
        
    def render(self, screen):
        self.game.render(screen)

       # Round Text
        t_round = gFonts['pixel_48'].render(f"Round", False, (0,0,0))
        rect = t_round.get_rect(center=(160 + 2,  HEIGHT / 5 - 50 + 2))
        screen.blit(t_round, rect)
        t_round = gFonts['pixel_48'].render(f"Round", False, (255,255,255))
        rect = t_round.get_rect(center=(160, HEIGHT / 5 - 50))
        screen.blit(t_round, rect)
        t_round = gFonts['pixel_48'].render(f"{self.game.round}", False, (255,255,255))
        rect = t_round.get_rect(center=(160, HEIGHT / 5 ))
        screen.blit(t_round, rect)

        # Score Text
        t_score = gFonts['pixel_48'].render("Score", False, (0,0,0))
        rect = t_score.get_rect(center=(160 + 2,  HEIGHT / 4 + 40 + 2))
        screen.blit(t_score, rect)
        t_score = gFonts['pixel_48'].render("Score", False, (255,255,255))
        rect = t_score.get_rect(center=(160, HEIGHT / 4 + 40))
        screen.blit(t_score, rect)
        t_score = gFonts['pixel_48'].render(f"{self.game.score}", False, (255,255,255))
        rect = t_score.get_rect(center=(160, HEIGHT / 4 + 90))
        screen.blit(t_score, rect)

        # Last Word Text
        t_word = gFonts['pixel_32'].render("Latest Word", False, (0,0,0))
        rect = t_word.get_rect(center=(160 + 2,  HEIGHT - 200 + 2))
        screen.blit(t_word, rect)
        t_word = gFonts['pixel_32'].render("Latest Word", False, (255,255,255))
        rect = t_word.get_rect(center=(160, HEIGHT - 200))
        screen.blit(t_word, rect)
        if self.game.formed_words != []:
            t_word = gFonts['pixel_32'].render(f"{self.game.formed_words[-1]}", False, (255,255,255))
            rect = t_word.get_rect(center=(160, HEIGHT - 150))
            screen.blit(t_word, rect)

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()