import pygame
from src.Util import SpriteManager, Animation
import src.Util as Util
from src.StateMachine import StateMachine
import glob, os

sprite_collection = SpriteManager().spriteCollection



card_image_list = {

}

folder_path = "./graphics/playingCards"
image_pattern = os.path.join(folder_path, "*.png") 
image_files = glob.glob(image_pattern)

key=0
for value in image_files:
    card_image_list[key] =  pygame.image.load(value)
    key +=1

alphabet_image_list = {
    'a': sprite_collection["a"].image
}


gSounds = {
  
}

gFonts = {

}


from src.StateMachine import StateMachine
from src.states.StartState import StartState
from src.states.DifficultySelectionState import DifficultySelectionState
from src.states.DrawState import DrawState
from src.states.PlayState import PlayState
from src.states.BetweenRoundState import BetweenRoundState
from src.states.GameOverState import GameOverState
from src.states.HighScoreState import HighScoreState