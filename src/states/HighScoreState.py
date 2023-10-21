from src.states.BaseState import BaseState
import pygame

class HighScoreState(BaseState):
    def __init__(self, state_manager):
        super(HighScoreState, self).__init__(state_manager)