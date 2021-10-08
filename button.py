import pygame.font

class Button:
    """A class to manage the botton elements."""

    def __init__(self, ai_game, msg):
        """Initialise button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.btn_color = (170, 150, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """Turn msg into a rendered image & center text on the btn."""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.btn_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        """Draw blank btn & then draw msg."""
        self.screen.fill(self.btn_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

