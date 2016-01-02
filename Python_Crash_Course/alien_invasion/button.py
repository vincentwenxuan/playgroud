import pygame.font



class Button(object):
    """ Button object that rendered on pygame screen"""
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimension of the button
        self.button_width = 200
        self.button_height = 50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0,0,self.button_width,self.button_height)
        self.rect.center = self.screen_rect.center

        # The button msg needs to be initialize once 
        self.prep_msg(msg)

    def prep_msg(self,msg):
        """ turn msg into a rendered image and center text on the button """
        self.msg_image = self.font.render(msg, True, self.text_color,
                                        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """ Draw the button on the screen """
        # draw the button rect
        self.screen.fill(self.button_color, self.rect)
        # draw the msg on the button
        self.screen.blit(self.msg_image, self.msg_image_rect)






