from src.states.BaseState import BaseState
import pygame

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
        pass