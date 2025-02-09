import random

import pygame


L = 700
H = 500

pygame.font.init()

class Game:

    def __init__(self):
        self.display = pygame.display.set_mode((L,H))
        self.running = True
        self.fps = pygame.time.Clock()
        self.shrek = pygame.image.load("shrek.png")
        self.ane = pygame.image.load("shrek_ane.png")
        self.shrek_size = 100
        self.x_a = random.randrange(1,550)
        self.y_a = random.randrange(1, 400)
        self.x = L/2
        self.y = H/2
        self.speed = 2.5
        self.points = 0

    def text(self, text, x, y, size, type):
        font = pygame.font.SysFont(type, size)
        img = font.render(text, False, (255,255,255))
        self.display.blit(img, (x,y))

    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_w] or key[pygame.K_UP]:
            self.y -= self.speed

        if key[pygame.K_s] or key[pygame.K_DOWN]:
            self.y += self.speed

        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.x -= self.speed

        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.x += self.speed


    def Run(self):
        while self.running:
            pygame.display.set_caption("Shrek")
            self.move()
            self.fps.tick(500)
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    self.running = False
            self.display.fill((90,255,25))
            self.shrek = pygame.transform.scale(self.shrek, (self.shrek_size, self.shrek_size))
            self.ane = pygame.transform.scale(self.ane, (150, 100))
            self.display.blit(self.ane, (self.x_a, self.y_a))
            self.display.blit(self.shrek, (self.x,self.y))
            shrek = self.display.blit(self.shrek, (self.x, self.y))
            ane = self.display.blit(self.ane, (self.x_a, self.y_a))
            timer = round(pygame.time.get_ticks()/1000 + 1)
            if shrek.colliderect(ane):
                self.points += 10
                if self.shrek_size < 170:
                    self.shrek_size += 10
                self.x_a = random.randrange(1, 550)
                self.y_a = random.randrange(1, 400)
            if self.shrek_size == 170:
                self.speed = 3.5
                self.text("(Max)", 117, 150, 25, "Arial")

            self.text("Points :  "+str(self.points), 10,10,25,"Arial")
            self.text("Temps en seconde :  " + str(timer), 10, 50, 25, "Arial")
            tp = round(self.points/timer)
            self.text("Points par seconde :  " + str(tp), 10, 100, 25, "Arial")
            self.text("Taille :  " + str(self.shrek_size), 10, 150, 25, "Arial")
            self.text("Vitesse :  " + str(self.speed), 10, 200, 25, "Arial")

            pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.Run()
    pygame.init()