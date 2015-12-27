import pygame

class Ship(object):
    """docstring for Ship"""
    def __init__(self, screen):
        
        self.screen = screen

        #Load the ship image
        self.surface = pygame.image.load('images/player.bmp')
        self.resize_ship(0.1)
        self.rect = self.surface.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the button center
        self.set_ship_positionx(self.screen_rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

        # ship movement: int either + or - 
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        self.set_speed(1,1)

    def blitme(self):
        ''' Draw the ship '''
        self.screen.blit(self.surface, self.rect)

    def resize_ship(self, scale):
        ''' resize ship surface according to scale arg'''
        current_size = self.surface.get_size()
        scaled_size = (int(current_size[0]*scale), int(current_size[1]*scale))
        self.surface = pygame.transform.scale(self.surface,scaled_size)

    def set_ship_positionx(self, centerx):
        ''' set ship center x coordinate '''
        self.rect.centerx = centerx

    def set_speed(self,x_speed,y_speed):
        ''' set the x y speed of ship, update() will be according to the speed'''
        if x_speed != None:
            self.speedx = x_speed
        if y_speed != None:
            self.speedy = y_speed

    def update(self):
        if self.moving_left == True:
            self.rect.centerx += -self.speedx
        if self.moving_right == True:
            self.rect.centerx += self.speedx
        if self.moving_up == True:
            self.rect.centery += -self.speedy
        if self.moving_down == True:
            self.rect.centery += self.speedy


