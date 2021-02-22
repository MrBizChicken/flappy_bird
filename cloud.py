import pygame
from constants import * 
import random
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randint(0, GAME_WIDTH)
        self.y = random.randint(0, 50)
        self.width = 50
        self.height = 20
        self.speed = 1
        self.image = pygame.image.load("cloud.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)





    def update(self):
        self.move()






    def move(self):

        if self.rect.left >= GAME_WIDTH:
            self.rect.right = 0

        else:
            self.rect.left += self.speed
