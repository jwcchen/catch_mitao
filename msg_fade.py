class Msg_Fade():
	def __init__(self):
		self.screen = screen
		self.rect = pygame.Rect(0,0,settings.button_width,settings.button_height)
		self.rect.centery = 350
		self.rect.centerx = screen.get_rect().centerx
		self.msg = "-1"
		self.msg_text = settings.button_font.render(self.msg, True, settings.button_text_color,settings.button_color)
		self.msg_text_rect = self.msg_text.get_rect()
		self.msg_text_rect.centery = self.rect.centery
		self.msg_text_rect.centerx = self.rect.centerx

	def draw(self,settings):
		self.screen.fill(settings.button_color,self.rect)
		self.screen.blit(self.msg_text,self.msg_text_rect)