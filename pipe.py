import pygame, random
from constants import *
import random


class Top_pipe(pygame.sprite.Sprite):
    def __init__(self, x, pipes_group):
        super().__init__()
        self.width = 64
        self.y = self.get_new_y()
        self.height = self.y
        self.x = x

        self.speed = 10
        self.image = pygame.image.load("pipe_top.png")

        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.x, self.y)

        self.pg = pipes_group

        # with out this we will spawn infinite pipes
        if type(self) == Top_pipe:
            pipes_group.add(Bottom_pipe(x, self.y, self.pg))


    def update(self):
        self.rect = self.rect.move(-self.speed, 0)

        # Pipe passes left side of screen
        if self.rect.right <= 0:
            self.reset()



    def reset(self):
        new_y = self.get_new_y()
        self.rect.left = GAME_WIDTH  + GAME_WIDTH // 3
        self.rect.bottom = new_y

        for p in self.pg:
            if  type(p) == Bottom_pipe and p.rect.x == self.rect.x:
                p.rect.top = new_y + p.gap

    def get_new_y(self):
        min_from_top = 50
        max_from_top = GAME_HEIGHT // 2

        return random.randint(min_from_top, max_from_top)


class Bottom_pipe(Top_pipe):
    def __init__(self, x, y, pipes_group):
        super().__init__(x, pipes_group)
        self.gap = 200
        self.height = GAME_HEIGHT - y + self.gap
        self.y = y + self.gap
        self.rect.topleft = (self.x, self.y)
        self.image = pygame.image.load("pipe_bottom.png")
