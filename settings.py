class Settings:
    """A class to store all settings for Alien's Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (100, 100, 200)

        self.ship_speed = 1.5

        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 7
        self.bullet_color = (60, 60, 60)
