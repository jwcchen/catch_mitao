import pygame
import glob
import random

class Box1():
    def __init__(self,screen, x, y):
        self.screen = screen
        self.image = pygame.image.load('images/box1.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def draw(self):
        self.screen.blit(self.image,self.rect)

class Box2():
    def __init__(self,screen, x, y):
        self.screen = screen
        self.image = pygame.image.load('images/box2.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def draw(self):
        self.screen.blit(self.image,self.rect)

class Cat():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load(random.choice(glob.glob('images/cat/*.png')))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.y = float(self.rect.centery)

    def draw(self):
        self.screen.blit(self.image,self.rect)

class BoxedCat():
    def __init__(self, screen, x, y):
        self.box1 = Box1(screen, x, y)
        self.box2 = Box2(screen, x, y)
        self.cat = Cat(screen, x, y)
        self.box1.rect.center = self.cat.rect.center
        self.box2.rect.center = self.box1.rect.center
        self.direction = 1
        self.cat_position = (x, y)

    def update(self, state):
        if self.cat.rect.centery > self.box1.rect.centery:
            state.cats.remove(self)
        else:
            if self.cat.rect.centery < self.box1.rect.centery - 40:
                self.direction = self.direction * (-1)
            animation_time = 1
            self.cat.y = self.cat.y - (40 / animation_time) * 0.004 * self.direction
            self.cat.rect.centery = self.cat.y

    def draw(self):
        self.box1.draw()
        self.cat.draw()
        self.box2.draw()
