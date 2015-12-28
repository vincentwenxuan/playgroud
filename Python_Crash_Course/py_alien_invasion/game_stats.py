




class GameStats():
    """ Statistics for Alien Invasion  """
    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()

    def reset_stats(self):
        ''' (re)initialize stats '''
        self.ships_left = self.settings.ships_limit
        self.game_active = True
