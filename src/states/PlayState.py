from src.states.BaseState import BaseState
import pygame
import pygame, sys

class PlayState(BaseState):
    def __init__(self, state_manager):
        super(PlayState, self).__init__(state_manager)
    
    def Exit(self):
        pass

    def Enter(self, params):
        pass

    def render(self, screen):
        pass

    def update(self, dt, events):
         for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                