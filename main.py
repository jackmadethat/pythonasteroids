import pygame
from constants import *

game = True
gameClock = pygame.time.Clock()
dt = 0

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while game == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()
        gameClock.tick(60)
        dt = gameClock.tick() / 1000
        # print(dt)


if __name__ == "__main__":
    main()
