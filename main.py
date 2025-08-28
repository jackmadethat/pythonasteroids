import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidField import *
from shot import *

def main():
    pygame.init()
    dt = 0 # Delta time
    gameClock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign containers to classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

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

        for asteroid in asteroids: 
            if asteroid.collision(player): # Check for collision with player
                print("Game Over!")
                pygame.quit()
            for shot in shots:
                if asteroid.collision(shot): # Check for collision with shot
                    asteroid.split()
                    shot.kill()


        for entity in drawable: # Draw drawables to screen (player and asteroids)
            entity.draw(screen)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
