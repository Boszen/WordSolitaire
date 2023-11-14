from src.states.BaseState import BaseState
from src.Game import Game
from src.Card import Card
from src.Alphabet import Alphabet
from src.Board import Board
from src.constants import *
from src.Dependency import *
import pygame, sys, math, random

class ApplyActionState(BaseState):
    def __init__(self, state_manager):
        super(ApplyActionState, self).__init__(state_manager)
        self.dragging_obj = None
    
    def Exit(self):
        pass

    def Enter(self, params):
        self.game = params['game']
        self.card_name = params ['card_name']
        gSounds['action'].play()

        i = 0
        for card in self.game.card_active:
            card.x = i * 130 + 890
            card.y = 460
            card.x_default = card.x
            card.y_default = card.y
            i += 1

        if self.card_name in ['move', 'copy_it']:
            for alphabet in self.game.alphabet_active:
                    for cell in self.game.board.cell:
                        if alphabet.collide(cell):
                            cell.occupied = 0
                    alphabet.x = alphabet.x_default
                    alphabet.y = alphabet.y_default
                
            self.game.syncAlphabetMatrix()
            self.previous_alphabet_matrix = [row[:] for row in self.game.alphabet_matrix]

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

        if self.card_name == 'move':
            if self.game.alphabet_board != []:
                t_move = gFonts['pixel_32'].render("Move 1 Alphabet", False, (255,255,255))
                rect = t_move.get_rect(center=(WIDTH/2, HEIGHT - 50))
                screen.blit(t_move, rect)
        
        if self.card_name == 'copy_it':
            if self.game.alphabet_board != []:
                t_copy = gFonts['pixel_32'].render("Copy 1 Alphabet on the board", False, (255,255,255))
                rect = t_copy.get_rect(center=(WIDTH/2, HEIGHT - 50))
                screen.blit(t_copy, rect)

    def update(self, dt, events):
        self.game.update(dt)
        if self.card_name == 'wild_draw':
            wild_alphabet = Alphabet('wild_',alphabet_image_list['wild_'])
            wild_alphabet.sequence = len(self.game.alphabet_active)
            self.game.alphabet_active.append(wild_alphabet)
            self.state_machine.Change('play',{
                        'game': self.game
                    })
        elif self.card_name == 'random_draw':
            random_alphabet = random.choice(self.game.alphabet_deck)
            random_alphabet.sequence = len(self.game.alphabet_active)
            self.game.moveList(self.game.alphabet_deck, self.game.alphabet_active, random_alphabet)
            self.state_machine.Change('play',{
                        'game': self.game
                    })
        elif self.card_name == 'con_draw':
            con_alphabet = []
            for alphabet in self.game.alphabet_deck:
                if not alphabet.name in ['a', 'e', 'i', 'o', 'u', 'wild']:
                    con_alphabet.append(alphabet)
            random_con_alphabet = random.choice(con_alphabet)
            random_con_alphabet.sequence = len(self.game.alphabet_active)
            self.game.moveList(self.game.alphabet_deck, self.game.alphabet_active, random_con_alphabet)
            self.state_machine.Change('play',{
                        'game': self.game
                    })
        elif self.card_name == 'vowel_draw':
            vowel_alphabet = []
            for alphabet in self.game.alphabet_deck:
                if alphabet.name in ['a', 'e', 'i', 'o', 'u']:
                    vowel_alphabet.append(alphabet)
            random_vowel_alphabet = random.choice(vowel_alphabet)
            random_vowel_alphabet.sequence = len(self.game.alphabet_active)
            self.game.moveList(self.game.alphabet_deck, self.game.alphabet_active, random_vowel_alphabet)
            self.state_machine.Change('play',{
                        'game': self.game
                    })
        elif self.card_name == 'card_draw':
            card_draw = []
            for i in range (2):
                random_card = random.choice(self.game.card_deck)
                while random_card.type == 'event':
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
        elif self.card_name == 'redraw':
            amount_to_draw = len(self.game.alphabet_active)
            self.game.clearAlphabet()
            self.game.clearCell()

            for i in range(amount_to_draw):
                random_alphabet = random.choice(self.game.alphabet_deck)
                random_alphabet.sequence = len(self.game.alphabet_active)
                self.game.moveList(self.game.alphabet_deck, self.game.alphabet_active, random_alphabet)
            self.state_machine.Change('play',{
                    'game': self.game
            })
        elif self.card_name == 'move':  
            if self.game.alphabet_board == []:
                gSounds['error'].play()
                self.game.card_active.append(Card('move',card_image_list['move']))
                self.state_machine.Change('play',{
                    'game': self.game
                })      
                    
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        for alphabet in reversed(self.game.alphabet_board):
                            if alphabet.mouseCollide(event.pos):
                                if not self.dragging_obj:
                                    # Only allow 1 instance dragging
                                    self.dragging_obj = alphabet
                                    self.dragging_obj.dragging = True
                                    self.dragging_obj.docked = False
                                    self.game.alphabet_board.remove(self.dragging_obj)
                                    self.game.alphabet_board.append(self.dragging_obj)
                                    #print(self.dragging_obj.name)
                                    alphabet.offset_x = alphabet.x - event.pos[0]
                                    alphabet.offset_y = alphabet.y - event.pos[1]
                                #print(alphabet.docked)

                        for cell in self.game.board.cell:
                            if cell.mouseCollide(event.pos):
                                cell.occupied = 0

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:  # Left mouse button
                        if self.dragging_obj:
                            if isinstance(self.dragging_obj, Alphabet):
                                self.dragging_obj.hover = False
                                collided_cell = []
                                for cell in self.game.board.cell:
                                    if self.dragging_obj.collide(cell):
                                        if cell.occupied ==0:
                                            collided_cell.append(cell)
                                if collided_cell != []:
                                    nearest_cell = collided_cell[0]
                                    for cell in collided_cell:
                                        if math.dist(cell.centerPoint(), self.dragging_obj.centerPoint()) < math.dist(nearest_cell.centerPoint(), self.dragging_obj.centerPoint()) :
                                            nearest_cell = cell
                                    self.dragging_obj.x = nearest_cell.centerPoint()[0] - self.dragging_obj.width/2
                                    self.dragging_obj.y = nearest_cell.centerPoint()[1] - self.dragging_obj.height/2
                                    self.dragging_obj.x_default = self.dragging_obj.x
                                    self.dragging_obj.y_default = self.dragging_obj.y
                                    self.dragging_obj.docked = True
                                    nearest_cell.occupied = self.dragging_obj.name
                                    gSounds['place'].play()
                                else:
                                    self.dragging_obj.x = self.dragging_obj.x_default
                                    self.dragging_obj.y = self.dragging_obj.y_default
                                    for cell in self.game.board.cell:
                                        if self.dragging_obj.collide(cell):
                                            if cell.occupied == 0:
                                                cell.occupied = self.dragging_obj.name
                                    self.dragging_obj.docked = True

                            self.dragging_obj.dragging = False
                            self.dragging_obj = None

                            self.game.syncAlphabetMatrix()
                            self.game.findWords()

                            if self.game.alphabet_matrix == self.previous_alphabet_matrix:
                                pass
                            else:
                                self.state_machine.Change('play',{
                                    'game': self.game
                                })
                elif event.type == pygame.MOUSEMOTION:
                    for alphabet in reversed(self.game.alphabet_board):
                        if alphabet.mouseCollide(event.pos) and not alphabet.dragging:
                            alphabet.hover = True
                        else:
                            alphabet.hover = False
                
        elif self.card_name == 'copy_it':
            if self.game.alphabet_board == []:
                gSounds['error'].play()
                self.game.card_active.append(Card('copy_it',card_image_list['copy_it']))
                self.state_machine.Change('play',{
                    'game': self.game
                })     
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        #print(self.game.alphabet_board)
                        for alphabet in self.game.alphabet_board:
                            if alphabet.mouseCollide(event.pos):
                                alphabet.hover = False
                                copy_alphabet = Alphabet(alphabet.name, alphabet.image)
                                copy_alphabet.sequence = len(self.game.alphabet_active)
                                self.game.alphabet_active.append(copy_alphabet)
                                self.state_machine.Change('play',{
                                    'game': self.game
                                })
                elif event.type == pygame.MOUSEMOTION:
                    for alphabet in reversed(self.game.alphabet_board):
                        if alphabet.mouseCollide(event.pos) and not alphabet.dragging:
                            alphabet.hover = True
                        else:
                            alphabet.hover = False

        for alphabet in self.game.alphabet_board:
            if alphabet.dragging:
                new_x, new_y = pygame.mouse.get_pos()
                new_x += alphabet.offset_x
                new_y += alphabet.offset_y
                alphabet.x = new_x
                alphabet.y = new_y

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state_machine.Change('play',{
                        'game': self.game
                    })
           