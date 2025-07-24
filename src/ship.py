import pygame

class Nave:
    """ A class to manage the Ship """

    def __init__(self, p_game):
        """Initialize the ship and set its starting position"""

        self.pantalla_completa = p_game.pantalla
        self.rect_pantalla = p_game.pantalla.get_rect()

        self.imagen = pygame.image.load("../images/ship.bmp").convert()
        self.imagen.set_colorkey((255, 255, 255))
        ancho = self.imagen.get_width() // 7
        alto = self.imagen.get_height() // 7

        self.imagen_scala = pygame.transform.scale(self.imagen,(ancho, alto))
        self.rect_ship = self.imagen_scala.get_rect()

        self.rect_ship.midbottom = self.rect_pantalla.midbottom


    def blitme(self):
        """Draw the ship at its current lacation."""
        self.pantalla_completa.blit(self.imagen_scala, self.rect_ship)
