import pygame

dis = 0.02

up = (0,-dis)
down = (0,dis)
left= (-dis, 0)
right = (dis, 0)

class MovingPixel:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.xdir = 0
        self.ydir = 0
    
    def direction(self, dir):
        self.xdir, self.ydir = dir

    def move(self):
        self.x += self.xdir
        self.y += self.ydir
    
    def draw(self, surface):
        surface.set_at((int(self.x),int(self.y)),(255,255,255))

width = 640
height = 400

screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = 1

pixel = MovingPixel(width/2, height/2)

while running:
    pixel.move()
    if pixel.x <=0 or pixel.x >=width or pixel.y<= 0 or pixel.y>=height:
        print("Crash")
        running = 0

    screen.fill((0,0,0))
    pixel.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pixel.direction(up)
            elif event.key == pygame.K_DOWN:
                pixel.direction(down)
            elif event.key == pygame.K_LEFT:
                pixel.direction(left)
            elif event.key == pygame.K_RIGHT:
                pixel.direction(right)
            pygame.display.flip()
        elif event.type == pygame.KEYUP:
            pixel.direction((0,0))
        pygame.display.flip()
        clock.tick(2000)
