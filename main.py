import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot



def main():
   
   print("Starting asteroids!")
   print("Screen width:", SCREEN_WIDTH)
   print("Screen height:", SCREEN_HEIGHT)
   
   updatable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   asteroids = pygame.sprite.Group()
   shots = pygame.sprite.Group()

   Asteroid.containers = (asteroids, updatable, drawable)
   Shot.containers = (shots, updatable, drawable)
   Player.containers = (updatable, drawable)
   AsteroidField.containers = (updatable,)


   p = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
   a = AsteroidField()
   
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   
   t = pygame.time.Clock()
   
   dt = 0

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return
         
      for updatable_sprite in updatable:
         updatable_sprite.update(dt)

      screen.fill((0,0,0))

      for asteroid in asteroids:
         for shot in shots:
            if asteroid.collisions(shot):
               shot.kill()
               asteroid.split()
               
         if asteroid.collisions(p):
            print("Game Over!")
            return   
          

      for draw_sprite in drawable:
               draw_sprite.draw(screen)
      
 
      pygame.display.flip()
      dt = t.tick(60) /1000.0
   


if __name__ == "__main__":
   main() 