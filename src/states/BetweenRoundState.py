from src.states.BaseState import BaseState
import pygame

class BetweenRoundState(BaseState):
    def __init__(self, state_manager):
        super(BetweenRoundState, self).__init__(state_manager)
        