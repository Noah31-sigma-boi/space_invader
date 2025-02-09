import time
import pygame
import random

pygame.font.init()

L = 400
H = 400

_ = None

One = [
    [_, _, _],
    [_, 1, _],
    [_, _, _]
]

Two = [
    [_, _, _],
    [1, _, 1],
    [_, _, _]
]

Three = [
    [_, 1, _],
    [_, _, _],
    [1, _, 1]
]

Four = [
    [1, _, 1],
    [_, _, _],
    [1, _, 1]
]

Five = [
    [1, _, 1],
    [_, 1, _],
    [1, _, 1]
]

Six = [
    [1, _, 1],
    [1, _, 1],
    [1, _, 1]
]

class Map:

    def __init__(self,game,map):
        self.game = game
        self.map = map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for i,row in enumerate(self.map):
            for j,value in enumerate(row):
                if value:
                    self.world_map[(j+1,i+1)] = value

    def draw(self):
        for pos in self.world_map:
            pygame.draw.circle(self.game.display, ((0,0,0)), (pos[0]*100, pos[1]*100),40)

class Game:

    def __init__(self):
        self.display = pygame.display.set_mode((L,H))
        self.running = True
        self.list_num = [One, Two, Three, Four, Five, Six]
        self.number = random.choice(self.list_num)

    def button(self):
        font = pygame.font.SysFont("Arial",25)
        img = font.render("Roll",False,(0,0,0))

        btn = pygame.Rect(L-50,H-50,40,30)
        Mx,My = pygame.mouse.get_pos()
        mouse = pygame.Rect(Mx,My,1,1)

        pygame.draw.rect(self.display,((200,200,200)),btn)
        pygame.draw.rect(self.display,((200,200,200)),mouse)
        self.display.blit(img,(L-50,H-50))

        if mouse.colliderect(btn):
            if pygame.mouse.get_pressed()[0]:
                self.number = random.choice(self.list_num)
                time.sleep(0.2)

    def Run(self):
        while self.running:
            pygame.display.set_caption("Dice")
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    self.running = False

            self.display.fill((255,255,255))
            self.map = Map(self, self.number)
            self.button()
            self.map.draw()

            pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.Run()
    pygame.init()
