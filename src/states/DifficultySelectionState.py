from src.states.BaseState import BaseState
import pygame


class DifficultySelectionState(BaseState):
    def __init__(self, state_manager):
        super(DifficultySelectionState, self).__init__(state_manager)
        self.difficulty = "Easy" #Default difficulty

    def Exit(self):
        pass

    def Enter(self, params):
        self.difficulty = "Easy"  # Reset the difficulty when entering the state
#assd

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # Move the selection up
                    if self.difficulty == "Medium":
                        self.difficulty = "Easy"
                    elif self.difficulty == "Hard":
                        self.difficulty = "Medium"
                elif event.key == pygame.K_DOWN:
                    # Move the selection down
                    if self.difficulty == "Easy":
                        self.difficulty = "Medium"
                    elif self.difficulty == "Medium":
                        self.difficulty = "Hard"
                elif event.key == pygame.K_RETURN:
                    # Start the game with the selected difficulty
                    if self.difficulty == "Easy":
                        self.state_manager.change_state("Game", difficulty="Easy")
                    elif self.difficulty == "Medium":
                        self.state_manager.change_state("Game", difficulty="Medium")
                    elif self.difficulty == "Hard":
                        self.state_manager.change_state("Game", difficulty="Hard")

    def render(self, screen):
        # Clear the screen
        screen.fill((0, 0, 0))
        
        # Render text and buttons for difficulty selection
        font = pygame.font.Font(None, 36)
        easy_text = font.render("Easy", True, (255, 255, 255))
        medium_text = font.render("Medium", True, (255, 255, 255))
        hard_text = font.render("Hard", True, (255, 255, 255))

        screen.blit(easy_text, (200, 100))
        screen.blit(medium_text, (200, 200))
        screen.blit(hard_text, (200, 300))

         # Highlight the selected difficulty
        if self.difficulty == "Easy":
            pygame.draw.rect(screen, (255, 0, 0), (180, 100, 20, 40), 2)
        elif self.difficulty == "Medium":
            pygame.draw.rect(screen, (255, 0, 0), (180, 200, 20, 40), 2)
        elif self.difficulty == "Hard":
            pygame.draw.rect(screen, (255, 0, 0), (180, 300, 20, 40), 2)
