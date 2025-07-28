import pygame

class Nave:
    """ A class to manage the Ship """

    def __init__(self, p_game):
        """Initialize the ship and set its starting position"""
        # Create instances of the screen & options.
        self.pantalla_completa = p_game.pantalla
        self.rect_pantalla = p_game.pantalla.get_rect()
        self.options = p_game.options

        # Load the ship image and remove its background color.
        self.imagen = pygame.image.load("../images/ship.bmp").convert()
        self.imagen.set_colorkey((255, 255, 255))

        # Resize the image and obtain its positioning rectangle.
        ancho = self.imagen.get_width() // 7
        alto = self.imagen.get_height() // 7
        self.imagen_scala = pygame.transform.scale(self.imagen,(ancho, alto))
        self.rect_ship = self.imagen_scala.get_rect()

        # Set the ship's rect to the center of the screen.
        self.rect_ship.midbottom = self.rect_pantalla.midbottom

        # Store the position as a float for greater precision.
        self.x_location = float(self.rect_ship.x)

        # Flags that control the ship's movement.
        self.flag_derecha = False
        self.flag_izquierda = False

    def navigate(self):
        """
        Adjust the ship's movement depending on
        user input (keydown or keyup events).
        """
        if (
            self.flag_derecha and 
            self.rect_ship.right < self.rect_pantalla.right
        ):
            self.x_location += self.options.speed_nave
        if self.flag_izquierda and self.rect_ship.left > 0:
            self.x_location -= self.options.speed_nave
        # Transfer the smoothed float value to the display position
        self.rect_ship.x = self.x_location


    def ship_visualize(self):
        """Draw the ship at its current lacation."""
        self.pantalla_completa.blit(self.imagen_scala, self.rect_ship)
