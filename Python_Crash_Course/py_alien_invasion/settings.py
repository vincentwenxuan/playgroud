


class Settings(object):
    """Settings for the alien invasion game"""
    def __init__(self):
        
        # general settings
        self.screen_size = (1200,800)
        self.bg_color = (40,40,40)

        # player ship settings
        self.player_speed = (1.5,0.5)
        self.player_size = 0.07

        # bullet settings
        self.bullet_speed = 2.5 # y speed only
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230,230,230)
