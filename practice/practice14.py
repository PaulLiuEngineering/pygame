import pygame

dis = 1

class Worm:
    def __init__(self, surface, x, y, length):
        self.surface = surface
        self.x = x
        self.y = y
        self.length = length
        self.xdir = 0
        self.ydir = -dis
        self.body = []
        self.crashed = 0

    def key_event(self, event):
        if event.key == pygame.K_w:
            self.xdir = 0
            self.ydir = -dis
        elif event.key == pygame.K_s:
            self.xdir = 0
            self.ydir= dis
        elif event.key == pygame.K_a:
            self.xdir = -dis
            self.ydir = 0
        elif event.key == pygame.K_d:
            self.xdir = dis
            self.ydir = 0
    
    def move(self):
        self.x += self.xdir
        self.y += self.ydir
        if(self.x, self.y) in self.body:
            self.crashed = 1
        self.body.insert(0,(self.x,self.y))
        if len(self.body) > self.length:
            self.body.pop()
    
    def draw(self):
        for x,y in self.body:
            self.surface.set_at((int(x),int(y)),(255,255,255))


width = 1200
height = 800

screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = 1

worm = Worm(screen, width/2, height/2, 200)

while running:
    screen.fill((0,0,0))
    worm.move()
    worm.draw()


    if worm.crashed == 1 or worm.x <=0 or worm.x >=width or worm.y<= 0 or worm.y>=height:
        print("Crash")
        running = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == pygame.KEYDOWN:
           worm.key_event(event)
    pygame.display.flip()
    clock.tick(240)
