import pygame
import random

width = 640
height = 400

screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = 1
# screen.fill((255,255,255))
while running:
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0

    screen.set_at((x,y),(red,green,blue))
    # screen.fill((0,0,0))
    pygame.display.flip()
    clock.tick(2000)