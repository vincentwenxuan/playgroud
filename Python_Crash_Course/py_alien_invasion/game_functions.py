import sys

import pygame

from alien import Alien

def check_event(player_ship, bullets):
    ''' in charge of checking the even like mouse move or quit '''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,player_ship, bullets)
        elif event.type == pygame.KEYUP:  
            check_keyup_event(event,player_ship)

def check_keydown_event(event,player_ship, bullets):
    '''check when key pressed'''
    if event.key == pygame.K_RIGHT:
        player_ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        player_ship.moving_left = True
    elif event.key == pygame.K_UP:
        player_ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        player_ship.moving_down = True 

    elif event.key == pygame.K_SPACE:
        player_ship.fire_bullet(bullets)

def check_keyup_event(event,player_ship):
    '''check when key released'''
    if event.key == pygame.K_RIGHT:
        player_ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        player_ship.moving_left = False
    elif event.key == pygame.K_UP:
        player_ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        player_ship.moving_down = False


def update_screen(ai_settings, screen, player_ship, bullets, aliens):
    ''' update all elements in screen according to settings '''

    # draw screen
    screen.fill(ai_settings.bg_color)

    # draw player
    player_ship.blitme()

    # draw alien
    aliens.draw(screen)
    
    # draw bullet
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    
    # make the change!
    pygame.display.flip()

def update_bullets(bullets):
    ''' update bullets motion and delete unused bullets '''
    bullets.update()
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_ships(player_ship):
    # movement update 
    player_ship.update()


def create_fleet(screen, ai_settings, aliens):
    ''' create a full fleet of aliens '''
    alien = Alien(screen, ai_settings)
    number_aliens_x = get_numer_alien_inrow(ai_settings, alien.rect.width)
    number_rows = get_numer_rows(ai_settings,alien.rect.height)

    # Create the first row of ships
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # create an alien and place it in the row
            create_alien(screen, ai_settings, aliens, alien_number, row_number)

def get_numer_rows(ai_settings, alien_height):
    ''' determine the number of rows of the fleet -> int '''
    # half the screen 
    available_space_y = ai_settings.screen_size[1]/2
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows

def get_numer_alien_inrow(ai_settings, alien_width):
    ''' determine the number of alien in a row -> int '''
    screen_width = ai_settings.screen_size[0]
    available_space_x = screen_width - 2*alien_width
    number_aliens_x = int(available_space_x / (2*alien_width)) 
    return number_aliens_x


def create_alien(screen, ai_settings, aliens, alien_number, row_number):
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien_x =  alien_width + 2*alien_width*alien_number
    alien_y = alien_height + 2*alien_height*row_number

    alien.set_position(alien_x, alien_y)
    aliens.add(alien)


