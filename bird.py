import pygame, random
from constants import *
import random
pygame.init()
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 64
        self.height = 64
        self.x = GAME_WIDTH // 2 - self.width * 2
        self.y = 350
        self.lift = -20
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.grav = 0.6
        self.vel = 0
        self.max_vel = -10
        self.started = False



    def update(self):
        if self.started:

            self.vel += self.grav
            self.rect.y += self.vel

        if self.vel < self.max_vel:
            self.vel = self.max_vel

        # if self.rect.top < GAME_HEIGHT:
        #     self.rect = self.rect.move(0, self.grav)



    def flap(self):
        if self.started == False:
            self.started = True

        if self.started:
            self.vel += self.lift
