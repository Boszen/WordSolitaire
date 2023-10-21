from src.states.BaseState import BaseState
import pygame

class DifficultySelectionState(BaseState):
    def __init__(self, state_manager):
        super(DifficultySelectionState, self).__init__(state_manager)