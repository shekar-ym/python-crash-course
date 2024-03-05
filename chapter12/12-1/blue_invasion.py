import sys
import pygame
from settings import Settings
from jet import Jet

class BlueInvasion:
    """Overall class to manage game assets and beviour."""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Blue Invasion")

        self.jet = Jet(self)
    
    def run_game(self):
        """Start the main loop for the gamee."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.jet.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance and run the game.
    bi = BlueInvasion()
    bi.run_game()