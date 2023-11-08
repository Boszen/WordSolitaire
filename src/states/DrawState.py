from src.states.BaseState import BaseState
from src.Game import Game
import pygame,sys

class DrawState(BaseState):
    def __init__(self, state_manager):
        super(DrawState, self).__init__(state_manager)
        self.game = Game()
        self.dragging_obj = None
    
    def Exit(self):
        pass

    def Enter(self, params):
        pass

    def render(self, screen):
        self.game.render(screen)

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    for card in reversed(self.game.card_deck):
                        if card.mouseCollide(event.pos):
                            if not self.dragging_obj:
                                # Only allow dragging if no card is currently being dragged
                                self.dragging_obj = card
                                card.dragging = True
                                self.game.card_deck.remove(self.dragging_obj)
                                self.game.card_deck.append(self.dragging_obj)
                                print(self.dragging_obj.type)
                                card.offset_x = card.x - event.pos[0]
                                card.offset_y = card.y - event.pos[1]

                    for alphabet in reversed(self.game.alphabet_deck):
                        if alphabet.mouseCollide(event.pos):
                            if not self.dragging_obj:
                                # Only allow dragging if no alphabet is currently being dragged
                                self.dragging_obj = alphabet
                                alphabet.dragging = True
                                self.game.alphabet_deck.remove(self.dragging_obj)
                                self.game.alphabet_deck.append(self.dragging_obj)
                                print(self.dragging_obj.type)
                                alphabet.offset_x = alphabet.x - event.pos[0]
                                alphabet.offset_y = alphabet.y - event.pos[1]
                    
                    for cell in self.game.board.cell:
                        if cell.mouseCollide(event.pos):
                            print (cell.num)
                                
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    if self.dragging_obj:
                        self.dragging_obj.dragging = False
                        self.dragging_obj = None

        for card in self.game.card_deck:
            if card.dragging:
                new_x, new_y = pygame.mouse.get_pos()
                new_x += card.offset_x
                new_y += card.offset_y
                card.x = new_x
                card.y = new_y
        
        for alphabet in self.game.alphabet_deck:
            if alphabet.dragging:
                new_x, new_y = pygame.mouse.get_pos()
                new_x += alphabet.offset_x
                new_y += alphabet.offset_y
                alphabet.x = new_x
                alphabet.y = new_y


