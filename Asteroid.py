from circleshape import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, self.radius, width=2)#this needs change

    def update(self, dt):
        position += self.velocity * dt

        