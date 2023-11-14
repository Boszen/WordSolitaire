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

        self.alphabet_show = []
        self.row = 0
        self.column = 0
        i = 0
        for alphabet in ALPHABETS:
            new_alphabet = Alphabet(alphabet,alphabet_image_list[alphabet])
            self.row = math.floor(i/10)
            self.column = i % 10
            new_alphabet.x = (self.column * 100)
            new_alphabet.y = (self.row * 85)
            self.alphabet_show.append(new_alphabet)
            i +=1

    def render(self, screen):
        self.game.render(screen)

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