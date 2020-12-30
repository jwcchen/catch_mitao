import pygame

class Cursor_Paw():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('images/paw.png')
        self.rect = self.image.get_rect()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.rect.centerx = mouse_x
        self.rect.centery = mouse_y

    def draw_paw(self):
        self.screen.blit(self.image,self.rect)
