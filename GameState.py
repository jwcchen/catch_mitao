class GameState():
    def __init__(self):
        self.active = False
        self.cats = []
        self.fish = []
        self.fish_left = 5

    def initiate(self,sb,play_button,settings,screen):
        self.cats = []
        self.fish_left = 5
        self.fish = []
        cat_position = {0:(600,400)}
        score = 0
        sb.prep_score(settings,score)
        sb.prep_fish(score,self,screen)
        play_button.msg_text = settings.button_font.render(play_button.msg, True, settings.button_text_color,settings.button_color)

