import pygame
from random import randint, uniform
from os.path import join


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("images", "player.png")).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.speed = 300
        self.direction = pygame.math.Vector2()

        # Cooldown Timer
        self.can_atk =True          # atk = Attack
        self.shot_atk_timer = 0     # cd = Cooldown
        self.atk_cd_dur = 400       # dur = Duration
    

    def atk_timer(self):
        if not self.can_atk:
            current_time = pygame.time.get_ticks()
            if current_time - self.shot_atk_timer >= self.atk_cd_dur:
                self.can_atk = True
        

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        atk_btn = pygame.key.get_just_pressed()
        if atk_btn[pygame.K_SPACE] and self.can_atk:
            Laser(laser_surf, self.rect.midtop, sprites)
            self.can_atk = False
            self.shot_atk_timer = pygame.time.get_ticks()

        self.atk_timer()

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surface):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_frect(center = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))

class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = pos)
        self.start_time = pygame.time.get_ticks()
        self.life_time = 3000
        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(400,500)

    
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if self.rect.bottom > WINDOW_HEIGHT:
            self.kill()
        """if pygame.time.get_ticks() - self.start_time >= self.life_time:
            self.kill()"""

class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf 
        self.rect = self.image.get_frect(midbottom = pos)
        #self.rect.y -= 0.1 I guess its not working here


    def update(self, dt):
        self.rect.centery -= 400 * dt
        if self.rect.bottom < 0:
            self.kill()


#General setup
pygame.init() #Initialize pygame

#Create window
WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 680
pygame.display.set_caption("Space Defender")
screen_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
clock = pygame.time.Clock() # helps framerate

#Imports
star_surf = pygame.image.load(join("images", "star.png")).convert_alpha()
laser_surf = pygame.image.load(join("images", "laser.png")).convert_alpha()
meteor_surf = pygame.image.load(join("images", "meteor.png")).convert_alpha()

# Sprites - Draw order is a must
sprites = pygame.sprite.Group()

# Helps on creating stars multiple times
for i in range(20):
    Star(sprites, star_surf)

player = Player(sprites)

# Meteor (Interval Timer)
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

while running:
    dt = clock.tick() / 1000 #framerate
    #print(clock.get_fps())

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == meteor_event:
            x, y = randint(0, WINDOW_WIDTH), randint(-200, -100)
            Meteor(meteor_surf, (x,y), sprites)

    # Updates the game
    sprites.update(dt)

    # Draw the game
    screen_display.fill("black")
    sprites.draw(screen_display)
    
    pygame.display.update()

pygame.quit()