import pygame
from src.Util import SpriteManager, Animation
import src.Util as Util
from src.StateMachine import StateMachine
import glob, os

sprite_collection = SpriteManager().spriteCollection

discard_bg = "./graphics/discardBg.png"

tile_image_list = {
    'x2_tile': sprite_collection["x2_tile"].image,
    'x0.5_tile': sprite_collection["x0.5_tile"].image,
    'block_tile': sprite_collection["block_tile"].image,
}

card_image_list = {
    'wild_draw':pygame.image.load('./graphics/playingCards/card-back1.png'),
    'random_draw':pygame.image.load('./graphics/playingCards/card-back1.png'),
    'con_draw':pygame.image.load('./graphics/playingCards/card-back1.png'),
    'vowel_draw':pygame.image.load('./graphics/playingCards/card-back1.png'),
    'card_draw':pygame.image.load('./graphics/playingCards/card-back1.png'),
    'redraw':pygame.image.load('./graphics/playingCards/card-back1.png'),
    'move':pygame.image.load('./graphics/playingCards/card-back1.png'),
    'copy_it':pygame.image.load('./graphics/playingCards/card-back1.png'),
    'alphabet_overload':pygame.image.load('./graphics/playingCards/card-back1.png'),
    'remove':pygame.image.load('./graphics/playingCards/card-back1.png'),
    'say_that_word':pygame.image.load('./graphics/playingCards/card-back1.png'),
    'x2_multiplier':pygame.image.load('./graphics/playingCards/card-back1.png'),
    'x0.5_multiplier':pygame.image.load('./graphics/playingCards/card-back1.png'),
    'block':pygame.image.load('./graphics/playingCards/card-back1.png'),
    'x2_block':pygame.image.load('./graphics/playingCards/card-back1.png'),
    'blind':pygame.image.load('./graphics/playingCards/card-back1.png'),
    'random_remove':pygame.image.load('./graphics/playingCards/card-back1.png'),
    'bonus':pygame.image.load('./graphics/playingCards/card-back1.png')
}

'''folder_path = "./graphics/playingCards"
image_pattern = os.path.join(folder_path, "*.png") 
image_files = glob.glob(image_pattern)

key=0
for value in image_files:
    card_image_list[key] =  pygame.image.load(value)
    key +=1'''

alphabet_image_list = {
    'a': sprite_collection["a"].image,
    'b': sprite_collection["b"].image,
    'c': sprite_collection["c"].image,
    'd': sprite_collection["d"].image,
    'e': sprite_collection["e"].image,
    'f': sprite_collection["f"].image,
    'g': sprite_collection["g"].image,
    'h': sprite_collection["h"].image,
    'i': sprite_collection["i"].image,
    'j': sprite_collection["j"].image,
    'k': sprite_collection["k"].image,
    'l': sprite_collection["l"].image,
    'm': sprite_collection["m"].image,
    'n': sprite_collection["n"].image,
    'o': sprite_collection["o"].image,
    'p': sprite_collection["p"].image,
    'q': sprite_collection["q"].image,
    'r': sprite_collection["r"].image,
    's': sprite_collection["s"].image,
    't': sprite_collection["t"].image,
    'u': sprite_collection["u"].image,
    'v': sprite_collection["v"].image,
    'w': sprite_collection["w"].image,
    'x': sprite_collection["x"].image,
    'y': sprite_collection["y"].image,
    'z': sprite_collection["z"].image,
    'wild': sprite_collection["wild"].image
}


gSounds = {
  
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
from src.states.ApplyActionState import ApplyActionState
from src.states.ApplyEventState import ApplyEventState
from src.states.BetweenRoundState import BetweenRoundState
from src.states.GameOverState import GameOverState
from src.states.HighScoreState import HighScoreState