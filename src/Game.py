import pygame
from src.constants import *
from src.Card import Card
from src.Dependency import *

class Game:
    def __init__(self):
        self.alphabet_deck = []
        self.card_deck = []
        self.turn = 0
        self.board = []
        self.Generate_Card()

    def Generate_Card(self):
        for card in card_image_list.keys():
            print(card)
            self.card_deck.append(Card(card,card_image_list[card]))
    
    def update(self, dt):
        pass

    def render(self, screen):
        for card in self.card_deck:
            card.render(screen)