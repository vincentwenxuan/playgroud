import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """docstring for Alien"""
    def __init__(self, screen, settings):
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings
        
        #Load the alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.resize_ship(self.settings.alien_size)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.init_position()
        self.speed_x = self.settings.alien_speed_x

    def init_position(self):
        ''' initialize alien at the top left of screen '''
        start_x = self.screen_rect.left + self.rect.width
        start_y = self.screen_rect.top + self.rect.height
        self.set_position(start_x,start_y)

    def set_position(self, x, y):
        ''' set the display and real position, None means no change '''
        if x != None:
            self.real_x = float(x)
            self.rect.x = int(self.real_x)
        if y != None:
            self.real_y = float(y)
            self.rect.y = int(self.real_y)
        
    def blitme(self):
        ''' Draw alien on the screen'''
        self.screen.blit(self.image, self.rect)


    def resize_ship(self, scale):
        ''' resize ship image according to scale arg'''
        current_size = self.image.get_size()
        scaled_size = (int(current_size[0]*scale), int(current_size[1]*scale))
        self.image = pygame.transform.scale(self.image,scaled_size)

    def update(self):
        ''' update the position of alien '''
        self.set_position(self.real_x + self.speed_x, y=None)
        
        # check if bump, inverse speed
        if self.check_bump() == True:
            self.set_position(x=None, y=self.real_y+self.settings.alien_drop_y)
            self.speed_x = -self.speed_x


    def check_bump(self):
        '''Check whether alien hit the wall -> bool '''
    
        if (self.rect.right >= self.screen_rect.right or
            self.rect.left <= self.screen_rect.left):
            return True
        else:
            return False