import pygame
import playstate as ps
import resman

class ScrabbleGame:
    def __init__(self):
        pygame.init()

        self.rman = resman.ResourceManager()

    def play(self, ai):
        '''
        Manages all the game states (only 1 state in this prototype).
        But, I must conform to the conventions....

        You could technically just isolate this whole thing and it
        could constitute as a program itself. But classes are nice.
        Modularization is fun. And you get to read more of these
        epic comments, right?
        '''
        # Constants
        SIZE = (800, 800)

        # Variables
        screen = pygame.display.set_mode(SIZE)
        clock = pygame.time.Clock()
        running = True
        currentState = ps.PlayState(self.rman, ai)

        pygame.display.set_caption("Scrabble")

        # Main loop
        while running:
            # Event handling
            for evt in pygame.event.get():
                if evt.type == pygame.QUIT:
                    running = False
                else:
                    currentState.handle(evt)

            # Drawing the state
            screen.fill((0, 0, 0))
            currentState.draw(screen)
            pygame.display.flip()

            # Updating the state
            currentState.update(clock.tick(60) / 1e3)

        pygame.quit()
