from src.states.BaseState import BaseState
from src.constants import *
import pygame,sys


class DifficultySelectionState(BaseState):
    def __init__(self, state_manager):
        super(DifficultySelectionState, self).__init__(state_manager)

        self.difficulty = 1 #Default difficulty

        self.medium_font = pygame.font.Font('./fonts/font.ttf', 48)
        self.large_font = pygame.font.Font('./fonts/font.ttf', 96)

    def Exit(self):
        pass

    def Enter(self, params):
        self.high_scores = params['high_scores']

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # Move the selection up
                    if self.difficulty == 1:
                        self.difficulty = 3 
                    else:
                        self.difficulty -=1
                elif event.key == pygame.K_DOWN:
                    # Move the selection down
                    if self.difficulty == 3:
                        self.difficulty = 1 
                    else:
                        self.difficulty +=1
                elif event.key == pygame.K_RETURN:
                    # Start the game with the selected difficulty
                    if self.difficulty == 1:
                        self.state_machine.Change("draw", {
                            'high_scores': self.high_scores,
                            'difficulty': self.difficulty
                        })
                    elif self.difficulty == 2:
                        self.state_machine.Change("draw", {
                            'high_scores': self.high_scores,
                            'difficulty': self.difficulty
                        })
                    elif self.difficulty == 3:
                        self.state_machine.Change("draw", {
                            'high_scores': self.high_scores,
                            'difficulty': self.difficulty
                        })

    def render(self, screen):
        active_color = (103,255,255)
        inactive_color = (255,255,255)

        # Render text and buttons for difficulty selection
        t_easy = self.medium_font.render("Easy", False, inactive_color)
        rect_easy = t_easy.get_rect(center=(WIDTH / 2, 250))
        t_medium = self.medium_font.render("Medium", False, inactive_color)
        rect_medium = t_medium.get_rect(center=(WIDTH / 2, 350))
        t_hard = self.medium_font.render("Hard", False, inactive_color)
        rect_hard = t_hard.get_rect(center=(WIDTH / 2, 450))

        if self.difficulty == 1:
            t_easy = self.medium_font.render("Easy", False, active_color)
        elif self.difficulty == 2:
            t_medium = self.medium_font.render("Medium", False, active_color)
        elif self.difficulty == 3:
            t_hard = self.medium_font.render("Hard", False, active_color)

        screen.blit(t_easy, rect_easy)
        screen.blit(t_medium, rect_medium)
        screen.blit(t_hard, rect_hard)
