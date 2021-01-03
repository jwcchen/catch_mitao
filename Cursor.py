import pygame

class Cursor_Paw():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('images/paw.png')
        
    def draw_paw(self, mouse_x, mouse_y):
        rect = self.image.get_rect()
        rect.centerx = mouse_x
        rect.centery = mouse_y
        self.screen.blit(self.image, rect)
