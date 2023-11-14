from src.states.BaseState import BaseState
from src.Game import Game
from src.Card import Card
from src.Alphabet import Alphabet
from src.Board import Board
from src.constants import *
from src.Dependency import gFonts
import pygame, sys, math

class GameOverState(BaseState):
    def __init__(self, state_manager):
        super(GameOverState, self).__init__(state_manager)

        self.small_font = pygame.font.Font('./fonts/font.ttf', 32)
        self.medium_font = pygame.font.Font('./fonts/font.ttf', 64)
        self.large_font = pygame.font.Font('./fonts/font.ttf', 96)

    def Exit(self):
        pass

    def Enter(self, params):
        self.game = params['game']
        self.score = self.game.score
        self.difficulty = self.game.difficulty

        self.current_score = self.game.high_score[self.difficulty]
        print(self.current_score)

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
                        score = self.current_score[i]['score']
                        if self.score > score: #break the record
                            rank = i
                            is_break_record = True

                    if is_break_record:
                        self.state_machine.Change("enter_high_score", {
                            'game': self.game,
                            'score_index': rank
                        })
                    else:
                        self.state_machine.Change('start', {
                            'high_scores': self.game.high_score
                        })

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


    def render(self, screen):
        t_game_over = gFonts['pixel_96'].render("Game Over", False, (0, 0, 0))
        rect = t_game_over.get_rect(center=(WIDTH / 2 + 2, HEIGHT / 3 + 20 + 2))
        screen.blit(t_game_over, rect)
        t_game_over = gFonts['pixel_96'].render("Game Over", False, (255, 255, 255))
        rect = t_game_over.get_rect(center=(WIDTH / 2, HEIGHT / 3 + 20))
        screen.blit(t_game_over, rect)

        t_score = gFonts['pixel_48'].render("Your Score:", False, (0, 0, 0))
        rect = t_score.get_rect(center=(WIDTH / 2 - 150 + 2, HEIGHT / 2+ 20 + 2))
        screen.blit(t_score, rect)
        t_score = gFonts['pixel_48'].render("Your Score:", False, (255, 255, 255))
        rect = t_score.get_rect(center=(WIDTH / 2 - 150, HEIGHT / 2 + 20))
        screen.blit(t_score, rect)

        t_score = gFonts['pixel_48'].render(f"{self.score}", False, (255, 255, 255))
        rect = t_score.get_rect(center=(WIDTH / 2 + 150 , HEIGHT / 2 + 20 ))
        screen.blit(t_score, rect)
        

        '''t_gameover = self.large_font.render("GAME OVER", False, (255, 255, 255))
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
        screen.blit(self.main_menu_text, (self.main_menu_button_rect.centerx - self.main_menu_text.get_width() / 2, self.main_menu_button_rect.centery - self.main_menu_text.get_height() / 4))'''