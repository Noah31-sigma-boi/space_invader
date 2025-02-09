from Ksi_simulator import *
import pygame


_ = None
map_level = [
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, 1, 1, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, 1, 1, _, _, _, _, _, _],
    [_, _, 1, 1, 1, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, 1, _, _, _, 1, 1, _, _, _, _, _, _, _, _],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Tiles_map_class:

    def __init__(self, game):
        self.game = game
        self.map = map_level
        self.world_map = {}
        self.get_map()
        self.ksi_head = pygame.image.load("ksi_head.png")
        self.screen = pygame.display.set_mode((800,500))

    def get_map(self):
        for i, row in enumerate(self.map):
            for j, value in enumerate(row):
                if value:
                    self.world_map[(j,i)] = value

    def draw(self):
        print(self.world_map)
        for pos in self.world_map:
            self.ksi_head = pygame.transform.scale(self.ksi_head, (50,50))
            wall = pygame.Rect(pos[0]*50, pos[1]*50, 50, 50)
            pygame.draw.rect(self.game.display, ((0,100,200)), wall)
            self.screen.blit(self.ksi_head, (pos[0]*50,pos[1]*50))

