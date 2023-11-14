from src.states.BaseState import BaseState
from src.Game import Game
from src.Card import Card
from src.Alphabet import Alphabet
from src.Board import Board
from src.constants import *
from src.Dependency import gFonts
import pygame, sys, math

class EnterHighScoreState(BaseState):
    def __init__(self, state_manager):
        super(EnterHighScoreState, self).__init__(state_manager)
        self.chars = {
            '1':65,
            '2':65,
            '3':65,
        }

        self.highlighted_char = 1

        self.medium_font = pygame.font.Font('./fonts/font.ttf', 48)
        self.large_font = pygame.font.Font('./fonts/font.ttf', 96)


    def Exit(self):
        pass

    def Enter(self, params):
        self.game = params['game']

        self.current_score = self.game.high_score[self.game.difficulty]
        self.score = self.game.score

        self.score_index = params['score_index']

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pass
                if event.key == pygame.K_LEFT and self.highlighted_char > 1:
                    self.highlighted_char -=1
                elif event.key == pygame.K_RIGHT and self.highlighted_char < 3:
                    self.highlighted_char +=1

                if event.key == pygame.K_UP:
                    self.chars[str(self.highlighted_char)] = self.chars[str(self.highlighted_char)] + 1
                    if self.chars[str(self.highlighted_char)] > 90:
                        self.chars[str(self.highlighted_char)] = 65
                elif event.key == pygame.K_DOWN:
                    self.chars[str(self.highlighted_char)] = self.chars[str(self.highlighted_char)] - 1
                    if self.chars[str(self.highlighted_char)] < 65:
                        self.chars[str(self.highlighted_char)] = 90

                if event.key == pygame.K_RETURN:
                    name = chr(self.chars['1'])+chr(self.chars['2']) + chr(self.chars['3'])

                    for i in range(8, self.score_index-1, -1):
                        #print(self.high_scores)
                        self.current_score[i+1]['name'] = self.current_score[i]['name']
                        self.current_score[i + 1]['score'] = self.current_score[i]['score']

                    self.current_score[self.score_index]['name'] = name
                    self.current_score[self.score_index]['score'] = self.score

                    if self.game.difficulty == 0:
                        rank_file_name = RANK_EASY
                    elif self.game.difficulty == 1:
                        rank_file_name = RANK_MEDIUM
                    else:
                        rank_file_name = RANK_HARD
                        
                    with open(rank_file_name, "w") as fp:
                        for i in range(10):
                            scores = self.current_score[i]['name'] + '\n' + \
                                     str(self.current_score[i]['score']) + '\n'
                            fp.write(scores)
                        fp.close()

                    self.state_machine.Change('high_score', {
                        'high_scores': self.game.high_score
                    })

    def render(self, screen):
        t_score = self.medium_font.render("Your score: " + str(self.score), False, (255, 255, 255))
        rect = t_score.get_rect(center=(WIDTH / 2, 90))
        screen.blit(t_score, rect)

        char1_color = (255, 255, 255)
        char2_color = (255, 255, 255)
        char3_color = (255, 255, 255)
        if self.highlighted_char == 1:
            char1_color = (103, 255, 255)
        elif self.highlighted_char == 2:
            char2_color = (103, 255, 255)
        elif self.highlighted_char == 3:
            char3_color = (103, 255, 255)

        t_char1 = self.large_font.render(chr(self.chars['1']), False, char1_color)
        t_char2 = self.large_font.render(chr(self.chars['2']), False, char2_color)
        t_char3 = self.large_font.render(chr(self.chars['3']), False, char3_color)

        rect = t_char1.get_rect(center=(WIDTH/2-84, HEIGHT/2))
        screen.blit(t_char1, rect)
        rect = t_char2.get_rect(center=(WIDTH / 2 - 18, HEIGHT / 2))
        screen.blit(t_char2, rect)
        rect = t_char3.get_rect(center=(WIDTH / 2 + 60, HEIGHT / 2))
        screen.blit(t_char3, rect)
