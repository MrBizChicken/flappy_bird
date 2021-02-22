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
        self.image = pygame.image.load("bird.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.grav = 0.6
        self.vel = 0
        self.max_vel = -10
        self.started = False




    def update(self, pipes_group):
        self.collide(pipes_group)
        self.gravity()

    def gravity(self):
        if self.started:

            self.vel += self.grav
            self.rect.y += self.vel

        if self.vel < self.max_vel:
            self.vel = self.max_vel

    def collide(self, pipes_group):
        if pygame.sprite.spritecollide(self, pipes_group, False):
            self.rect.x = GAME_WIDTH // 2 - self.width * 2
            self.rect.y = 350
            self.started = False
            for p in pipes_group:

                p.reset()

    def flap(self):
        if self.started == False:
            self.started = True

        if self.started:
            self.vel += self.lift
