import pygame

width = 640
height = 400

x = width/2
y = height/2

dir_x = 0
dir_y = 0

screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = 1

while running:
    x+=dir_x
    y+=dir_y

    if x <=0 or x >=width or y<= 0 or y>=height:
        print("Crash")
        running = 0
    
    screen.fill((0,0,0))
    screen.set_at((int(x),int(y)),(255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dir_x = 0
                dir_y = -0.1
            elif event.key == pygame.K_DOWN:
                dir_x = 0
                dir_y = 0.1
            elif event.key == pygame.K_LEFT:
                dir_x = -0.1
                dir_y = 0
            elif event.key == pygame.K_RIGHT:
                dir_x = 0.1
                dir_y = 0
        pygame.display.flip()
        clock.tick(120)

