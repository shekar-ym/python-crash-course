import sys
import pygame
from blue_settings import BlueSettings
from jet import Jet

class BattleBlue:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = BlueSettings()
        
        self.screen = pygame.display.set_model((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Battle of Blues")

        self.jet = Jet(self)


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)


    def _check_events(self):
        """Respond to keypreses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.jet.blitme()

        pygame.display.flip()


if __name__ == '__main_':
    #Make a game instance and run the game.abs
    bb = BattleBlue()
    bb.run_game()