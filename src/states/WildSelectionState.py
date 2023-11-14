from src.states.BaseState import BaseState
from src.Game import Game
from src.Card import Card
from src.Alphabet import Alphabet
from src.Board import Board
from src.constants import *
from src.Dependency import *
import pygame, sys, math, random

class WildSelectionState(BaseState):
    def __init__(self, state_manager):
        super(WildSelectionState, self).__init__(state_manager)
    
    def Exit(self):
        pass

    def Enter(self, params):
        self.game = params['game']
        self.alphabet_tile = params['alphabet_tile']

        self.selection_bg = pygame.image.load(carpet_bg)
        self.selection_bg_width ,self.selection_bg_height = self.selection_bg.get_size()

        self.alphabet_show = []
        self.row = 0
        self.column = 0
        i = 0
        for alphabet in ALPHABETS:
            new_alphabet = Alphabet(alphabet,alphabet_image_list[alphabet])
            self.row = math.floor(i/10)
            self.column = i % 10
            if self.row == 2:
                new_alphabet.x = (self.column * 100) + WIDTH/2 - 282
            else:
                new_alphabet.x = (self.column * 100) + WIDTH/2 - 482
            new_alphabet.y = (self.row * 85) + 250
            self.alphabet_show.append(new_alphabet)
            i +=1

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
            
        screen.blit(self.selection_bg, (WIDTH/2 - self.selection_bg_width/2, HEIGHT/2 - self.selection_bg_height/2))

        t_select = gFonts['pixel_48'].render("WILD alphabet!, Choose your alphabet", False, (0, 0, 0))
        rect = t_select.get_rect(center=(WIDTH / 2 +2, HEIGHT / 5 +30 +2))
        screen.blit(t_select, rect)
        t_select = gFonts['pixel_48'].render("WILD alphabet!, Choose your alphabet", False, (255, 255, 255))
        rect = t_select.get_rect(center=(WIDTH / 2, HEIGHT / 5 +30))
        screen.blit(t_select, rect)

        for alphabet in self.alphabet_show:
            alphabet.render(screen)

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for alphabet in self.alphabet_show:
                        if alphabet.mouseCollide(event.pos):
                            self.alphabet_tile.name = alphabet.name
                            self.alphabet_tile.image = alphabet.image
                            self.alphabet_tile.dragging = False
                            self.alphabet_tile.hover = False
                            self.state_machine.Change('play',{
                                'game': self.game
                            })
            elif event.type == pygame.MOUSEMOTION:
                for alphabet in reversed(self.alphabet_show):
                        if alphabet.mouseCollide(event.pos):
                            alphabet.hover = True
                        else:
                            alphabet.hover = False