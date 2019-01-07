import pygame
 
w = h = 500
screen = pygame.display.set_mode((w+1, h+1))
clock = pygame.time.Clock()
running = True
size = 250
step = 10
color = 255, 255, 255
for x in range(0, size+1, step):
    pygame.draw.line(screen, color, (0, size-x), (x, 0))
    pygame.draw.line(screen, color, (w-(size-x), 0), (w, x))
    pygame.draw.line(screen, color, (w, h-(size-x)), (w-x, h))
    pygame.draw.line(screen, color, (250-x, h), (0, h-x))
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick()
