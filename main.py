import pygame
import sys

# Init pygame module
pygame.init()

# Setup screen variables
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
black = (0, 0, 0)

# Main game loop
while True:
    # Event manager
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Create game window
    screen.fill(black)
    pygame.display.flip()
