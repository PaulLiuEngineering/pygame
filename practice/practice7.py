import pygame, sys
x = 0
y = 0
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0,0,0)
xdir = 1
ydir = 1
width = 1000
height = 800
pygame.init()
screen = pygame.display.set_mode((width, height))

while 1:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        sys.exit()
    screen.fill(black)
    pygame.draw.line(screen, red, (0, y), (width-1, y))
    pygame.draw.line(screen, blue, (x, 0), (x, height-1))
    x += xdir
    y += ydir
    if x == 0 or x == width-1: 
        xdir *= -1
    if y == 0 or y == height-1: 
        ydir *= -1
    
    pygame.display.flip()
