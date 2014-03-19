import constants
import pygame
RED = (255, 0, 0)


class Cursor:
    def __init__(self, x, y, surface):
        self.x = x
        self.y = y
        self.surface = surface
        self.width = constants.FONT_SIZE/2
        self.height = constants.FONT_SIZE

    def draw(self):
        pygame.draw.rect(self.surface, RED, [self.x * self.width, self.y * self.height, self.width, self.height])
