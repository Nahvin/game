import pygame
import os
from constants import *
from player import Player


def main():
    if "DISPLAY" in os.environ:  # Run audio only if DISPLAY is set
        pygame.mixer.init()
    else:
        print("Audio initialization skipped in headless mode.")
    pygame.init()


    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()
        player.draw(screen)


if __name__ == "__main__":
    main()