from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()
        # If the radius of the asteroid is less than or equal to ASTEROID_MIN_RADIUS, just return, this was a small asteroid and we're done
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(random_angle)
            v2 = self.velocity.rotate(-random_angle)
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            s1 = Asteroid(self.position.x, self.position.y, new_radius)
            s1.velocity = v1 * 1.2
            s2 = Asteroid(self.position.x, self.position.y, new_radius)
            s2.velocity = v2 * 1.2

            
            
            