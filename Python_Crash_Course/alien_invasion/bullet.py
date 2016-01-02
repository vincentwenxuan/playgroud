import pygame

# Sprite class is for manageing objects in group
from pygame.sprite import Sprite  

class Bullet(Sprite):
    """docstring for Bullet"""
    def __init__(self, screen, ai_settings, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        # create bullet position at the tip of the ship
        self.rect = pygame.Rect(0,0,
                            ai_settings.bullet_width,
                            ai_settings.bullet_height,)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # initialize color
        self.color = ai_settings.bullet_color

        # initialize the position of the bullet
        self.real_y = float(self.rect.y)
        self.speed_y = ai_settings.bullet_speed

    def update(self):
        ''' move the bullet up the screen '''
        # update real position
        self.real_y -= self.speed_y

        # update display position
        self.rect.y = int(self.real_y)


    def draw_bullet(self):
        ''' draw the bullet on the screen '''
        pygame.draw.rect(self.screen, self.color, self.rect)








