import pygame

# Game parameters
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800
BG_COLOR = 150, 150, 80
CREEP_FILENAMES = [
    'bluecreep.png',
    'pinkcreep.png',
    'graycreep.png']
N_CREEPS = 20

class Creep(Sprite):
    """ A creep sprite that bounces off walls and changes its
        direction from time to time.
    """
    def __init__(self, screen, img_filename, init_position,init_direction, speed):
        """ Create a new Creep.

            screen:
                The screen on which the creep lives (must be a
                pygame Surface object, such as pygame.display)

            img_filaneme:
                Image file for the creep.

            init_position:
                A vec2d or a pair specifying the initial position
                of the creep on the screen.

            init_direction:
                A vec2d or a pair specifying the initial direction
                of the creep. Must have an angle that is a
                multiple of 45 degres.

            speed:
                Creep speed, in pixels/millisecond (px/ms)
        """

pygame.init()
screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
clock = pygame.time.Clock()

# Create N_CREEPS random creeps.
creeps = []
for i in range(N_CREEPS):
    creeps.append(Creep(screen,
        choice(CREEP_FILENAMES),
        (randint(0, SCREEN_WIDTH),randint(0, SCREEN_HEIGHT)), (choice([-1, 1]),choice([-1, 1])),0.1))


while 1:
    # Limit frame speed to 50 FPS
    #
    time_passed = clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()

    # Redraw the background
    screen.fill(BG_COLOR)

    # Update and redraw all creeps
    for creep in creeps:
        creep.update(time_passed)
        creep.blitme()

    pygame.display.flip()