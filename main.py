import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidField import *

def main():
    pygame.init()
    dt = 0 # Delta time
    gameClock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Assign containers to classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Instantiate player and field that spawns asteroids
    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Print Game Start info
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Game loop
    while game == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = gameClock.tick(60) / 1000 # Regulate tick rate

        screen.fill("black") # Zero the screen to black
        updatable.update(dt) # Update updatables

        for asteroid in asteroids: # Check for collision with player
            if asteroid.collision(player):
                print("Game Over!")
                pygame.quit()

        for entity in drawable: # Draw drawables to screen (player and asteroids)
            entity.draw(screen)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
