# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import * 
def main():
    
    pygame.init()
    player1 = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0
    
    while True:
        
        screen.fill('black')
        player1.draw(screen)
        player1.update(delta_time)
        pygame.display.flip()
        clock.tick(60)
        
        delta_time = clock.tick(60) / 100
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    main()
