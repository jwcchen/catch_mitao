import pygame.font

from BoxedCat import Fish

class Scoreboard():
	def __init__(self,screen,settings,score,high_score,state,msg_fade):
		self.screen = screen

		self.text_color = (255,255,255)
		self.font = pygame.font.SysFont(None, 48)

	
		self.prep_score(settings,score)
		self.prep_high_score(settings,high_score)
		self.prep_level(settings,score,msg_fade)
		self.prep_cat(state, settings)



	def prep_score(self,settings,score):
		#round it to nearest 10 and change integer to string
		rounded_score = int(round(score,-1))
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str,True,self.text_color,settings.bg_color)
		self.score_image_rect = self.score_image.get_rect()
		self.score_image_rect.right = self.screen.get_rect().right - 350
		self.score_image_rect.centery = self.score_image_rect.centery + 10

	def prep_high_score(self,settings,high_score):
		rounded_high_score = int(round(high_score,-1))
		high_score_string = "{:,}".format(rounded_high_score)
		self.high_score_image = self.font.render(high_score_string,True,self.text_color,settings.bg_color)
		self.high_score_image_rect = self.high_score_image.get_rect()
		self.high_score_image_rect.centerx = self.screen.get_rect().centerx + 50
		self.high_score_image_rect.centery = self.score_image_rect.centery

	def prep_level(self, settings, score,msg_fade):
		level = "L" + str((score // 750)+1)
		self.level_image = self.font.render(level, True, self.text_color, settings.bg_color)
		self.level_image_rect = self.level_image.get_rect()
		self.level_image_rect.left, self.level_image_rect.top = 10, 10
	
	def prep_fish(self,state,screen):
		
		for fish_number in range(state.fish_left):
				create_fish = Fish(screen)
				create_fish_rect = create_fish.rect
				create_fish.rect.x = 50 + fish_number * create_fish.rect.width
				# create_fish.rect.y = 10
				state.fish.append(create_fish)

	def prep_cat(self, state, settings):
		n_cat = str(len(state.cats))
		self.n_cat_image = self.font.render(n_cat, True, self.text_color, settings.bg_color)
		self.n_cat_image_rect = self.n_cat_image.get_rect()
		
		self.n_cat_image_rect.centerx = self.screen.get_rect().centerx - 110
		self.n_cat_image_rect.centery = self.score_image_rect.centery
		

	def draw_score(self):
		self.screen.blit(self.level_image,self.level_image_rect)
		self.screen.blit(self.score_image,self.score_image_rect)
		self.screen.blit(self.high_score_image,self.high_score_image_rect)
		self.screen.blit(self.n_cat_image,self.n_cat_image_rect)
		