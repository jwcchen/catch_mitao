class GameState():
    def __init__(self):
        self.stage = 'home' # 'about' 'play' 'over'
        self.high_score = 0
        self.reset()

    def reset(self):
        self.cats = []
        self.fish_left = 5
        self.score = 0
