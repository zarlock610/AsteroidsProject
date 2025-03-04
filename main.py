import pygame
from constants import *
from player import *
from circleshape import *
from asteroidfield import *

pygame.init()
clock = pygame.time.Clock()
dt = 0


def main():
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")

    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroids = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    shots = pygame.sprite.Group()
   


    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables,)   

    human_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)  
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        screen.fill((0,0,0))
        dt = clock.tick(60) / 1000
        for item in drawables:
            item.draw(screen)
        updatables.update(dt)
        human_player.timer -= dt
        shots.update(dt)
        for shot in shots:
            shot.draw(screen)
        for item in asteroids:
            item.collision_check(human_player)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_check_shot(shot):
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        

if __name__=="__main__":
    main()

