from src.states.BaseState import BaseState
import pygame, sys
from src.constants import *

class GameOverState(BaseState):
    def __init__(self, state_manager):
        super(GameOverState, self).__init__(state_manager)
        #self.new_record_Sound = pygame.mixer.Sound('')#
        self.small_font = pygame.font.Font('./fonts/font.ttf', 32)
        self.medium_font = pygame.font.Font('./fonts/font.ttf', 64)
        self.large_font = pygame.font.Font('./fonts/font.ttf', 96)

    def Exit(self):
        pass

    def Enter(self, params):
        self.score = params['score']
        self.high_score = params['high_score']
        self.game_over_message = params
        self.main_menu_button_rect = pygame.Rect(200, 300, 200, 50)  # Define the button's position and size
        self.main_menu_button_color = (0, 255, 0)  # Green
        self.main_menu_font = pygame.font.Font(None, 36)
        self.main_menu_text = self.main_menu_font.render("Main Menu", True, (0, 0, 0))

    def update(self, dt, events):
          for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    is_break_record = False
                    rank = 11

                    for i in range(9, -1, -1):
                        score = self.high_scores[i]['score']
                        if self.score > score: #break the record
                            rank = i
                            is_break_record = True

                    if is_break_record:
                        self.new_record_sound.play()
                        self.state_machine.Change("enter-high-score", {
                            'high_scores': self.high_scores,
                            'score': self.score,
                            'score_index': rank
                        })
                    else:
                        self.state_machine.Change('start', {
                            'high_scores': self.high_scores
                        })

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


    def render(self, screen):
        t_gameover = self.large_font.render("GAME OVER", False, (255, 255, 255))
        rect = t_gameover.get_rect(center=(WIDTH / 2, HEIGHT/3))
        screen.blit(t_gameover, rect)

        t_gameover = self.small_font.render("Stage Complete", False, (255, 255, 255))
        rect = t_gameover.get_rect(center=(WIDTH / 2, HEIGHT/3))
        screen.blit(t_gameover, rect)

        t_score = self.medium_font.render("Difficulty: " + str(self.difficulty), False, (255, 255, 255))
        rect = t_score.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(t_score, rect)

        t_score = self.medium_font.render("Score: " + str(self.score), False, (255, 255, 255))
        rect = t_score.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(t_score, rect)

        #Render the "Main Menu" button
        pygame.draw.rect(screen, self.main_menu_button_color, self.main_menu_button_rect)
        screen.blit(self.main_menu_text, (self.main_menu_button_rect.centerx - self.main_menu_text.get_width() / 2, self.main_menu_button_rect.centery - self.main_menu_text.get_height() / 4))