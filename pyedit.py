import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 680
HEIGHT = 320
FPS = 60
FONT_SIZE = 24
BACKSPACE_THRESHOLD = 15
text = [""]
curLine = 0

# todo:
# 1) cursor
# 2) allow for holding any key arbitrary length

def main():
    global text
    global curLine
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("pyEdit")

    font = pygame.font.SysFont("consolas", FONT_SIZE)

    backspace_ticks = 0
    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    text[curLine] += '    '
                elif event.key == pygame.K_RETURN:
                    text.append('')
                    curLine += 1
                elif event.key == pygame.K_BACKSPACE:
                    print(event.key)
                    handle_backspace()
                    backspace_ticks = 1
                else:
                    text[curLine] += event.unicode
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    backspace_ticks = 0

        screen.fill(WHITE)

        if backspace_ticks > 0:
            backspace_ticks += 1

        if backspace_ticks > BACKSPACE_THRESHOLD:
            handle_backspace()

        for i in range(curLine + 1):
            label = font.render(text[i], 1, BLACK)
            screen.blit(label, (0, FONT_SIZE * i))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


def handle_backspace():
    global curLine
    global text
    if len(text[curLine]) == 0 and curLine != 0:
        del text[curLine]
        curLine -= 1
    else:
        text[curLine] = text[curLine][0:-1]


if __name__ == "__main__":
    main()