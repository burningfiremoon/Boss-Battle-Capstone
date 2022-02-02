## download -m pip install -U pygame --user

# imports
import sys, pygame, random

pygame.init()
# -----FPS-----
FPS = 60
FramePerSec = pygame.time.Clock()

# variables
Game = True

# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# display/screen
Display = pygame.display.set_mode((1920, 1080))
Display.fill(BLACK)
# main loop
while True:

    pygame.display.update()
    if not Game:
        pygame.quit()
        sys.exit()
