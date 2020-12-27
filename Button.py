import pygame.font

		
class Play_Button():
	def __init__(self,screen,settings):
		self.screen = screen
		self.rect = pygame.Rect(0,0,settings.button_width,settings.button_height)
		self.rect.centery = 350
		self.rect.centerx = self.screen.get_rect().centerx - 250
		self.msg = "Play"
		self.msg_text = settings.button_font.render(self.msg, True, settings.button_text_color,settings.button_color)
		self.msg_text_rect = self.msg_text.get_rect()
		self.msg_text_rect.centery = self.rect.centery
		self.msg_text_rect.centerx = self.rect.centerx
		self.pop_flag = True

	def draw(self,settings):
	# self.screen.fill(self.button_color2,self.rect2)
		self.screen.fill(settings.button_color,self.rect)
		self.screen.blit(self.msg_text,self.msg_text_rect)

class Exit_Button():
	def __init__(self,screen,settings):
		self.screen = screen
		self.rect = pygame.Rect(0,0,settings.button_width,settings.button_height)
		self.rect.centery = 350
		self.rect.centerx = screen.get_rect().centerx
		self.msg = "Exit"
		self.msg_text = settings.button_font.render(self.msg, True, settings.button_text_color,settings.button_color)
		self.msg_text_rect = self.msg_text.get_rect()
		self.msg_text_rect.centery = self.rect.centery
		self.msg_text_rect.centerx = self.rect.centerx
		self.pop_flag = True

	def draw(self,settings):
		self.screen.fill(settings.button_color,self.rect)
		self.screen.blit(self.msg_text,self.msg_text_rect)



class About_Button():
	def __init__(self,screen,settings):
		self.screen = screen
		self.rect = pygame.Rect(0,0,settings.button_width,settings.button_height)
		self.rect.centery = 350
		self.rect.centerx = screen.get_rect().centerx + 250
		self.msg = "About"
		self.msg_text = settings.button_font.render(self.msg, True, settings.button_text_color,settings.button_color)
		self.msg_text_rect = self.msg_text.get_rect()
		self.msg_text_rect.centery = self.rect.centery
		self.msg_text_rect.centerx = self.rect.centerx
		self.pop_flag = True


	def draw(self,settings):
		self.screen.fill(settings.button_color,self.rect)
		self.screen.blit(self.msg_text,self.msg_text_rect)


class Return_Button():
	def __init__(self,screen,settings):
		self.screen = screen
		self.return_rect = pygame.Rect(0,0,settings.return_width,settings.return_height)
		self.return_rect.centerx, self.return_rect.centery = 600,350
		self.rect_outer = pygame.Rect(0,0,settings.return_width_outer,settings.return_height_outer)
		self.rect_outer.centerx, self.rect_outer.centery = self.return_rect.centerx, self.return_rect.centery
		self.msg = "This is my first game. Hope you enjoy it!"
		self.msg_text = settings.return_button_font.render(self.msg, True, settings.button_text_color_new,settings.button_color)
		self.msg_text_rect = self.msg_text.get_rect()
		self.msg_text_rect.centerx, self.msg_text_rect.centery = self.return_rect.centerx, self.return_rect.centery
		self.pop_flag = True

	def draw(self,settings):
		self.screen.fill(settings.return_outer_color,self.rect_outer)
		self.screen.fill(settings.button_color,self.return_rect)
		self.screen.blit(self.msg_text,self.msg_text_rect)

class Void_High_Score():
	def __init__(self,screen,sb,settings):
		self.screen = screen
		# self.rect = pygame.Rect(0,0,settings.button_width,settings.button_height)
		# self.rect.centery = sb.score_image_rect.centery
		# self.rect.centerx = screen.get_rect().centerx + 400
		self.msg = "CLEAR"
		self.msg_text = settings.font_small.render(self.msg, True, sb.text_color,settings.button_color)
		self.msg_text_rect = self.msg_text.get_rect()
		self.msg_text_rect.centery = sb.score_image_rect.centery
		self.msg_text_rect.centerx = screen.get_rect().centerx + 400


	def draw(self):
		self.screen.blit(self.msg_text,self.msg_text_rect)


class Home_Button():
	def __init__(self,screen,sb):
		self.screen = screen
		self.image = pygame.image.load('images/home.png')
		self.rect = self.image.get_rect()
		self.rect.centery = sb.score_image_rect.centery
		self.rect.right = screen.get_rect().right - 10


	def draw(self):
		self.screen.blit(self.image,self.rect)

class Msg_Fade_Minus():
	def __init__(self,screen,settings):
		self.screen = screen
		self.rect = pygame.Rect(0,0,settings.button_width,settings.button_height)
		self.rect.center = screen.get_rect().center
		self.msg = "- 1"
		self.msg_text = settings.button_font.render(self.msg, True, settings.button_text_color,settings.button_color)
		self.msg_text_rect = self.msg_text.get_rect()
		self.msg_text_rect.center = self.rect.center
		

	def draw(self,settings):
		self.screen.fill(settings.button_color,self.rect)
		self.screen.blit(self.msg_text,self.msg_text_rect)

class Msg_Fade_Plus():
	def __init__(self,screen,settings):
		self.screen = screen
		self.rect = pygame.Rect(0,0,settings.button_width,settings.button_height)
		self.rect.center = screen.get_rect().center
		self.msg = "Level + 1"
		self.msg_text = settings.button_font.render(self.msg, True, settings.button_text_color,settings.button_color)
		self.msg_text_rect = self.msg_text.get_rect()
		self.msg_text_rect.center = self.rect.center
		

	def draw(self,settings):
		self.screen.fill(settings.button_color,self.rect)
		self.screen.blit(self.msg_text,self.msg_text_rect)

class Fish_Fade():
    def __init__(self,screen,msg_fade):
        self.screen = screen
        self.image = pygame.image.load('images/fish.png')
        self.rect = self.image.get_rect()
        self.rect.centery = msg_fade.rect.centery
        self.rect.centerx = msg_fade.rect.centerx - 60
       

    def draw(self):
        self.screen.blit(self.image,self.rect)

class Game_Over():
	def __init__(self,screen,settings):
		self.screen = screen
		self.rect = pygame.Rect(0,0,settings.button_width,settings.button_height)
		self.rect.center = screen.get_rect().center
		self.msg = "Oops! No Fish Left!"
		self.msg_text = settings.button_font.render(self.msg, True, settings.button_text_color,settings.button_color)
		self.msg_text_rect = self.msg_text.get_rect()
		self.msg_text_rect.center = self.rect.center
		
	def draw(self,settings):
		self.screen.fill(settings.button_color,self.rect)
		self.screen.blit(self.msg_text,self.msg_text_rect)





