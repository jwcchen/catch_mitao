class GameState():
    def __init__(self):
        self.stage = 'home' # 'about' 'play' 'over'
        self.high_score = 0

        self.fade_flag_fish = False
        self.fade_flag_level = False
        self.enter_level_flag = True

        self.reset()
        # = GameState.reset(self)

    def reset(self):
        self.cats = []
        self.fish_left = 2
        self.score = 0
