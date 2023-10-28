from src.states.BaseState import BaseState
from src.constants import *
import pygame,sys

class HighScoreState(BaseState):
    def __init__(self, state_manager):
        super(HighScoreState, self).__init__(state_manager)
        self.options = 1

        self.small_font = pygame.font.Font('./fonts/font.ttf', 24)
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
                if event.key == pygame.K_ESCAPE:
                    #self.return_to_main_sound.play()
                    self.state_machine.Change('start', {
                        'high_scores': self.high_scores
                    })
                if event.key == pygame.K_LEFT:
                    if self.options == 1:
                        self.options = 3
                    else:
                        self.options -= 1
                if event.key == pygame.K_RIGHT:
                    if self.options == 3:
                        self.options = 1
                    else:
                        self.options += 1
                        

    def render(self, screen):
        active_color = (103, 255, 255)
        inactive_color = (255,255,255)

        t_high_score = self.large_font.render("High Scores", False, (255,255,255))
        rect_high_score = t_high_score.get_rect(center=(WIDTH/4, 60))
        t_easy = self.medium_font.render("Easy", False, inactive_color)
        rect_easy = t_easy.get_rect(center=(WIDTH - 500, 70))
        t_medium = self.medium_font.render("Medium", False, inactive_color)
        rect_medium = t_medium.get_rect(center=(WIDTH - 300, 70))
        t_hard = self.medium_font.render("Hard", False, inactive_color)
        rect_hard = t_hard.get_rect(center=(WIDTH - 100, 70))

        if self.options == 1:
            t_easy = self.medium_font.render("Easy", False, active_color)
            current_score = self.high_scores[0]
        elif self.options == 2:
            t_medium = self.medium_font.render("Medium", False, active_color)
            current_score = self.high_scores[1]
        elif self.options == 3:
            t_hard = self.medium_font.render("Hard", False, active_color)
            current_score = self.high_scores[2]

        screen.blit(t_high_score, rect_high_score)
        screen.blit(t_easy, rect_easy)
        screen.blit(t_medium, rect_medium)
        screen.blit(t_hard, rect_hard)


        for i in range(10):
            name = current_score[i]['name']
            score = current_score[i]['score']

            t_index = self.medium_font.render(str(i+1), False, (255, 255, 255))
            rect = t_index.get_rect(topright=(WIDTH/4 + 200, 180+i*39))
            screen.blit(t_index, rect)

            t_name = self.medium_font.render(name, False, (255, 255, 255))
            rect = t_name.get_rect(topright=(WIDTH/4 + 114 + 250, 180 + i * 39))
            screen.blit(t_name, rect)

            t_score = self.medium_font.render(str(score), False, (255, 255, 255))
            rect = t_score.get_rect(topright=(WIDTH / 2 + 200, 180 + i * 39))
            screen.blit(t_score, rect)

            t_escape_message = self.small_font.render("Press Escape to return to the main menu", False, (255, 255, 255))
            rect = t_escape_message.get_rect(center=(WIDTH/2, HEIGHT-54))
            screen.blit(t_escape_message, rect)