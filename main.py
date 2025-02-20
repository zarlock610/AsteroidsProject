import pygame
from constants import *
from player import *
from circleshape import *

pygame.init()
clock = pygame.time.Clock()
dt = 0

def main():
    while True:
        for event in pygame.event.get():#this block allows x to close
            if event.type == pygame.QUIT:
                return
        print("Starting asteroids!")
        print("Screen width: 1280")
        print("Screen height: 720")
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill((0,0,0))
        dt = clock.tick(60) / 1000
        human_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
        human_player.draw(screen)
        pygame.display.flip()

if __name__=="__main__":
    main()

