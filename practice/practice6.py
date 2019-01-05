import pygame,sys

screen = pygame.display.set_mode((640, 480))
black = (0, 0, 0)
blue = (0, 0, 255)
white = (255,255,255)

while 1:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        sys.exit()
    screen.fill(black)
    pygame.draw.line(screen, blue, (0, 0), (639, 479))
    pygame.draw.aaline(screen, blue, (639, 0), (0, 479))
    pygame.display.flip()
