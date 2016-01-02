




class GameStats():
    """ Statistics for Alien Invasion  """
    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        
        self.game_active = False


    def reset_stats(self):
        ''' (re)initialize stats '''
        self.ships_left = self.settings.ships_limit
        
