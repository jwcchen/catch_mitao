import pygame

import os

import glob

import random

filelist= [file for file in os.listdir('images/cat') if file.endswith('.png')]


#from pygame.sprite import Sprite

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
    def __init__(self,screen, x, y):
        self.screen = screen
        
        self.image = pygame.image.load(random.choice(glob.glob('images/cat/*.png')))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.y = float(self.rect.centery)

    def draw(self):
        self.screen.blit(self.image,self.rect)

class BoxedCat():
    def __init__(self,screen, x, y):

        self.box1 = Box1(screen, x, y)
        self.box2 = Box2(screen, x, y)
        self.cat = Cat(screen, x, y)
        self.box1.rect.center = self.cat.rect.center
        self.box2.rect.center = self.box1.rect.center
        self.is_animating = False
        self.animation_time = None
        self.direction = 1
        self.t2 = 0
        self.sequence = 0

    def animate(self, animation_time):
        self.is_animating = True
        self.animation_time = animation_time

    def update(self, state, cat_position):
        if self.is_animating:
            if self.cat.rect.centery > self.box1.rect.centery:
                state.cats.remove(self)
                cat_position.pop(self.sequence)
                # print(state.cats)
                # print(self.cat.rect.centery,self.box1.rect.centery)
                # print(self.sequence)
                
            else:
                if self.cat.rect.centery < self.box1.rect.centery - 40:
                    self.direction = self.direction * (-1)
                
                self.cat.y = self.cat.y - (40/self.animation_time) * 0.004 * self.direction
                self.cat.rect.centery = self.cat.y

    def draw(self):
        self.box1.draw()
        self.cat.draw()
        self.box2.draw()


class Fish():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/fish.png')
        self.rect = self.image.get_rect()

    def draw(self):
        self.screen.blit(self.image,self.rect)

class Cat_Symbol():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('images/cat_symbol.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
       

    def draw(self):
        self.screen.blit(self.image,self.rect)

class Multiply():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('images/multiply.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 450
       

    def draw(self):
        self.screen.blit(self.image,self.rect)



