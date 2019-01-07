import pygame
class Illini:
    def __init__(self,x,y,health):
        self.x = x
        self.y = y
        self.health = health
        self.xdir = 0
        self.ydir = 0
        self.jump = 1
width = 1200
height = 800
running = 1
screen = pygame.display.set_mode(width,height)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0