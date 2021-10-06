import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien & set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the image of alien 1 and set its position.
        self.img = pygame.image.load("images/alien1.bmp")
        # Rescale the size of an alien
        self.image = pygame.transform.scale(self.img, (60, 48))
        self.rect = self.image.get_rect()

        # Set the position of an alien at the right top with a gap
        # self.rect.right = self.screen_rect.right
        # self.rect.top = self.screen_rect.top + 20
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # # Load the image of alien 2 and set its position.
        # self.image_2 = pygame.image.load("images/alien2.bmp")
        # self.rect_2 = self.image_2.get_rect()
        # self.rect_2.x = self.rect_2.width
        # self.rect_2.y = self.rect_2.height
        # self.x_2 = float(self.rect_2.x)


    def check_edges(self):
        """Return True if alien is at the edges of the screen."""
        screen_rect = self.screen.get_rect()
        if (self.rect.bottom >= screen_rect.bottom) or (self.rect.top >= 0):
            return True


    def update(self):
        """Move the alien to up or down."""
        self.y += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.y = self.y
