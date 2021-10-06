class Settings:
    """A class to store all settings for Alien's Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (100, 100, 200)

        self.bullet_width = 15
        self.bullet_height = 7
        self.bullet_color = (60, 60, 60)
        self.bullet_limits = 3

        self._speed_settings()

    
    def _speed_settings(self):
        """A method to control the speed of ship, bullet & alien."""
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed = 1.0
        self.fleet_speed_left = 1.0
        # fleet_direction of 1 means down; -1 means up
        self.fleet_direction = 1