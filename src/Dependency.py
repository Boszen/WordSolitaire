import pygame
from src.Util import SpriteManager, Animation
import src.Util as Util
from src.StateMachine import StateMachine

sprite_collection = SpriteManager().spriteCollection



card_image_list = {
    "1": pygame.image.load("./graphics/playingCards/card-back1.png"),
    "2": pygame.image.load("./graphics/playingCards/card-back2.png")
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