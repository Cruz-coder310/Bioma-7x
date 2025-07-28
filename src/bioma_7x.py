import pygame

import sys

from settings import Options

from ship import Nave

class VideoGame:
    """Manages the game, including the screen, colors, and key components."""
    def __init__(self):
        """Initialize the game & create game resources""" 
        pygame.init()
        self.reloj = pygame.time.Clock()
        self.options = Options()
        self.pantalla = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.options.pantalla_ancho = self.pantalla.get_rect().width
        self.options.pantalla_alto = self.pantalla.get_rect().height
        pygame.display.set_caption("Bioma 7X")
        self.nave = Nave(self)


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.nave.navigate()
            self._update_screen()
            self.reloj.tick(60)


    def _check_events(self):
        """Respond to keypresses."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._process_keydown(event)
            elif event.type == pygame.KEYUP:
                self._process_keyup(event)

    def _process_keydown(self, event):
        """Handles keydown events & updates movement flags."""
        if event.key == pygame.K_RIGHT:
            self.nave.flag_derecha = True
        elif event.key == pygame.K_LEFT:
            self.nave.flag_izquierda = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _process_keyup(self, event):
        """Handles keyup events & reserts movement flags."""
        if event.key == pygame.K_RIGHT:
            self.nave.flag_derecha = False
        elif event.key == pygame.K_LEFT:
            self.nave.flag_izquierda = False


    def _update_screen(self):
        """ Update images on the screen, & flip to the new screen."""
        self.pantalla.fill(self.options.color_pnt)
        # Draw the ship onto the screen
        self.nave.ship_visualize()
        pygame.display.flip()


if __name__ == "__main__":
    bioma = VideoGame()
    bioma.run_game()
