import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self,ai_game):
        """Initiate the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and gets its rect.
        self.image = pygame.image.load('/Users/cyelahankamunikris/Documents/chandra-work/python-crash-course/chapter12/12-1/images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

