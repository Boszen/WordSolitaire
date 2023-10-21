from src.states.BaseState import BaseState
import pygame

class PlayState(BaseState):
    def __init__(self, state_manager):
        super(PlayState, self).__init__(state_manager)