import pygame
from constants import *
from circleshape import *
from player import *



player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

def main():
    pygame.init()
    game = True
    gameClock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while game == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = gameClock.tick(60) / 1000

        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        
        pygame.display.flip()

        # gameClock.tick(60)
        # print(dt)


if __name__ == "__main__":
    main()
