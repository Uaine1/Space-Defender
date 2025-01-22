import pygame
import random
from os.path import join

#General setup
pygame.init() #Initialize pygame
#Create window
WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 720
pygame.display.set_caption("Space Defender")
screen_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True

#Plaim surface
surface = pygame.Surface((100,200))
surface.fill("cyan")

#Importng an image
player = pygame.image.load(join("images", "player.png")).convert_alpha()
xplayer = 100

#Stars
star = pygame.image.load(join("images", "star.png")).convert_alpha()
star_pos = [(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)) for i in range(20)]

while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game
    # Draw order is a must
    screen_display.fill("black")
    
    for pos in star_pos:
        screen_display.blit(star, pos)

    screen_display.blit(player, (xplayer, 150))
    xplayer += 0.3

    pygame.display.update()

pygame.quit()