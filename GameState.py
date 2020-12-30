class GameState():
    def __init__(self):
        self.active = False
        self.cats = []
        self.fish = []
        self.fish_left = 5

    def initiate(self,sb,play_button,settings,screen,state):
        self.cats = []
        self.fish_left = 5
        self.fish = []
        sb.prep_score(settings,0)
        sb.prep_fish(state,screen)
        play_button.msg_text = settings.button_font.render(play_button.msg, True, settings.button_text_color,settings.button_color)

