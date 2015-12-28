import pygame

from bullet import Bullet


class Ship(object):
    """docstring for Ship"""
    def __init__(self, screen, settings):
        
        self.screen = screen
        self.settings = settings

        #Load the ship image
        self.surface = pygame.image.load('images/player.bmp')
        self.resize_ship(self.settings.player_size)
        self.rect = self.surface.get_rect()
        self.screen_rect = screen.get_rect()

        # initialize ship real and display position
        self.init_position()

        # initialize ship speed and movement state
        self.init_movement()

    def init_position(self):
        # the real postion (since display position only take int)
        self.real_positionx = float(self.screen_rect.centerx)
        self.real_positiony = float(self.screen_rect.bottom - self.surface.get_height()*0.5)
        # Start each new ship at the button center
        self.set_display_position(self.real_positionx,self.real_positiony)
   
    def init_movement(self):
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

    def set_display_position(self, centerx, centery):
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
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.real_positionx += -self.speedx
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.real_positionx += self.speedx
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.real_positiony += -self.speedy
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.real_positiony += self.speedy

        self.set_display_position(self.real_positionx, self.real_positiony)



    def fire_bullet(self, bullets_group):
        ''' fire bullet, add bullet into bullets group '''

        if len(bullets_group) < self.settings.max_bullets:
            new_bullet = Bullet(self.screen, self.settings, self)
            bullets_group.add(new_bullet)




