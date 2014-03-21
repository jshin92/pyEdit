import pygame
from Cursor import Cursor
from Text import Text
WHITE = (255, 255, 255)
WIDTH = 680
HEIGHT = 320
FPS = 60
FONT_SIZE = 24

# todo:
# 1) camera for moving type off screen


def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("pyEdit")

    font = pygame.font.SysFont("consolas", FONT_SIZE)
    font_size = pygame.font.Font.size(font, "a")
    done = False
    cursor = Cursor(0, 0, screen, font_size[0], font_size[1])

    clock = pygame.time.Clock()
    text = Text(cursor, font, FONT_SIZE, screen)
    while not done:
        for event in pygame.event.get():
            if text.handle_event(event):
                done = True

        screen.fill(WHITE)

        text.check_ticks()
        text.draw()

        cursor.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()