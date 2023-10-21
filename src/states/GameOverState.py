from src.states.BaseState import BaseState
import pygame

class GameOverState(BaseState):
    def __init__(self, state_manager):
        super(GameOverState, self).__init__(state_manager)