import pygame.font

from Settings import settings

y_alignment = 30

class Void_High_Score():
    def __init__(self,screen):
        self.screen = screen
        self.msg = "CLEAR"
        self.image = settings.font_small.render(self.msg, True, settings.score_text_color, settings.button_color)
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_rect().centerx + 400
        self.rect.centery = y_alignment

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Home_Button():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('images/home.png')
        self.rect = self.image.get_rect()
        self.rect.right = screen.get_rect().right - 10
        self.rect.centery = y_alignment

    def draw(self):
        self.screen.blit(self.image,self.rect)

class Scoreboard():
    def __init__(self,screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 48)
        self.fish_image = pygame.image.load('images/fish.png')
        self.cat_image = pygame.image.load('images/cat_symbol.png')
        self.multiply_image = pygame.image.load('images/multiply.png')
        self.void_button = Void_High_Score(screen)
        self.home_button = Home_Button(screen)

    def draw(self, score, high_score, n_cat, fish_left):
        level = "L" + str(score // 750 + 1)
        level_image = self.font.render(level, True, settings.score_text_color, settings.bg_color)
        level_rect = level_image.get_rect()
        level_rect.left = 10
        level_rect.centery = y_alignment
        self.screen.blit(level_image, level_rect)

        for i in range(fish_left):
            fish_rect = self.fish_image.get_rect()
            fish_rect.x = 50 + i * fish_rect.width
            fish_rect.centery = y_alignment
            self.screen.blit(self.fish_image, fish_rect)

        score_image = self.font.render(str(score), True, settings.score_text_color, settings.bg_color)
        score_rect = score_image.get_rect()
        score_rect.right = self.screen.get_rect().right - 350
        score_rect.centery = y_alignment
        self.screen.blit(score_image, score_rect)

        high_score_image = self.font.render(str(high_score), True, settings.score_text_color, settings.bg_color)
        high_score_rect = high_score_image.get_rect()
        high_score_rect.centerx = self.screen.get_rect().centerx + 50
        high_score_rect.centery = y_alignment
        self.screen.blit(high_score_image, high_score_rect)

        cat_rect = self.cat_image.get_rect()
        cat_rect.centerx = 400
        cat_rect.centery = y_alignment
        self.screen.blit(self.cat_image, cat_rect)

        multiply_rect = self.multiply_image.get_rect()
        multiply_rect.centerx = 450
        multiply_rect.centery = y_alignment
        self.screen.blit(self.multiply_image, multiply_rect)

        n_cat_image = self.font.render(str(n_cat), True, settings.score_text_color, settings.bg_color)
        n_cat_rect = n_cat_image.get_rect()
        n_cat_rect.centerx = self.screen.get_rect().centerx - 110
        n_cat_rect.centery = y_alignment
        self.screen.blit(n_cat_image, n_cat_rect)

        self.void_button.draw()
        self.home_button.draw()
