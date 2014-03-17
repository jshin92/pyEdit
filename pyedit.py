import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 680
HEIGHT = 320
FPS = 60
FONT_SIZE = 24

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("pyEdit")

text = [""]
curLine = 0
font = pygame.font.SysFont("consolas", FONT_SIZE)

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
            else:
                text[curLine] = text[curLine] + event.unicode

    screen.fill(WHITE)

    for i in range(curLine + 1):
        label = font.render(text[i], 1, BLACK)
        screen.blit(label, (0, FONT_SIZE * i))
    pygame.display.flip()

    clock.tick(FPS)


pygame.quit()