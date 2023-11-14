import os.path

import pygame, math
from pygame import mixer
from src.constants import *


pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.init()

music_channel = mixer.Channel(0)
music_channel.set_volume(0.2)

from src.Dependency import *

class GameMain:
    def __init__(self):
        self.max_frame_rate = 60
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.scroll_bg = False

        self.bg_image = pygame.transform.scale(
            pygame.image.load("./graphics/Board/Wallpaper.png"), (WIDTH+5, HEIGHT+5))

        self.g_state_manager = StateMachine(self.screen)
        states = {
            'start': StartState(self.g_state_manager),
            'dif_select': DifficultySelectionState(self.g_state_manager),
            'draw': DrawState(self.g_state_manager),
            'discard': DiscardState(self.g_state_manager),
            'play': PlayState(self.g_state_manager),
            'wild': WildSelectionState(self.g_state_manager),
            'action': ApplyActionState(self.g_state_manager),
            'event': ApplyEventState(self.g_state_manager),
            'between': BetweenRoundState(self.g_state_manager),
            'high_score': HighScoreState(self.g_state_manager),
            'enter_high_score': EnterHighScoreState(self.g_state_manager),
            'game_over': GameOverState(self.g_state_manager)
        }
        self.g_state_manager.SetStates(states)
    
    def LoadHighScores(self):
        if not os.path.exists(RANK_EASY):
            with open(RANK_EASY, "w") as fp:
                for i in range(10):
                    scores ="AAA\n" + str((10-i)*10) + "\n"
                    fp.write(scores)
                fp.close()

        if not os.path.exists(RANK_MEDIUM):
            with open(RANK_MEDIUM, "w") as fp:
                for i in range(10):
                    scores ="BBB\n" + str((10-i)*10) + "\n"
                    fp.write(scores)
                fp.close()

        if not os.path.exists(RANK_HARD):
            with open(RANK_HARD, "w") as fp:
                for i in range(10):
                    scores ="CCC\n" + str((10-i)*10) + "\n"
                    fp.write(scores)
                fp.close()

        rank_files = [RANK_EASY,RANK_MEDIUM,RANK_HARD]

        scores = []

        for file_name in rank_files:

            file = open(file_name, "r+")
            
            all_lines = file.readlines()
            score = []

            list_header = 0
            counter =0
            for i in range(10):
                score.append({
                    'name':'',
                    'score':0
                })

            for line in all_lines:
                if list_header == 0:
                    score[counter]['name'] = line[:-1]
                    list_header += 1
                else:
                    score[counter]['score'] = int(line[:-1])
                    counter+=1
                    list_header = 0
            scores.append(score)

        return scores

    def RenderBackground(self):
        if self.scroll_bg:
            i = 0
            while i < self.num_dup_images:
                main.screen.blit(self.bg_image,
                                 (self.bg_image.get_width() * i + self.scroll, 0))  # appending same images to the back
                i += 1
            self.scroll -= 6
            if abs(self.scroll) > self.bg_image.get_width():
                self.scroll = 0
        else:
            
            main.screen.blit(self.bg_image, (0, 0))

    def PlayGame(self):
        #self.bg_music.play(-1)
        clock = pygame.time.Clock()
        self.g_state_manager.Change('start',{
            'high_scores': self.LoadHighScores(),
        })

        scroll = 0

        while True:
            pygame.display.set_caption("Word Solitaire")
            dt = clock.tick(self.max_frame_rate) / 1000.0

            #input
            events = pygame.event.get()

            #update
            self.g_state_manager.update(dt, events)

            #bg render
            self.RenderBackground()
            #render
            self.g_state_manager.render()

            #screen update
            pygame.display.update()


if __name__ == '__main__':
    main = GameMain()

    main.PlayGame()
