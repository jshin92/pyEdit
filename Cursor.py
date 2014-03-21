import pygame
RED = (255, 0, 0)


class Cursor:
    def __init__(self, x, y, surface, font_width, font_height, camera):
        self.x = x
        self.y = y
        self.surface = surface
        self.width = font_width
        self.height = font_height - 1
        self.camera = camera

    def draw(self):
        pygame.draw.rect(self.surface, RED, [self.x * self.width - self.camera.x * self.width,
                                             self.y * self.height - self.camera.y * self.height,
                                             self.width,
                                             self.height])
