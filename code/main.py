import pygame
import random
from os.path import join


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("images", "player.png")).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.speed = 300
        self.direction = pygame.math.Vector2()
        

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        atk_btn = pygame.key.get_just_pressed()
        if atk_btn[pygame.K_SPACE]:
            print("Fire Laser")


class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surface):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_frect(center = (random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)))


class Meteor(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("images", "meteor.png")).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))


class Laser(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("images", "laser.png")).convert_alpha()
        self.rect = self.image.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))
        #self.rect.y -= 0.1 I guess its not working here


#General setup
pygame.init() #Initialize pygame

#Create window
WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 680
pygame.display.set_caption("Space Defender")
screen_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True

clock = pygame.time.Clock() # helps framerate

# Draw order is a must
sprites = pygame.sprite.Group()

star_surf = pygame.image.load(join("images", "star.png")).convert_alpha()
# Helps on creating stars multiple times
for i in range(20):
    Star(sprites, star_surf)

meteor = Meteor(sprites)
player = Player(sprites)
laser = Laser(sprites)

while running:
    dt = clock.tick() / 1000 #framerate
    #print(clock.get_fps())

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Updates the game
    sprites.update(dt)

    # Draw the game
    screen_display.fill("black")
    sprites.draw(screen_display)
    
    pygame.display.update()

pygame.quit()