from src.states.BaseState import BaseState
from src.constants import *
import pygame, sys

class StartState(BaseState):
    def __init__(self, state_manager):
        super(StartState, self).__init__(state_manager)
        self.medium_font = pygame.font.Font('./fonts/font.ttf', 48)
        self.large_font = pygame.font.Font('./fonts/font.ttf', 96)

        self.option = 1

    def Exit(self):
        pass

    def Enter(self, params):
        self.high_scores = params['high_scores']

    def render(self, screen):
        # title
        t_title = self.large_font.render("Word Solitaire", False, (255, 255, 255))
        rect = t_title.get_rect(center=(WIDTH / 2, HEIGHT / 3))
        screen.blit(t_title, rect)

        t_start_color = (255, 255, 255)
        t_highscore_color = (255, 255, 255)

        if self.option == 1:
            t_start_color = (103, 255, 255)

        if self.option == 2:
            t_highscore_color = (103, 255, 255)

        t_start = self.medium_font.render("START", False, t_start_color)
        rect = t_start.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 210))
        screen.blit(t_start, rect)
        t_highscore = self.medium_font.render("HIGH SCORES", False, t_highscore_color)
        rect = t_highscore.get_rect(center=(WIDTH/2, HEIGHT/2 + 280))
        screen.blit(t_highscore, rect)



    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    if self.option==1:
                        self.option=2
                    else:
                        self.option=1
                    #self.menu_change_sound.play()
                if event.key == pygame.K_RETURN:
                    #self.confirm_sound.play()

                    if self.option == 1:
                        self.state_machine.Change('dif_select', {
                            'high_scores': self.high_scores
                        })
                    else:
                        self.state_machine.Change('high_score', {
                            'high_scores': self.high_scores
                        })
