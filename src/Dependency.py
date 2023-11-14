import pygame
from src.Util import SpriteManager, Animation
import src.Util as Util
from src.StateMachine import StateMachine
import glob, os
from src.constants import *

sprite_collection = SpriteManager().spriteCollection

carpet_bg = "./graphics/carpetBg.png"
board_graphics = "./graphics/Board/Board.png"

tile_image_list = {
    'x2_tile': pygame.image.load('./graphics/Board/x2.png'),
    'x0.5_tile': pygame.image.load('./graphics/Board/x0.5.png'),
    'block_tile': pygame.image.load('./graphics/Board/Block.png'),
}

card_image_list = {
    #Action Cards
    'wild_draw':pygame.image.load('./graphics/Cards/Action/WildCard.png'),
    'random_draw':pygame.image.load('./graphics/Cards/Action/AdditionalDraw.png'),
    'con_draw':pygame.image.load('./graphics/Cards/Action/ConsonantDraw.png'),
    'vowel_draw':pygame.image.load('./graphics/Cards/Action/VowelDraw.png'),
    'card_draw':pygame.image.load('./graphics/Cards/Action/DrawCard.png'),
    'redraw':pygame.image.load('./graphics/Cards/Action/RedrawCard.png'),
    'move':pygame.image.load('./graphics/Cards/Action/MoveAlphabet.png'),
    'copy_it':pygame.image.load('./graphics/Cards/Action/CopyIt.png'),
    #'alphabet_overload':pygame.image.load('./graphics/Cards/Action/AlphabetOverload.png'),
    #'remove':pygame.image.load('./graphics/Cards/Action/RemoveTile.png'),
    #'say_that_word':pygame.image.load('./graphics/Cards/Action/SayThatWord.png'),
    #Event Cards
    'x2_multiplier':pygame.image.load('./graphics/Cards/Event/x2Multiplier.png'),
    'x0.5_multiplier':pygame.image.load('./graphics/Cards/Event/x0.5Multiplier.png'),
    'block':pygame.image.load('./graphics/Cards/Event/Block.png'),
    'x2_block':pygame.image.load('./graphics/Cards/Event/x2Block.png'),
    #'blind':pygame.image.load('./graphics/Cards/Event/BlindCard.png'),
    #'random_remove':pygame.image.load('./graphics/Cards/Event/RandomRemove.png')
}

alphabet_image_list = {
    'wild_': pygame.image.load('./graphics/Board/wild_.png')   
}

folder_path = "./graphics/Alphabet"
image_pattern = os.path.join(folder_path, "*.png") 
image_files = glob.glob(image_pattern) 
i=0
for value in image_files:
    alphabet_image_list[ALPHABETS[i]] = pygame.image.load(value)
    i += 1

gSounds = {
  'action': pygame.mixer.Sound('./sounds/Action.wav'),
  'enter': pygame.mixer.Sound('./sounds/Enter.wav'),
  'error': pygame.mixer.Sound('./sounds/Error.wav'),
  'event': pygame.mixer.Sound('./sounds/Event.wav'),
  'exit': pygame.mixer.Sound('./sounds/Exit.wav'),
  'place': pygame.mixer.Sound('./sounds/Place.wav'),
  'score': pygame.mixer.Sound('./sounds/Score.wav'),
  'select': pygame.mixer.Sound('./sounds/Select.wav')
}

gFonts = {
    'pixel_32': pygame.font.Font('./fonts/font.ttf',32),
    'pixel_48': pygame.font.Font('./fonts/font.ttf', 48),
    'pixel_96': pygame.font.Font('./fonts/font.ttf', 96)
}


from src.StateMachine import StateMachine
from src.states.StartState import StartState
from src.states.DifficultySelectionState import DifficultySelectionState
from src.states.DrawState import DrawState
from src.states.DiscardState import DiscardState
from src.states.PlayState import PlayState
from src.states.WildSelectionState import WildSelectionState
from src.states.ApplyActionState import ApplyActionState
from src.states.ApplyEventState import ApplyEventState
from src.states.GameOverState import GameOverState
from src.states.HighScoreState import HighScoreState
from src.states.EnterHighScoreState import EnterHighScoreState