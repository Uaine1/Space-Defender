import pygame
import random
from os.path import join

#General setup
pygame.init() #Initialize pygame

#Create window
WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 680
pygame.display.set_caption("Space Defender")
screen_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
clock = pygame.time.Clock() # helps framerate

#Plaim surface
surface = pygame.Surface((100,200))
surface.fill("cyan")

#Importss
player = pygame.image.load(join("images", "player.png")).convert_alpha()
player_rect = player.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2(1,1)
player_speed = 300

#Star
star = pygame.image.load(join("images", "star.png")).convert_alpha()
star_pos = [(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)) for i in range(20)]

#Meteor
meteor = pygame.image.load(join("images", "meteor.png")).convert_alpha()
meteor_rect = meteor.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

#Laser
laser = pygame.image.load(join("images", "laser.png")).convert_alpha()
laser_rect = laser.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))

while running:
    dt = clock.tick() / 1000 #framerate
    #print(clock.get_fps())

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game
    # Draw order is a must
    screen_display.fill("black")
    
    for pos in star_pos:
        screen_display.blit(star, pos)

    screen_display.blit(meteor, meteor_rect)
    screen_display.blit(laser, laser_rect)

    # Player movements
    if player_rect.bottom >= WINDOW_HEIGHT or player_rect.top <= 0:
        player_direction.y *= -1

    if player_rect.right >= WINDOW_WIDTH or player_rect.left <= 0:
        player_direction.x *= -1

    player_rect.center += player_direction * player_speed * dt  

    screen_display.blit(player, player_rect)
    #xplayer += 0.3
    
    pygame.display.update()

pygame.quit()