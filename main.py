import pygame
import sys

# Init pygame module
pygame.init()

# Setup screen variables
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
speed = (2, 2)
white = (255, 255, 255)

# Setup player variables
box = pygame.image.load("box.png")
boxrect = box.get_rect()

# Main game loop
while True:
    # Event manager
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Create game window
    screen.fill(white)
    screen.blit(box, boxrect)
    pygame.display.flip()
