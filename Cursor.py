import pygame
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Cursor:
    def __init__(self, x, y, surface, font_width, font_height, camera):
        self.x = x
        self.y = y
        self.surface = surface
        self.width = font_width
        self.height = font_height - 1
        self.camera = camera
        self.mode = 'command'
        self.cur_color = BLUE

    def set_mode(self, mode):
        self.mode = mode
        if self.mode == 'command':
            self.cur_color = BLUE
        else:
            self.cur_color = RED

    def draw(self):
        pygame.draw.rect(self.surface, self.cur_color, [self.x * self.width - self.camera.x * self.width,
                                                        self.y * self.height - self.camera.y * self.height,
                                                        self.width,
                                                        self.height])
