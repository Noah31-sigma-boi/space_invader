import pygame


class Player:
    def __init__(self,game, world_map):
        self.game = game
        self.world_map = world_map
        self.x = 100
        self.y = 100
        self.jump = True
        self.high_jump = 20
        self.gravity = 1
        self.high_r = self.high_jump
        self.droite = False
        self.gauche = True
        self.soldier = pygame.image.load("soldier.png")
        self.gun_duration = 1000
        self.gun_shoot = False
        self.gun_x = 0
        self.gun_y = 0
        self.gun_direction = 0
        self.start = 0
        self.fps = pygame.time.Clock()

    def jump_func(self, y):
        start = y
        if self.jump == False:
            self.y -= self.high_jump
            self.high_jump -= self.gravity
            if self.y >= start:
                self.high_jump = self.high_r
                self.jump = True




    def move(self, player, ground):
        held_keys = pygame.key.get_pressed()



        if held_keys[pygame.K_d]:

            if self.droite:
                self.soldier = self.soldier = pygame.transform.flip(self.soldier, 1, 0)
                self.droite = False
                self.gauche = True

            if not self.x >= 590:
                self.x += 0.35

        if held_keys[pygame.K_a]:
            pygame.transform.rotate(self.soldier, 180)
            if self.gauche:
                self.soldier = self.soldier = pygame.transform.flip(self.soldier, 1, 0)
                self.gauche = False
                self.droite = True
            if not self.x <= 10:
                self.x -= 0.35

        if held_keys[pygame.K_SPACE]:
            if self.jump == True:
                self.start = ground.y - 100
                self.jump = False

        if pygame.mouse.get_pressed()[0]:
            if self.gun_shoot:
                pass
            else:
                self.gun_x = self.x

                self.gun_shoot = True
                if self.gauche:
                    self.gun_x = self.x + 75
                    self.gun_y = self.y + 32
                    self.gun_direction = 0.5
                if self.droite:
                    self.gun_direction = -0.5

        if self.gun_shoot:

            if self.gun_duration == 0:
                self.gun_duration = 1000
                self.gun_shoot = False
            else:
                self.gun_duration -= 1
            self.gun_x += self.gun_direction
            gun = pygame.Rect(self.gun_x, self.gun_y, 10, 10)
            pygame.draw.rect(self.game.display, ((255, 255, 0)), gun)

        if self.jump == True:
            if not player.colliderect(ground):
                self.y += 1

    def Run(self):
        self.fps.tick(200)

        player = pygame.Rect(self.x, self.y, 100,100)
        pygame.draw.rect(self.game.display, ((255,255,255)), player)
        self.soldier = pygame.transform.scale(self.soldier, (100,100))
        self.game.display.blit(self.soldier, (self.x, self.y))

        for pos in self.world_map:
            ground = pygame.Rect(pos[0] * 50, pos[1] * 50, 50, 50)
            pygame.draw.rect(self.game.display, ((200, 200, 200)), ground)

        self.move(player, ground)
        print(player.y)