# Example file showing a basic pygame "game loop"
from player import Player
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player = Player()


# Create the font (only needs to be done once)
font = pygame.font.SysFont(None, 25)
text = font.render( "Press 'A' or 'S' or 'D' or 'F' to test animations", True, (255, 255, 255))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # UPDATING PLAYER HERE
    # ---------------------------------
    player.update(dt)
    # ---------------------------------

    # PAINTING PLAYER HERE
    # ---------------------------------
    player.draw(screen)
    # ---------------------------------

    screen.blit(text, (1280/2-150, 100))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()