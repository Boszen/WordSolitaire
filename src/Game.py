import pygame
from src.constants import *
from src.Card import Card
from src.Alphabet import Alphabet
from src.Board import Board
from src.Dependency import *

class Game:
    def __init__(self,difficulty,high_score):
        self.difficulty = difficulty - 1
        self.high_score = high_score

        self.alphabet_deck = []
        self.alphabet_active = []
        self.alphabet_board = []
        self.alphabet_used = []
        self.Generate_Alphabet()
        self.card_deck = []
        self.card_active = []
        self.card_used = []
        self.Generate_Card()
        self.alphabet_matrix = [[0 for _ in range(7)] for _ in range(7)]
        self.alphabet_draw_amount = 3
        self.card_draw_amount = 3
        self.round = 0
        self.score = 0
        self.formed_words = []
        self.board = Board()
        
    def Generate_Alphabet(self):
        for alphabet in alphabet_image_list.keys():
            if alphabet in ['n', 'r', 't']:
                for i in range(6):
                    self.alphabet_deck.append(Alphabet(alphabet,alphabet_image_list[alphabet]))
            elif alphabet in ['a', 'i']:
                for i in range(5):
                    self.alphabet_deck.append(Alphabet(alphabet,alphabet_image_list[alphabet]))
            elif alphabet in ['d', 'e', 'l', 'o', 's', 'u']:
                for i in range(4):
                    self.alphabet_deck.append(Alphabet(alphabet,alphabet_image_list[alphabet]))   
            elif alphabet in ['g']:
                for i in range(3):
                    self.alphabet_deck.append(Alphabet(alphabet,alphabet_image_list[alphabet]))
            elif alphabet in ['j', 'k', 'q', 'x', 'z']:
                self.alphabet_deck.append(Alphabet(alphabet,alphabet_image_list[alphabet]))
            else:
                for i in range(2):
                    self.alphabet_deck.append(Alphabet(alphabet,alphabet_image_list[alphabet]))

    def Generate_Card(self):
        for card in card_image_list.keys():
            new_card = Card(card, card_image_list[card])
            if card in ['x2_multiplier', 'x0.5_multiplier', 'block', 'x2_block', 'random_remove', 'blind']:
                new_card.type = 'event'
            else:
                new_card.type = 'action'
            self.card_deck.append(new_card)
    
    def moveList(self,listFrom,listTo,item):
        for list in listFrom:
            if list == item:
                listTo.append(list)
                listFrom.remove(list)
                break

    def clearAlphabet(self):
        for alphabet in self.alphabet_active:
            self.alphabet_used.append(alphabet)
        self.alphabet_active = []

    def clearCard(self):
        for card in self.card_active:
            self.card_used.append(card)
        self.card_active = []

    def syncAlphabetMatrix(self):
        for cell in self.board.cell: 
            self.alphabet_matrix[cell.num[0]][cell.num[1]] = cell.occupied

    def findWords(self):
        formed_words_and_indices = []

        # Check horizontally
        for row_idx, row in enumerate(self.alphabet_matrix):
            row_str = ''.join(str(alphabet) for alphabet in row)  # Convert each element to a string
            for word in WORDS:
                if word in row_str:
                    col_idx = row_str.index(word)
                    index = [(row_idx, col_idx + i) for i in range(len(word))]
                    formed_words_and_indices.append((word,index))
        
        for col_idx in range(len(self.alphabet_matrix[0])):
            col_str = ''.join(str(self.alphabet_matrix[row][col_idx]) for row in range(len(self.alphabet_matrix)))
            for word in WORDS:
                if word in col_str:
                    row_idx = col_str.index(word)
                    index = [(row_idx + i, col_idx) for i in range(len(word))]
                    formed_words_and_indices.append((word,index))

        for word,indices in formed_words_and_indices:
            self.formed_words.append(word)
            spec_cell_list = []
            for cell_idx in indices:
                for cell in self.board.cell:
                    if cell.num == cell_idx:
                        spec_cell = cell
                        spec_cell_list.append(spec_cell)
                for alphabet in self.alphabet_active:
                    if spec_cell.collide(alphabet):
                        alphabet.docked = False
                        if spec_cell.special == 'x2_tile':
                            self.score += ALPHABET_SCORE[alphabet.name]*2
                        elif spec_cell.special == 'x0.5_tile':
                            self.score += ALPHABET_SCORE[alphabet.name]*0.5
                        else:
                            self.score += ALPHABET_SCORE[alphabet.name]
                        self.moveList(self.alphabet_active, self.alphabet_used, alphabet)

                for alphabet in self.alphabet_board:
                    if spec_cell.collide(alphabet):
                        alphabet.docked = False
                        if spec_cell.special == 'x2_tile':
                            self.score += ALPHABET_SCORE[alphabet.name]*2
                        elif spec_cell.special == 'x0.5_tile':
                            self.score += ALPHABET_SCORE[alphabet.name]*0.5
                        else:
                            self.score += ALPHABET_SCORE[alphabet.name]
                        self.moveList(self.alphabet_board, self.alphabet_used, alphabet)

                for cell in spec_cell_list:
                    cell.reset()

    def update(self, dt):
        pass

    def render(self, screen):
        self.board.render(screen)
        for alphabet in self.alphabet_board:
            alphabet.render(screen)
        for alphabet in self.alphabet_active:
            alphabet.render(screen)
        for card in self.card_active:
            card.render(screen)
        
        