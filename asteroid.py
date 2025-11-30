import pygame
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import CircleShape
from logger import log_event
import random  


class Asteroid(CircleShape):
    def __init__(self,x, y, radius):
       super().__init__(x, y, radius)
       
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", tuple(self.position), self.radius, width=LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        from asteroidfield import AsteroidField  # import here to avoid circular dependency
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        elif self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            randomizer = random.uniform(20,50)
            velocity1 = self.velocity.rotate(randomizer)
            velocity2 = self.velocity.rotate(-randomizer)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = velocity1
            new_asteroid2.velocity = velocity2
          