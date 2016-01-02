


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
        self.max_bullets = 4

        # alien settings
        self.alien_size = 0.07 
        self.alien_speed_x = 0.7
        self.alien_drop_y = 30
        self.fleet_direction = 1 # right=1, left=-1
        
        # stat settings
        self.ships_limit = 3