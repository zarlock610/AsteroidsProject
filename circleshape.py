import pygame
import sys

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def collision_check(self, CircleShape):
        distance = self.position.distance_to(CircleShape.position)
        if distance <= (self.radius + CircleShape.radius):
            print ("Game Over!")
            sys.exit()
        else: return False

    def collision_check_shot(self, CircleShape):
        distance = self.position.distance_to(CircleShape.position)
        if distance <= (self.radius + CircleShape.radius):
            return True
        else: return False