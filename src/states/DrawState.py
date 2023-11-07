from src.states.BaseState import BaseState
from src.Game import Game
import pygame,sys

class DrawState(BaseState):
    def __init__(self, state_manager):
        super(DrawState, self).__init__(state_manager)
        self.game = Game()
        self.dragged_card = None
    
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
                            if not self.dragged_card:
                                # Only allow dragging if no card is currently being dragged
                                self.dragged_card = card
                                card.dragging = True
                                self.game.card_deck.remove(self.dragged_card)
                                self.game.card_deck.append(self.dragged_card)
                                print(self.dragged_card.type)
                                card.offset_x = card.x - event.pos[0]
                                card.offset_y = card.y - event.pos[1]
                                
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    if self.dragged_card:
                        self.dragged_card.dragging = False
                        self.dragged_card = None

        for card in self.game.card_deck:
            if card.dragging:
                new_x, new_y = pygame.mouse.get_pos()
                new_x += card.offset_x
                new_y += card.offset_y
                card.x = new_x
                card.y = new_y


