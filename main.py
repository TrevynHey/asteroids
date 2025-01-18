# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (updatable,shots,drawable)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for object in updatable:
            object.update(dt)
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        for object in asteroids:
            if player.collide(object):
                print("Game over!")
                return

if __name__ == "__main__":
    main()