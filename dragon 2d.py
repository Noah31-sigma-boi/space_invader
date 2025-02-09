import random
import time

import pygame




class Game:

    def __init__(self):
        self.display = pygame.display.set_mode((700,500))
        self.running = True
        self.x = 1
        self.y = 0
        self.x_cooldown = 1000
        self.x_v = False
    def move(self,player, ground):
        held_keys = pygame.key.get_pressed()

        if held_keys[pygame.K_d]:
            self.x += 1

        if held_keys[pygame.K_a]:
            self.x -= 1

        if held_keys[pygame.K_f]:

            mx, my = pygame.mouse.get_pos()
            if self.x != mx:
                if self.x > mx:
                    self.x -= mx/self.x
                else:
                    self.x += mx/self.x

            if self.y != my:
                if self.y > my:
                    self.y -= 2
                    self.y -= my/self.y
                else:
                    self.y += my/self.y

        if held_keys[pygame.K_z]:
            mx, my = pygame.mouse.get_pos()
            pygame.draw.line(self.display, (250,170,0), (self.x+20, self.y+20),( mx, my),10)
            pygame.draw.circle(self.display, ((255,0,0)), (mx,my), 20)

        if held_keys[pygame.K_c]:
            self.y = 100
            mx, my = pygame.mouse.get_pos()
            mx = mx + random.randrange(-150,150)
            pygame.draw.line(self.display, (250,170,0), (self.x+20, self.y+20),( mx, my),10)
            pygame.draw.circle(self.display, ((255,0,0)), (mx,my), 20)

        else:
            if not player.colliderect(ground):
                self.y += 1
                self.x_cooldown = 100

    def run(self):
        while self.running:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    self.running = False
            player = pygame.Rect(self.x, self.y, 20, 50)
            ground = pygame.Rect(0,400,1000,1000)
            self.display.fill((10,10,10))
            pygame.draw.rect(self.display, ((200,200,200)), ground)
            pygame.draw.rect(self.display, ((255,0,0)), player)
            self.move(player, ground)
            pygame.display.flip()



if __name__ == '__main__':
    game= Game()
    game.run()
    pygame.init()

