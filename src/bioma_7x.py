import pygame

import sys

from settings import Settings

from ship import Nave

class VideoGame:
    """Manages the game, including the screen, colors, and key components."""

    def __init__(self):
        """Initialize the game & create game resources""" 
        pygame.init()

        self.reloj = pygame.time.Clock()
        self.settings = Settings()
        self.pantalla = pygame.display.set_mode(
            (self.settings.pantalla_ancho, self.settings.pantalla_alto)
        )
        pygame.display.set_caption("Bioma 7X")
        self.ship = Nave(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

            self.reloj.tick(60)


    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """ Update images on the screen, & flip to the new screen."""
        self.pantalla.fill(self.settings.color_pnt)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == "__main__":
    pth = VideoGame()
    pth.run_game()
