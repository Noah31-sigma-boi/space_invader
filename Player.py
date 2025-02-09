from Ksi_simulator import *
import pygame

class Player:

    def __init__(self, game, map):
        self.game = game
        self.fps = pygame.time.Clock()
        self.map = map
        self.world_map = {}
        self.x = 0
        self.y = 0
        self.direction_X = 0
        self.direction_Y = 0



    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.direction_Y = -1

        elif key[pygame.K_s]:
            self.direction_Y = +1

        elif key[pygame.K_a]:
            self.direction_X = -1

        elif key[pygame.K_d]:
            self.direction_X = +1
        else:
            self.direction_X = 0
            self.direction_Y = 0

        self.x += self.direction_X
        self.y += self.direction_Y
    def check_collision(self, player):
        for i, row in enumerate(self.map):
            for j, value in enumerate(row):
                if value:
                    self.world_map[(j,i)] = value

        for pos in self.world_map:

            wall = pygame.Rect(pos[0]*50, pos[1]*50, 50, 50)
            pygame.draw.rect(self.game.display, ((0,0,0)), wall)
            if player.colliderect(wall):
                if self.direction_Y == -1:
                    self.y += 1

                if self.direction_Y == 1:
                    self.y -= 1

                if self.direction_X == 1:
                    self.x -= 1

                if self.direction_X == -1:
                    self.x += 1

    def draw(self):

        player = pygame.Rect(self.x, self.y, 36, 59)
        self.check_collision(player)

        pygame.draw.rect(self.game.display, ((255, 0, 0)), player)

        self.fps.tick(300)

