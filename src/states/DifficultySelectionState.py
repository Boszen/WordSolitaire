from src.states.BaseState import BaseState
from src.Game import Game
from src.constants import *
from src.Dependency import *
import pygame,sys, random


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
                    gSounds['select'].play()
                    # Move the selection up
                    if self.difficulty == 1:
                        self.difficulty = 3 
                    else:
                        self.difficulty -=1
                elif event.key == pygame.K_DOWN:
                    gSounds['select'].play()
                    # Move the selection down
                    if self.difficulty == 3:
                        self.difficulty = 1 
                    else:
                        self.difficulty +=1
                elif event.key == pygame.K_RETURN:
                    gSounds['enter'].play()
                    game = Game(self.difficulty, self.high_scores)
                    starter_block_cell = []
                    if self.difficulty == 1:
                        game.dict = WORDS
                        for i in range(2):
                            starter_block_cell.append(random.choice(game.board.cell))
                        for cell in starter_block_cell:
                            cell.special = 'block_tile'
                            cell.color = (150,150,150)
                    elif self.difficulty == 2:
                        for word in WORDS:
                            if 4 <= len(word) <= 7:
                                game.dict.append(word)
                        for i in range(4):
                            starter_block_cell.append(random.choice(game.board.cell))
                        for cell in starter_block_cell:
                            cell.special = 'block_tile'
                            cell.color = (150,150,150)
                    elif self.difficulty == 3:
                        for word in WORDS:
                            if 5 <= len(word) <= 7:
                                game.dict.append(word)
                        for i in range(4):
                            starter_block_cell.append(random.choice(game.board.cell))
                        for cell in starter_block_cell:
                            cell.special = 'block_tile'
                            cell.color = (150,150,150)

                    for cell in game.board.cell:
                        cell.update()
                    self.state_machine.Change("draw", {
                        'game': game
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
            t_easy = self.medium_font.render("Easy (3 Alphabet)", False, active_color)
        elif self.difficulty == 2:
            t_medium = self.medium_font.render("Medium (4 Alphabet)", False, active_color)
        elif self.difficulty == 3:
            t_hard = self.medium_font.render("Hard (5 Alphabet)", False, active_color)

        screen.blit(t_easy, rect_easy)
        screen.blit(t_medium, rect_medium)
        screen.blit(t_hard, rect_hard)
