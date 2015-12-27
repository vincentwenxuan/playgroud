import sys

import pygame

def check_event(player_ship):
    ''' in charge of checking the even like mouse move or quit '''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_ship.set_speed(1,None)
            elif event.key == pygame.K_LEFT:
                player_ship.set_speed(-1,None)
            elif event.key == pygame.K_UP:
                pass
                # disable vertical movement
                #player_ship.set_speed(None,-1)
            elif event.key == pygame.K_DOWN:
                pass
                # disable vertical movement
                #player_ship.set_speed(None,1)
        elif event.type == pygame.KEYUP:  
            if event.key == pygame.K_RIGHT:
                player_ship.set_speed(0,None)
            if event.key == pygame.K_LEFT:
                player_ship.set_speed(0,None)

def update_screen(ai_settings, screen, player_ship):
    ''' update all elements in screen according to settings '''

    screen.fill(ai_settings.bg_color)
    player_ship.blitme()
    pygame.display.flip()



