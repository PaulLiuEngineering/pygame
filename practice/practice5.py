import sys, pygame
pygame.init()

size = width, height = 1000, 800
speed = [0, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = 0
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = 0
    if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
        speed[1] = -2
        speed[0] = 0
    if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
        speed[1] = 2
        speed[0] = 0
    if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
        speed[0] = -2
        speed[1] = 0
    if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
        speed[0] = 2
        speed[1] = 0
    if event.type == pygame.KEYUP and event.key == pygame.K_w:
        speed[1] = 0
        speed[0] = 0
    if event.type == pygame.KEYUP and event.key == pygame.K_s:
        speed[1] = 0
        speed[0] = 0
    if event.type == pygame.KEYUP and event.key == pygame.K_a:
        speed[0] = 0
        speed[1] = 0
    if event.type == pygame.KEYUP and event.key == pygame.K_d:
        speed[0] = 0
        speed[1] = 0
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()