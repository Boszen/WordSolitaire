from src.states.BaseState import BaseState
import pygame

class StartState(BaseState):
    def __init__(self, state_manager):
        super(StartState, self).__init__(state_manager)