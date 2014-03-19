import pygame
from Cursor import Cursor
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 680
HEIGHT = 320
FPS = 60
FONT_SIZE = 24
KEY_THRESHOLD = 15
text = [""]
curLine = 0

# todo:
# 1) cursor
# 2) camera for moving type off screen


def main():
    global text
    global curLine
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("pyEdit")

    font = pygame.font.SysFont("consolas", FONT_SIZE)
    font_size = pygame.font.Font.size(font, "a")
    cur_ticks = 0
    done = False
    cursor = Cursor(0, 0, screen, font_size[0], font_size[1])

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                cur_ticks = 1
                cur_key = event.key
                cur_unicode = event.unicode
                handle_key_input(event.key, event.unicode, cursor)
            elif event.type == pygame.KEYUP:
                cur_ticks = 0

        screen.fill(WHITE)

        if cur_ticks > 0:
            cur_ticks += 1

        if cur_ticks > KEY_THRESHOLD:
            handle_key_input(cur_key, cur_unicode, cursor)

        for i in range(curLine + 1):
            label = font.render(text[i], 1, BLACK)
            screen.blit(label, (0, FONT_SIZE * i))

        cursor.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


def handle_key_input(key, unicode, cursor):
    global curLine
    global text
    if key == pygame.K_TAB:
        text[curLine] += '    '
    elif key == pygame.K_RETURN:
        text.append('')
        curLine += 1
        cursor.y += 1
        cursor.x = 0
    elif key == pygame.K_BACKSPACE:
        handle_backspace(cursor)
        cursor.x -= 1
    else:
        text[curLine] += unicode
        if key != pygame.K_LSHIFT and key != pygame.K_RSHIFT:
            cursor.x += 1


def handle_backspace(cursor):
    global curLine
    global text
    if len(text[curLine]) == 0 and curLine != 0:
        del text[curLine]
        curLine -= 1
    else:
        text[curLine] = text[curLine][0:-1]


if __name__ == "__main__":
    main()