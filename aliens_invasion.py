import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AliensInvasion:
    """Overall class to manage game assets & behaviour."""

    def __init__(self):
        """Initialize the game & create game resources."""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        # Fullscreen mode
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien's Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()


    # Starting the game.
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()


    def _check_events(self):
        """Respond to keypresses & mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False


    # Methods for bullets.
    def _fire_bullet(self):
        """Create a new bullet & add it to the bullet group."""
        if len(self.bullets) < self.settings.bullet_limits:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Update position of bullets & get rid of old bullets."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)


    # Methods for aliens
    def _create_fleet(self):
        """Create the fleet of aliens."""
        alien = Alien(self)
        alien_height, alien_width = alien.rect.size
        available_space_y = self.settings.screen_height - (2 * alien_height)
        number_aliens_y = available_space_y // (2 * alien_height)

        # Determine the number of columns of aliens
        ship_width = self.ship.rect.width
        available_space_x = (
            self.settings.screen_width - (2 * alien_width) - ship_width)
        number_cols = available_space_x // (alien_width + 30)

        # Create the full fleet of aliens
        for col_number in range(number_cols):
            for alien_number in range(number_aliens_y):
                self._create_alien(alien_number, col_number)
            

    def _create_alien(self, alien_number, col_number):
        """Create an alien & place it in the column."""
        alien = Alien(self)
        alien_height, alien_width = alien.rect.size

        alien.y = alien_height + 2 * alien_height * alien_number
        alien.rect.y = alien.y
        alien.rect.right = (self.ship.rect.width * 3) + (alien_width * col_number)
        self.aliens.add(alien)


    def _check_fleet_edges(self):
        """Respond appropriately if any aliesn have reached an edges."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Move the entire fleet to the left & then go up."""
        for alien in self.aliens.sprites():
            alien.rect.x += self.settings.fleet_speed_left
        self.settings.fleet_direction *= -1


    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

    # A method to draw and update objects in the game.
    def _update_screen(self):
        """Update images on the screen & flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        
        pygame.display.flip()


if __name__ == "__main__":
    ai = AliensInvasion()
    ai.run_game()
