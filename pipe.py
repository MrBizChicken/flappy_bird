import pygame, random
from constants import *
import random
pygame.init()
class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 64
        self.height = random.randint(0, 200)
        self.x = 50
        self.y = 0
        self.speed = 3
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)






    def update(self):
        pass
