import pygame 
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init() 

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable, )
    AsteroidField()

    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720") 

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip() 
        
        
        dt = clock.tick(60) / 1000  # Delta time in seconds.
        

    
if __name__ == "__main__":
    main()
