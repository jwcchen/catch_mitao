import pygame.font

pygame.init()

class Settings():
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (252,220,226)
		self.generation_time = 0.7
		
		self.button_color = (252,220,226)
		self.button_text_color = (252,174,187)
		self.button_font = pygame.font.SysFont("Arial Rounded", 40)
		self.button_width, self.button_height = 200,150	

		self.button_text_color_new = (241,131,156)
		self.button_font_new = pygame.font.SysFont("Arial Rounded", 50, bold=True)

		self.return_button_font = pygame.font.SysFont("Arial Rounded", 30)
		self.return_width, self.return_height = 850, 100
		self.return_width_outer, self.return_height_outer = 870,120
		self.return_outer_color = (255,255,255)

		self.font_small = pygame.font.SysFont("None", 48)