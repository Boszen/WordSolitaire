import os.path
#Test

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
            pygame.image.load("./graphics/background.png"), (WIDTH+5, HEIGHT+5))

        self.g_state_manager = StateMachine(self.screen)
        states = {
            'start': StartState(self.g_state_manager),
            'dif_select': DifficultySelectionState(self.g_state_manager),
            'draw': DrawState(self.g_state_manager),
            'play': PlayState(self.g_state_manager),
            'between': BetweenRoundState(self.g_state_manager),
            'high_score': HighScoreState(self.g_state_manager),
            'game_over': GameOverState(self.g_state_manager),
        }
        self.g_state_manager.SetStates(states)


    '''def LoadHighScores(self):
        if not os.path.exists(RANK_FILE_NAME):
            with open(RANK_FILE_NAME, "w") as fp:
                for i in range(10, 0, -1):
                    scores = "AAA\n" + str(i*10) + "\n"
                    fp.write(scores)
                fp.close()

        file = open(RANK_FILE_NAME, "r+")
        all_lines = file.readlines()
        scores = []

        name_flip = True
        counter =0
        for i in range(10):
            scores.append({
                'name':'',
                'score':0
            })

        for line in all_lines:
            if name_flip:
                scores[counter]['name'] = line[:-1]
            else:
                scores[counter]['score'] = int(line[:-1])
                counter+=1

            name_flip = not name_flip

        return scores'''

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
        self.g_state_manager.Change('start',{})

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