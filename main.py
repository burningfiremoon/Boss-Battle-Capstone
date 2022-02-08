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
WIDTH = 1920
HEIGHT = 1080

# display/screen
Display = pygame.display.set_mode((WIDTH, HEIGHT))
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
    def update(self):
        "Player movement"
        self.calc_grav()

        # ___Hit Reg___
        # __Horizontal__
        self.rect.x += self.vel_x

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we're moving right, set our right side to the left side of the item we hit
            # opposite for moving left; set left side to the right side of the item we hit
            if self.vel_0:
                self.rect.right = block.rect.left
            elif self.vel_x < 0:
                self.rect.left = block.rect.right

        # __Vertical__
        self.rect.y += self.vel_y

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset position based on the top/bottom of the object
            if self.vel_y >0:
                self.rect.bottom = block.rect.top
            elif self.vel_y < 0:
                self.recct.top - block.rect.bottom
            # Stop vertical movement when we're in the vertical hit box of objects in list
            self.vel_y = 0
        if self.rect.right >= WIDTH - 8:
            self.rect.right = WIDTH - 9
        elif self.rect.x < 8:
            self.rect.x = 9

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT - 9
        elif self.rect.y < 8:
            self.rect.y = 9

    def calc_grav(self):
        """The Earth is flat things just fall"""
        if self.vel_y == 0:
            self.vel_y = 1
        else:
            self.vel_y += .35

        # See if we are on the ground.
        if self.rect.y >= HEIGHT - self.rect.height and self.vel_y >= 0:
            self.vel_y = 0
            self.rect.y = HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= HEIGHT:
            self.vel_y = -10

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.vel_x = -6
        self.facing_right = False

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.vel_x = 6
        self.facing_right = True

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.vel_x = 0




# main loop
while True:

    pygame.display.update()
    if not Game:
        pygame.quit()
        sys.exit()
