import pygame
from src.constants import *
from src.Card import Card
from src.Alphabet import Alphabet
from src.Board import Board
from src.Dependency import *

class Game:
    def __init__(self):
        self.alphabet_deck = []
        self.Generate_Alphabet()
        self.card_deck = []
        self.Generate_Card()
        self.alphabet_matrix = []
        self.turn = 0
        self.board = Board()
        
    def Generate_Alphabet(self):
        for alphabet in alphabet_image_list.keys():
            print(alphabet)
            self.alphabet_deck.append(Alphabet(alphabet,alphabet_image_list[alphabet]))    

    def Generate_Card(self):
        for card in card_image_list.keys():
            print(card)
            self.card_deck.append(Card(card,card_image_list[card]))
    
    def update(self, dt):
        pass

    def render(self, screen):
        self.board.render(screen)
        for alphabet in self.alphabet_deck:
            alphabet.render(screen)
        for card in self.card_deck:
            card.render(screen)
        
        