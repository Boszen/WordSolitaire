import pygame
from src.constants import *
from src.Card import Card
from src.Alphabet import Alphabet
from src.Board import Board
from src.Dependency import *

class Game:
    def __init__(self):
        self.alphabet_deck = []
        self.alphabet_active = []
        self.alphabet_used = []
        self.Generate_Alphabet()
        self.card_deck = []
        self.card_active = []
        self.card_used = []
        self.Generate_Card()
        self.alphabet_matrix = [[0 for _ in range(7)] for _ in range(7)]
        self.turn = 0
        self.board = Board()
        
    def Generate_Alphabet(self):
        for alphabet in alphabet_image_list.keys():
            if alphabet in ['n', 'r', 't']:
                for i in range(0,6):
                    self.alphabet_deck.append(Alphabet(alphabet,alphabet_image_list[alphabet]))
            elif alphabet in ['a', 'i']:
                for i in range(0,5):
                    self.alphabet_deck.append(Alphabet(alphabet,alphabet_image_list[alphabet]))
            elif alphabet in ['d', 'e', 'l', 'o', 's', 'u']:
                for i in range(0,4):
                    self.alphabet_deck.append(Alphabet(alphabet,alphabet_image_list[alphabet]))   
            elif alphabet in ['g']:
                for i in range(0,3):
                    self.alphabet_deck.append(Alphabet(alphabet,alphabet_image_list[alphabet]))
            elif alphabet in ['j', 'k', 'q', 'x', 'z']:
                self.alphabet_deck.append(Alphabet(alphabet,alphabet_image_list[alphabet]))
            else:
                for i in range(0,2):
                    self.alphabet_deck.append(Alphabet(alphabet,alphabet_image_list[alphabet]))

    def Generate_Card(self):
        for card in card_image_list.keys():
            self.card_deck.append(Card(card,card_image_list[card]))
    
    def moveList(self,listFrom,listTo,itemType):
        for list in listFrom:
            if list.type == itemType:
                listFrom.remove(list)
                listTo.append(list)
                break

    def update(self, dt):
        pass

    def render(self, screen):
        self.board.render(screen)
        for alphabet in self.alphabet_active:
            alphabet.render(screen)
        for card in self.card_active:
            card.render(screen)
        
        