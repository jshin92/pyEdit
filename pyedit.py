import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 680
HEIGHT = 320
FPS = 60

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("pyEdit")

text = [""]
font = pygame.font.SysFont("monospace", 15)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            text[0] = text[0] + event.unicode
            print(event.unicode)


    screen.fill(WHITE)

    label = font.render(text[0], 1, BLACK)
    screen.blit(label, (0, 0))
    pygame.display.flip()

    clock.tick(FPS)


pygame.quit()