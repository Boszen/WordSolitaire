from src.states.BaseState import BaseState
import pygame

class DrawState(BaseState):
    def __init__(self, state_manager):
        super(DrawState, self).__init__(state_manager)