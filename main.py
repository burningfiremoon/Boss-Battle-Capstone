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
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# display/screen
Display = pygame.display.set_mode((1920, 1080))
Display.fill(BLACK)
# ----- Classes ------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # what character looks like
        self.image = pygame.image.load("./Sprites/right_player1-1.png")
        # Hit box
        self.rect = self.image.get_rect()

        # ___Speed of the player___
        self.vel_x = 0
        self.vel_y = 0

        # direction variables and HP
        self.facing_right = True
        self.hp = 3

        # list of objects the sprites cannot walk through
        self.level = None







# main loop
while True:

    pygame.display.update()
    if not Game:
        pygame.quit()
        sys.exit()
