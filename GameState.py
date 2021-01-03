class GameState():
    def __init__(self):
        self.active = False
        self.cats = []
        self.cat_id = 0
        self.cat_position = {0: [600, 400]}
        self.fish = []
        self.fish_left = 5


        self.music_flag = True
        self.about_flag = False
        self.three_button_flag = True
        self.break_flag = False
        self.generate_flag = False
        self.fade_flag_fish = False
        self.home_flag = False
        self.fade_flag_level = False
        self.enter_level_flag = True

    def initiate(self,sb,play_button,settings,screen,state):
        self.cats = []
        self.fish_left = 5
        self.fish = []
        sb.prep_score(settings,0)
        sb.prep_fish(state,screen)
        play_button.msg_text = settings.button_font.render(play_button.msg, True, settings.button_text_color,settings.button_color)


