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
        self.last = (0,0)
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
        self.body.insert(0,(self.x,self.y))
        self.x += self.xdir
        self.y += self.ydir

        r,g,b,a = self.surface.get_at((int(self.x),int(self.y)))

        if(r,g,b) != (0,0,0):
            self.crashed = 1
        
        if len(self.body) > self.length:
            self.last = self.body.pop()
        else:
            self.last = self.body[-1]
    
    def draw(self):
        for x,y in self.body:
            self.surface.set_at((int(x),int(y)),(255,255,255))
            self.surface.set_at((int(self.last[0]),int(self.last[1])),(0,0,0))


width = 1200
height = 800

screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = 1

worm = Worm(screen, width/2, height/2, 200)

while running:
    # screen.fill((0,0,0))
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
