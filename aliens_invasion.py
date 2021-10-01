import sys
import pygame

from settings import Settings
from ship import Ship

class AliensInvasion:
    """Overall class to manage game assets & behaviour."""

    def __init__(self):
        """Initialize the game & create game resources."""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien's Invasion")

        self.ship = Ship(self)

    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            
            pygame.display.flip()


if __name__ == "__main__":
    ai = AliensInvasion()
    ai.run_game()
