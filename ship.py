from time import perf_counter
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship & set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.img = pygame.image.load("images/ship.bmp")
        self.image = pygame.transform.scale(self.img, (100, 88))
        self.rect = self.image.get_rect()

        # Position the ship
        self.positioning_ship()

        self.moving_up = False
        self.moving_down = False


    def positioning_ship(self):
        """Center the ship on the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)


    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y


    def blitme(self):
        self.screen.blit(self.image, self.rect)




