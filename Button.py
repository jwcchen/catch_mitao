import pygame.font
from Settings import settings
import Scoreboard

class Text_Button():
    def __init__(self, screen, msg, x, y, font_size, font_size_hovering):
        self.screen = screen
        self.msg = msg
        font = pygame.font.SysFont("Arial Rounded", font_size)
        self.msg_image = font.render(self.msg, True, settings.button_text_color, settings.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.centery = y
        self.msg_image_rect.centerx = x
        font_hovering = pygame.font.SysFont("Arial Rounded", font_size_hovering)
        self.msg_image_hovering = font_hovering.render(self.msg, True, settings.button_text_color_new, settings.button_color)
        self.msg_image_hovering_rect = self.msg_image_hovering.get_rect()
        self.msg_image_hovering_rect.centery = y
        self.msg_image_hovering_rect.centerx = x
        self.hovering = False

    def check_hovering(self, mouse_x, mouse_y):
        return self.msg_image_rect.collidepoint(mouse_x, mouse_y)

    def draw(self):
        if self.hovering:
            self.screen.blit(self.msg_image_hovering, self.msg_image_hovering_rect)
        else:
            self.screen.blit(self.msg_image, self.msg_image_rect)

class MainScreen_Button():
    def __init__(self, screen, msg, x, y):
        self.screen = screen
        self.text_button = Text_Button(screen, msg, x, y, 48, 50)
        self.icon = pygame.image.load('images/icon.png')
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.centery = y
        self.icon_rect.right = self.text_button.msg_image_rect.left

    def draw(self):
        self.text_button.draw()
        self.screen.blit(self.icon, self.icon_rect)

class Return_Button():
    def __init__(self, screen, msg, x, y):
        self.screen = screen
        self.return_rect = pygame.Rect(0,0,settings.return_width,settings.return_height)
        self.return_rect.centerx, self.return_rect.centery = x, y
        self.rect_outer = pygame.Rect(0,0,settings.return_width_outer,settings.return_height_outer)
        self.rect_outer.centerx, self.rect_outer.centery = self.return_rect.centerx, self.return_rect.centery
        self.text_button = Text_Button(screen, msg, x, y, 30, 30)

    def draw(self,settings):
        self.screen.fill(settings.return_outer_color,self.rect_outer)
        self.screen.fill(settings.button_color,self.return_rect)
        self.text_button.draw()

class Note_Msg():
    def __init__(self, screen, msg):
        self.screen = screen
        self.msg = msg
        self.msg_text = settings.button_font.render(self.msg, True, settings.button_text_color,settings.button_color)
        self.msg_text_rect = self.msg_text.get_rect()
        self.msg_text_rect.center = self.screen.get_rect().center
        self.timer = 0

    def update(self, elapsed_time):
        self.timer = max(self.timer - elapsed_time, 0)

    def draw(self):
        if self.timer > 0:
            self.screen.blit(self.msg_text,self.msg_text_rect)

class Note_Fish():
    def __init__(self, screen):
        self.screen = screen
        self.msg = Note_Msg(screen, "-1")
        self.image = pygame.image.load('images/fish.png')
        self.rect = self.image.get_rect()
        self.rect.centery = self.msg.msg_text_rect.centery
        self.rect.centerx = self.msg.msg_text_rect.centerx - 60
        self.timer = 0

    def update(self, elapsed_time):
        self.timer = max(self.timer - elapsed_time, 0)
        self.msg.timer = self.timer

    def draw(self):
        if self.timer > 0:
            self.msg.draw()
            self.screen.blit(self.image, self.rect)

