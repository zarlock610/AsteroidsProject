import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
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
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__=="__main__":
    main()

