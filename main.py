import pygame
import os
from constants import *
from player import Player


def main():
    """if "DISPLAY" in os.environ:  # Run audio only if DISPLAY is set
        pygame.mixer.init()
    else:
        print("Audio initialization skipped in headless mode.")"""
    
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.timeClock()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    dt = 0




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()