import pygame 
from constants import *

def main():
    pygame.init() 

    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720") 

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    BLACK = (0, 0, 0)

    running = True

    while running:
     for event in pygame.event.get():
      if event.type == pygame.QUIT:
       return
      screen.fill(BLACK)
      pygame.display.flip() 

if __name__ == "__main__":
    main()
