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
        self.speed = 5
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)



    def update(self):
        self.key_input()




    def key_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:

            if self.rect.bottom > 0:
                self.rect.y += self.speed

        if keys[pygame.K_UP]:
            if self.rect.top < GAME_HEIGHT:
                self.rect.y += -self.speed
