import pygame
import sys

# Init pygame module
pygame.init()

# TODO: Setup game variables

# Setup screen variables
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
speed = [2, 2]
white = (255, 255, 255)

# Setup player variables
bike = pygame.image.load("bikeright.png")
bikerect = bike.get_rect()

# Main game loop
while True:
    # Event manager
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Move the player around the screen
        bikerect = bikerect.move(speed)

        # Move the player based on users input
        if bikerect.left < 0 or bikerect.right > width:
            speed[0] = -speed[0]
        if bikerect.top < 0 or bikerect.bottom > height:
            speed[1] = -speed[1]

    # Create game window
    screen.fill(white)
    screen.blit(bike, bikerect)
    pygame.display.flip()
