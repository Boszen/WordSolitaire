from src.states.BaseState import BaseState
from src.constants import *
from src.Dependency import *
import pygame, sys

class StartState(BaseState):
    def __init__(self, state_manager):
        super(StartState, self).__init__(state_manager)

        self.option = 1

    def Exit(self):
        pass

    def Enter(self, params):
        self.high_scores = params['high_scores']

    def render(self, screen):
        # title
        t_title = gFonts['pixel_96'].render("Word Solitaire", False, (255, 255, 255))
        rect = t_title.get_rect(center=(WIDTH / 2, HEIGHT / 3 + 20))
        screen.blit(t_title, rect)

        t_start_color = (255, 255, 255)
        t_highscore_color = (255, 255, 255)

        if self.option == 1:
            t_start_color = (103, 255, 255)

        if self.option == 2:
            t_highscore_color = (103, 255, 255)

        t_start = gFonts['pixel_48'].render("START", False, t_start_color)
        rect = t_start.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 210))
        screen.blit(t_start, rect)
        t_highscore = gFonts['pixel_48'].render("HIGH SCORES", False, t_highscore_color)
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
                    gSounds['select'].play()
                    if self.option==1:
                        self.option=2
                    else:
                        self.option=1
                    #self.menu_change_sound.play()
                if event.key == pygame.K_RETURN:
                    gSounds['enter'].play()
                    if self.option == 1:
                        self.state_machine.Change('dif_select', {
                            'high_scores': self.high_scores
                        })
                    else:
                        self.state_machine.Change('high_score', {
                            'high_scores': self.high_scores
                        })
