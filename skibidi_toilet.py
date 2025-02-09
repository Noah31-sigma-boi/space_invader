import random

import pygame
import pygame.font

pygame.font.init()
class Game:

    def __init__(self):
        self.display = pygame.display.set_mode((600,400))
        self.running = True

    def text(self, text, x, y, font):
        img = font.render(text,False,(0,0,0))
        self.display.blit(img, (x,y))

    def button(self, x,y, zx,zy):

        button = pygame.Rect(x,y,zx,zy)
        pygame.draw.rect(self.display, ((200,200,200)), button)

        mx,my = pygame.mouse.get_pos()
        mouse = pygame.Rect(mx,my, 1,1)
        pygame.draw.rect(self.display, ((255,255,255)), mouse)

        if mouse.colliderect(button):
            if pygame.mouse.get_pressed()[0]:
                print("skibidi toilet")
    def Run(self):
        while self.running:
            pygame.display.set_caption("Skibidi_toilet")
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    self.running = False
            self.display.fill((255,255,255))
            font = pygame.font.SysFont("Arial",30)
            self.text("SKIBIDI DOB DOB DOB YES YES !!!!", 10,10,font)
            self.button(15,70,150,70)


            pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.Run()
    pygame.init()