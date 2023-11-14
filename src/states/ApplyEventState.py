from src.states.BaseState import BaseState
from src.Game import Game
from src.Card import Card
from src.Alphabet import Alphabet
from src.Board import Board
from src.constants import *
from src.Dependency import *
import pygame, sys, math, random

class ApplyEventState(BaseState):
    def __init__(self, state_manager):
        super(ApplyEventState, self).__init__(state_manager)
        self.dragging_obj = None
    
    def Exit(self):
        pass

    def Enter(self, params):
        self.game = params['game']
        self.card_name = params ['card_name']
        self.card_name_check = params ['card_name']

    def render(self, screen):
        self.game.render(screen)

        t_round = gFonts['pixel_48'].render(f"Round", False, (0,0,0))
        rect = t_round.get_rect(center=(WIDTH - 220, HEIGHT / 5 - 50))
        screen.blit(t_round, rect)
        t_round = gFonts['pixel_48'].render(f"Round", False, (255,255,255))
        rect = t_round.get_rect(center=(WIDTH - 222.5, HEIGHT / 5 - 48.5))
        screen.blit(t_round, rect)

        t_round = gFonts['pixel_48'].render(f"{self.game.round}", False, (255,255,255))
        rect = t_round.get_rect(center=(WIDTH - 220, HEIGHT / 4 - 30))
        screen.blit(t_round, rect)

        t_event = gFonts['pixel_48'].render("Event", False, (0,0,0))
        rect = t_event.get_rect(center=(WIDTH - 220, HEIGHT - 20 ))
        screen.blit(t_event, rect)

        card_show = Card(self.card_name, card_image_list[self.card_name])
        card_show.image = pygame.transform.scale(card_show.image, (card_show.width *2, card_show.height*2 ))
        card_show.width = card_show.width*2
        card_show.height = card_show.height*2
        card_show.x = WIDTH/2 - card_show.width/2
        card_show.y = HEIGHT/2 - card_show.height/2 - 50
        card_show.render(screen)

    def update(self, dt, events):
        if self.card_name_check == 'x2_multiplier':
            random_cell = random.choice(self.game.board.cell)
            random_cell.special = 'x2_tile'
            random_cell.color = (150,255,150)
            self.card_name_check = None
        elif self.card_name_check == 'x0.5_multiplier':
            random_cell = random.choice(self.game.board.cell)
            random_cell.special = 'x0.5_tile'
            random_cell.color = (255,150,150)
            self.card_name_check = None
        elif self.card_name_check == 'block':
            random_cell = random.choice(self.game.board.cell)
            while random_cell.special == 'block_tile' or random_cell.occupied != 0:
                random_cell = random.choice(self.game.board.cell)
            random_cell.special = 'block_tile'
            random_cell.color = (150,150,150)
            self.card_name_check = None
        elif self.card_name_check == 'x2_block':
            for i in range (2):
                random_cell = random.choice(self.game.board.cell)
                while random_cell.special == 'block_tile' or random_cell.occupied != 0:
                    random_cell = random.choice(self.game.board.cell)
                random_cell.special = 'block_tile'
                random_cell.color = (150,150,150)
            self.card_name_check = None

        for cell in self.game.board.cell:
            cell.update()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.state_machine.Change('play',{
                        'game': self.game
                    })
           