import pygame 
from constants import *
from player import *

def main():
    pygame.init() 

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720") 

    
    
    BLACK = (0, 0, 0)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(BLACK)
        player.draw(screen)
        pygame.display.flip() 
        
        
        dt = clock.tick(60) / 1000  # Delta time in seconds.
        

    
if __name__ == "__main__":
    main()
