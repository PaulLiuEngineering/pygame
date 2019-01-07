import pygame
import random
dis = 1
class Worm:
    def __init__(self, surface):
        self.surface = surface
        self.x = int(surface.get_width()/2)
        self.y = int(surface.get_height()/2)
        self.length = 1
        self.grow_to = 50
        self.xdir = 0
        self.ydir = -dis
        self.body = []
        self.crashed = 0
        self.color = (0, 255, 255)

    def event(self, event):
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

        # r,g,b,a = self.surface.get_at((int(self.x),int(self.y)))

        # if(r,g,b) != (0,0,0):
        #     self.crashed = 1
        self.body.insert(0,(self.x,self.y))
        if(self.grow_to > self.length):
            self.length += 1
        
        if len(self.body) > self.length:
            self.last = self.body.pop()
        # else:
        #     self.last = self.body[-1]
    
    def draw(self):
        for x,y in self.body:
            self.surface.set_at((int(x),int(y)),self.color)
            # self.surface.set_at((int(self.last[0]),int(self.last[1])),(0,0,0))

    def position(self):
        return self.x, self.y

    def eat(self):
        self.grow_to += 25

class Food:
    def __init__(self, surface):
        self.surface = surface
        self.x = random.randint(0,surface.get_width())
        self.y = random.randint(0,surface.get_height())
        self.ps = []
        self.color = (255,255,255)

    def draw(self):
        # self.surface.set_at((int(self.x),int(self.y)),self.color)
        for i in range(25):
            self.ps.insert(0, (int(self.x + i/5),int(self.y + i%5)))
            self.surface.set_at(self.ps[0],self.color)


    def position(self):
        return self.x, self.y

wi = 1000
h = 800
screen = pygame.display.set_mode((wi,h))
clock = pygame.time.Clock()

score = 0
w = Worm(screen)
f = Food(screen)

running = 1
while running:
    screen.fill((0,0,0))
    w.move()
    w.draw()
    f.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == pygame.KEYDOWN:
           w.event(event)

    if w.crashed == 1 or w.x<=0 or w.x>=wi or w.y<=0 or w.y>=h:
        print("Crash")
        running = 0
    elif w.position() in f.ps:
        score += 1
        w.eat()
        print("Score is: %d" % score)
        f = Food(screen)

    pygame.display.flip()
    clock.tick(240)
