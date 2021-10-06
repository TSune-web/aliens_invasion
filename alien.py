import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien & set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the image of alien 1 and set its position.
        self.image = pygame.image.load("images/alien1.bmp")
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

