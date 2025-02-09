import pygame
from Pygame_map import *
from Pygame_player import *

class Game:


    def __init__(self):
        self.display = pygame.display.set_mode((700,500))
        self.running = True
        self.map = Map_tiles(self)
        self.player = Player(self, self.map.world_map)

    def Run(self):


        while self.running:

            pygame.display.set_caption("PyGame")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.display.fill((0,0,0))
            self.map.draw()
            self.player.Run()
            pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.Run()
    pygame.init()