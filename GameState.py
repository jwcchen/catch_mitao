class GameState():
    def __init__(self):
        self.stage = 'home' # 'about' 'play' 'over'
        self.cats = []
        self.fish = []
        self.fish_left = 2
        self.score = 0

        self.fade_flag_fish = False
        self.fade_flag_level = False
        self.enter_level_flag = True

    def initiate(self,sb,play_button,settings,screen,state):
        self.cats = []
        self.fish_left = 2
        self.fish = []
        self.score = 0
        sb.prep_score(settings, 0)
        sb.prep_fish(state,screen)