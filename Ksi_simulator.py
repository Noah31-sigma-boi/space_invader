import pygame

import Tiles_map
from Tiles_map import *
from Player import *
class Game:

    def __init__(self):
        self.display = pygame.display.set_mode((800,500))
        self.run = True
        self.bg = pygame.image.load("ksi.jpg")
        self.tiles = Tiles_map_class(self)
        self.player = Player(self, Tiles_map.map_level)
        self.img = pygame.image.load("ksi_head.png")

    def Run_game(self):
        while self.run:
            self.img = pygame.transform.scale(self.img, (36, 59))
            pygame.display.set_caption("KSI SIMULATOR")
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    self.run = False
            self.display.fill((0,0,0))
            self.player.move()
            self.bg = pygame.transform.scale(self.bg, (800,500))

            self.player.draw()
            self.display.blit(self.bg, (0, 0))
            self.tiles.draw()
            self.display.blit(self.img, (self.player.x, self.player.y))

            pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.Run_game()
    pygame.init()