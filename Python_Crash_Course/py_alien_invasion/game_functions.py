import sys

import pygame

def check_event(player_ship):
    ''' in charge of checking the even like mouse move or quit '''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                player_ship.moving_left = True
            elif event.key == pygame.K_UP:
                player_ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                player_ship.moving_down = True
        elif event.type == pygame.KEYUP:  
            if event.key == pygame.K_RIGHT:
                player_ship.moving_right = False
            if event.key == pygame.K_LEFT:
                player_ship.moving_left = False
            if event.key == pygame.K_UP:
                player_ship.moving_up = False
            if event.key == pygame.K_DOWN:
                player_ship.moving_down = False
def update_screen(ai_settings, screen, player_ship):
    ''' update all elements in screen according to settings '''

    screen.fill(ai_settings.bg_color)
    player_ship.blitme()
    pygame.display.flip()



