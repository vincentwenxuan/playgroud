import pygame

class Ship(object):
    """docstring for Ship"""
    def __init__(self, screen, settings):
        
        self.screen = screen
        self.settings = settings

        #Load the ship image
        self.surface = pygame.image.load('images/player.bmp')
        self.resize_ship(0.1)
        self.rect = self.surface.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the button center
        self.set_display_positionx(self.screen_rect.centerx,0)
        self.rect.bottom = self.screen_rect.bottom

        # the real postion (since display position only take int)
        self.real_positionx = float(self.screen_rect.centerx)
        self.real_positiony = float(self.screen_rect.centery)

        # ship movement 
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        self.set_speed(self.settings.player_speed[0],self.settings.player_speed[1])

    def blitme(self):
        ''' Draw the ship '''
        self.screen.blit(self.surface, self.rect)

    def resize_ship(self, scale):
        ''' resize ship surface according to scale arg'''
        current_size = self.surface.get_size()
        scaled_size = (int(current_size[0]*scale), int(current_size[1]*scale))
        self.surface = pygame.transform.scale(self.surface,scaled_size)

    def set_display_positionx(self, centerx,centery):
        ''' set ship center x coordinate '''
        self.rect.centerx = int(centerx)
        self.rect.centery = int(centery)

    def set_speed(self,x_speed,y_speed):
        ''' set the x y speed of ship, update() will be according to the speed'''
        if x_speed != None:
            self.speedx = x_speed
        if y_speed != None:
            self.speedy = y_speed

    def update(self):
        # update real movement and display movement 
        if self.moving_left == True :
            self.real_positionx += -self.speedx
        if self.moving_right == True:
            self.real_positionx += self.speedx
        if self.moving_up == True:
            self.real_positiony += -self.speedy
        if self.moving_down == True:
            self.real_positiony += self.speedy

        self.set_display_positionx(self.real_positionx, self.real_positiony)


