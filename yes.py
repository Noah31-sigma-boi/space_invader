import random
import time

import pygame
import pygame.font

pygame.font.init()
L = 600
H = 400
class Game:

    def __init__(self):
        self.display = pygame.display.set_mode((L,H))
        self.running = True
        self.meme = pygame.image.load("meme_btn.jpg")
        self.detect = False
        self.cooldown = 500
        self.detect_2 = False

    def text(self, text, x, y, font):
        img = font.render(text,False,(0,0,0))
        self.display.blit(img, (x,y))

    def button(self, x,y, zx,zy,text,font):


        button = pygame.Rect(x,y,zx,zy)
        pygame.draw.rect(self.display, ((200,200,200)), button)

        mx,my = pygame.mouse.get_pos()
        mouse = pygame.Rect(mx,my, 1,1)
        pygame.draw.rect(self.display, ((255,255,255)), mouse)
        self.text(text, x,y, font)

        if mouse.colliderect(button):
            if pygame.mouse.get_pressed()[0]:
                if text != "*leave blank*":
                    self.text(text, 10,10,font)
                    self.detect = True

    def Run(self):
        while self.running:
            pygame.display.set_caption("Detector")
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    #self.running = False
                    print("Gays are not able to leave this quiz")
            self.meme = pygame.transform.scale(self.meme, (600, 400))
            self.display.fill((255,255,255))
            font = pygame.font.SysFont("Arial", 24)
            self.button(L / 2-75, H / 2 - 70 / 2, 150,70, "no",font)
            self.button(L / 2 - 350 / 2-75, H / 2 - 70 / 2, 150, 70, "yes", font)
            self.button(L / 2 + 350 / 2-75, H / 2 - 70 / 2, 150, 70, "*leave blank*", font)
            self.text("___, I am gay", 10,10,font)
            pygame.display.flip()
            if self.detect:

                time.sleep(2)


if __name__ == '__main__':
    print("If u cheat ur gay >:)")
    game = Game()
    game.Run()
    pygame.init()