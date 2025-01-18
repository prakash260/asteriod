import pygame
from constants import * 
from player import Player



def main():
   print("Starting asteroids!")
   print("Screen width:", SCREEN_WIDTH)
   print("Screen height:", SCREEN_HEIGHT)
   p = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   t = pygame.time.Clock()
   dt = 0

   while True:
      # p.draw(screen)
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return
    
      screen.fill((0, 0, 0))
      p.update(dt)
      p.draw(screen)
      pygame.display.flip()
      dt = t.tick(60) /1000.0
   




if __name__ == "__main__":
   main() 