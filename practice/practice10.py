import pygame
 
x = y = 0
bgcolor = (0,0,0)
linecolor = (255,255,255)
running = 1
screen = pygame.display.set_mode((640, 400))
red = 0
reddir = 1
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    elif event.type == pygame.MOUSEMOTION:
        x,y = event.pos
    screen.fill(bgcolor)
    pygame.draw.line(screen,(red,0,0),(x,0),(x,399))
    pygame.draw.line(screen,(red,0,0),(0,y),(639,y))
    red += reddir
    if red == 255 or red == 0:
        reddir *= -1
    pygame.display.flip()