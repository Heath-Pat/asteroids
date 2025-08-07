# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import * 
def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    all_asteroids = pygame.sprite.Group()
     
    Asteroid.containers = (all_asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player1 = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))
    
    delta_time = 0
    
    while True:
        
        screen.fill('black')
        clock.tick(50)

        for obj in drawable:
            obj.draw(screen)
        
        updatable.update(delta_time)
        for obj in all_asteroids:
            if obj.check_collision(player1):
                print('Game over!')
                sys.exit('Exiting')
        
        pygame.display.flip()
        
        
        delta_time = clock.tick(60) / 100
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    main()
