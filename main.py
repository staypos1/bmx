import pygame
import sys

# Init pygame module
pygame.init()

# Setup screen variables
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
speed = [2, 2]
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

        # Move the player around the screen
        boxrect = boxrect.move(speed)

        # Move the player based on users input
        if boxrect.left < 0 or boxrect.right > width:
            speed[0] = -speed[0]
        if boxrect.top < 0 or boxrect.bottom > height:
            speed[1] = -speed[1]

    # Create game window
    screen.fill(white)
    screen.blit(box, boxrect)
    pygame.display.flip()
