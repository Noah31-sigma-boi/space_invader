import random
import time

import pygame

lenght = 700
height = 500

pygame.font.init()

class Game:

    def __init__(self):
        self.display = pygame.display.set_mode((lenght, height))
        self.running = True
        self.bg = pygame.image.load("image.jpg")
        self.player = pygame.image.load("rocket.png")
        self.target = pygame.image.load("spaceship.png")
        self.boom = pygame.image.load("boom.png")
        self.heart = pygame.image.load("heart.png")
        self.heart2 = pygame.image.load("heart.png")
        self.heart3 = pygame.image.load("heart.png")
        self.one = True
        self.two = True
        self.three = True
        self.x = lenght / 2
        self.fps = pygame.time.Clock()
        self.gun_y = 400
        self.gun_detect = False
        self.gun_x = -10
        self.target_x = random.randrange(1, height, 5)
        self.target_y = 0
        self.score = 0
        self.boom_cooldown = 500


    def Move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            if self.x-25 > 0:
                self.x -= 1
        if key[pygame.K_d]:
            if self.x + 55 < 700:
                self.x += 1

        if key[pygame.K_SPACE]:
            if self.gun_detect:
                pass
            else:
                self.gun_detect = True
                self.gun_x = self.x + 5

    def lives_detect(self):
        if self.three:
            self.three = False
        elif self.two:
            self.two = False
        elif self.one:
            print(self.score)
            self.running = False

    def Run(self):
        animation = False
        while self.running:
            pygame.display.set_caption("Space shooter")
            self.fps.tick(500)
            self.Move()
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    print(self.score)
                    self.running = False

            self.bg = pygame.transform.scale(self.bg, (lenght, height))
            self.display.blit(self.bg, (0, 0))
            self.heart = pygame.transform.scale(self.heart, (50, 50))
            if self.one:
                self.display.blit(self.heart, (500, 30))
            self.heart2 = pygame.transform.scale(self.heart2, (50, 50))
            if self.two:
                self.display.blit(self.heart2, (570, 30))
            self.heart3 = pygame.transform.scale(self.heart3, (50, 50))
            if self.three:
                self.display.blit(self.heart3, (640, 30))

            self.player = pygame.transform.scale(self.player, (70,100))
            self.display.blit(self.player, (self.x-25, 400))
            gun = pygame.Rect(self.gun_x, self.gun_y, 10,30)
            if self.gun_detect:

                self.gun_y -= 1
                pygame.draw.rect(self.display, ((255,255,0)), gun)

            self.target_y += 0.5

            self.target = pygame.transform.scale(self.target, (100,80))
            target = self.display.blit(self.target, (self.target_x, self.target_y))
            if self.target_y == 700 or target.colliderect(gun):
                self.target_y = 0

            font = pygame.font.SysFont("Arial", 24)
            img = font.render("Score : " + str(self.score), False, (255,255,255))
            self.display.blit(img, (30,10))



            if target.colliderect(gun):
                self.score += 10
                self.target_x = random.randrange(1, height, 5)

            if self.target_y == 670:
                self.score -= 30
                self.lives_detect()
                self.target_x = random.randrange(1, height, 5)

            if self.gun_y == 0:
                self.gun_detect = False
                self.gun_y = 400

            player = self.display.blit(self.player, (self.x-25, 400))
            if player.colliderect(target):
                self.score -= 30
                self.target_x = random.randrange(1, height, 5)
                self.target_y = 0
                animation = True
                self.lives_detect()

            if animation:
                self.boom = pygame.transform.scale(self.boom, (70,70))
                self.display.blit(self.boom, (self.x -25, 385))
                self.boom_cooldown -= 1
                if self.boom_cooldown == 0:
                    self.boom_cooldown = 500
                    animation = False
            pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.Run()
    pygame.init()
