from src.states.BaseState import BaseState
from src.Game import Game
from src.Card import Card
from src.Alphabet import Alphabet
from src.Board import Board
from src.constants import *
from src.Dependency import *
import pygame, sys, math

class PlayState(BaseState):
    def __init__(self, state_manager):
        super(PlayState, self).__init__(state_manager)
        self.dragging_obj = None
    
    def Exit(self):
        pass

    def Enter(self, params):
        self.game = params['game']

        for alphabet in self.game.alphabet_active:
            row = math.floor(alphabet.sequence/3)
            column = alphabet.sequence % 3
            if not alphabet.docked:
                alphabet.x = (column*100) + 935
                alphabet.y = 370 - (row * 65)
                alphabet.x_default = alphabet.x
                alphabet.y_default = alphabet.y
        i = 0
        for card in self.game.card_active:
            card.x = i * 130 + 890
            card.y = 460
            card.x_default = card.x
            card.y_default = card.y
            i += 1
        '''print('Card_deck')
        print(len(self.game.card_deck))
        print('Card_active')
        print(len(self.game.card_active))
        print('Card_used')
        print(len(self.game.card_used))
        print('Alphabet_deck')
        print(len(self.game.alphabet_deck))
        print('Alphabet_active')
        print(len(self.game.alphabet_active))
        print('Alphabet_board')
        print(len(self.game.alphabet_board))
        print('Alphabet_used')
        print(len(self.game.alphabet_used))
        print('--------------------')'''

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    for card in reversed(self.game.card_active):
                        if card.mouseCollide(event.pos):
                            if not self.dragging_obj:
                                # Only allow 1 instance dragging
                                self.dragging_obj = card
                                card.dragging = True
                                self.game.card_active.remove(self.dragging_obj)
                                self.game.card_active.append(self.dragging_obj)
                                #print(self.dragging_obj.name)
                                card.offset_x = card.x - event.pos[0]
                                card.offset_y = card.y - event.pos[1]
                                #print(card.name,", ",card.type)

                    for alphabet in reversed(self.game.alphabet_active):
                        if alphabet.mouseCollide(event.pos):
                            if alphabet.name == 'wild_':
                                    self.state_machine.Change('wild',{
                                        'game': self.game,
                                        'alphabet_tile': alphabet
                                    })
                            #print(alphabet.sequence)
                            if not self.dragging_obj:
                                # Only allow 1 instance dragging
                                self.dragging_obj = alphabet
                                self.dragging_obj.dragging = True
                                self.dragging_obj.docked = False
                                self.game.alphabet_active.remove(self.dragging_obj)
                                self.game.alphabet_active.append(self.dragging_obj)
                                #print(self.dragging_obj.name)
                                alphabet.offset_x = alphabet.x - event.pos[0]
                                alphabet.offset_y = alphabet.y - event.pos[1]
                            #print(alphabet.docked)
                    
                    for cell in self.game.board.cell:
                        if cell.mouseCollide(event.pos):
                            #print(cell.num)
                            if not cell.turn_locked:
                                cell.occupied = 0
                                
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    if self.dragging_obj:
                        if isinstance(self.dragging_obj, Alphabet):
                            collided_cell = []
                            for cell in self.game.board.cell:
                                if self.dragging_obj.collide(cell):
                                    if cell.occupied ==0 and cell.special != 'block_tile':
                                        collided_cell.append(cell)
                            if collided_cell != []:
                                nearest_cell = collided_cell[0]
                                for cell in collided_cell:
                                    if math.dist(cell.centerPoint(), self.dragging_obj.centerPoint()) < math.dist(nearest_cell.centerPoint(), self.dragging_obj.centerPoint()) :
                                        nearest_cell = cell
                                self.dragging_obj.x = nearest_cell.centerPoint()[0] - self.dragging_obj.width/2
                                self.dragging_obj.y = nearest_cell.centerPoint()[1] - self.dragging_obj.height/2
                                self.dragging_obj.docked = True
                                nearest_cell.occupied = self.dragging_obj.name
                                gSounds['place'].play()
                                
                            else:
                                self.dragging_obj.x = self.dragging_obj.x_default
                                self.dragging_obj.y = self.dragging_obj.y_default
                                
                        elif isinstance(self.dragging_obj, Card):
                            for cell in self.game.board.cell:
                                if self.dragging_obj.collide(cell):
                                    self.game.moveList(self.game.card_active, self.game.card_used, self.dragging_obj)
                                    self.state_machine.Change('action',{
                                        'game': self.game,
                                        'card_name': self.dragging_obj.name
                                    })
                                    break
                            self.dragging_obj.x = self.dragging_obj.x_default
                            self.dragging_obj.y = self.dragging_obj.y_default

                            #print(self.dragging_obj.docked)

                        self.dragging_obj.dragging = False
                        self.dragging_obj = None

                        self.game.syncAlphabetMatrix()
                        self.game.findWords()
                        #print(self.game.alphabet_matrix)

                        all_alphabets_docked = True
                        for alphabet in self.game.alphabet_active:
                            if not alphabet.docked:
                                all_alphabets_docked = False
                                break

                        if all_alphabets_docked:
                            if self.game.round >= 15:
                                self.state_machine.Change('game_over',{
                                    'game': self.game
                                })
                                break
                            for alphabet in self.game.alphabet_active:
                                alphabet.x_default = alphabet.x
                                alphabet.y_default = alphabet.y
                                self.game.alphabet_board.append(alphabet)
                            self.game.alphabet_active = []
                            #print(self.game.high_score)
                            self.state_machine.Change('draw', {
                                'game': self.game
                            })

            elif event.type == pygame.MOUSEMOTION:
                for card in reversed(self.game.card_active):
                        if card.mouseCollide(event.pos) and not card.dragging:
                            card.hover = True
                        else:
                            card.hover = False
                for alphabet in reversed(self.game.alphabet_active):
                        if alphabet.mouseCollide(event.pos) and not alphabet.dragging:
                            alphabet.hover = True
                        else:
                            alphabet.hover = False
                            

        for card in self.game.card_active:
            if card.dragging:
                new_x, new_y = pygame.mouse.get_pos()
                new_x += card.offset_x
                new_y += card.offset_y
                card.x = new_x
                card.y = new_y
        
        for alphabet in self.game.alphabet_active:
            if alphabet.dragging:
                new_x, new_y = pygame.mouse.get_pos()
                new_x += alphabet.offset_x
                new_y += alphabet.offset_y
                alphabet.x = new_x
                alphabet.y = new_y