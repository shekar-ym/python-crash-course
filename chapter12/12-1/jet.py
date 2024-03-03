import pygame

class Jet:
    """A class to manage a Jet"""

    def __init__(self,bb_game):
        """Initiate the Jet and set its starting position."""
        self.screen = bb_game.screen
        self.screen_rect = bb_game.screen.get_rect()

        #Load the Jet image and gets its rect.
        self.image = pygame.image.load('/Users/cyelahankamunikris/Documents/chandra-work/python-crash-course/chapter12/12-1/images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new Jet at the center of the screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the Jet at its current location."""
        self.screen.blit(self.image,self.rect)

