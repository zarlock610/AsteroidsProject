import pygame
from constants import *
from player import *
from circleshape import *

pygame.init()
clock = pygame.time.Clock()
dt = 0

def main():
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updatables, drawables) 

    human_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)  

    while True:
        for event in pygame.event.get():#this block allows x to close
            if event.type == pygame.QUIT:
                return
        
        
        screen.fill((0,0,0))
        dt = clock.tick(60) / 1000
        for item in drawables:
            item.draw(screen)
        updatables.update(dt)
        pygame.display.flip()
        

if __name__=="__main__":
    main()

