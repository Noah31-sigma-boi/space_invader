import random

import pygame
import pygame.font

pygame.font.init()
L = 600
H = 400
class Game:

    def __init__(self):
        self.display = pygame.display.set_mode((L,H))
        self.running = True
        self.meme = pygame.image.load("meme_btn_g.jpg")
        self.detect = False
        self.cooldown = 500
        self.choose = random.randrange(0,5)
        self.meme_g = pygame.image.load("meme_btn.jpg")

    def text(self, text, x, y, font):
        img = font.render(text,False,(0,0,0))
        self.display.blit(img, (x,y))

    def button(self, x,y, zx,zy,text,size):
        font = pygame.font.SysFont("Arial", size)

        button = pygame.Rect(x,y,zx,zy)
        pygame.draw.rect(self.display, ((200,200,200)), button)

        mx,my = pygame.mouse.get_pos()
        mouse = pygame.Rect(mx,my, 1,1)
        pygame.draw.rect(self.display, ((255,255,255)), mouse)
        self.text(text, x,y, font)

        if mouse.colliderect(button):
            if pygame.mouse.get_pressed()[0]:
                self.detect = True

    def Run(self):
        while self.running:
            pygame.display.set_caption("Detector")
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    self.running = False
            self.meme = pygame.transform.scale(self.meme, (600, 400))
            self.meme_g = pygame.transform.scale(self.meme_g, (600,400))
            self.display.fill((255,255,255))
            font = pygame.font.SysFont("Arial", 30)

            self.text("Gay detector", 10, 10, font)

            self.button(L/2-150/2,H/2-70/2,150,70, "Reveal",25)
            if self.detect:
                self.cooldown -= 1
                if self.choose != 1:
                    self.display.blit(self.meme, (0,0))
                elif self.choose == 1:
                    self.display.blit(self.meme_g, (0, 0))
            if self.cooldown <= 0:
                self.choose = random.randrange(0,5)
                self.cooldown = 500
                self.detect = False

            pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.Run()
    pygame.init()