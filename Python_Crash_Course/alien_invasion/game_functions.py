import sys
from time import sleep

import pygame

from alien import Alien

def check_event(player_ship, aliens, bullets, play_button, stats, ai_settings, screen):
    ''' in charge of checking the even like mouse move or quit '''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,player_ship, bullets)
        elif event.type == pygame.KEYUP:  
            check_keyup_event(event,player_ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_play_button(stats, play_button, aliens, bullets, ai_settings, player_ship, screen)

def check_play_button(stats, play_button, aliens, bullets, ai_settings, player_ship, screen):
    # TODO: defect: changed argument, too many arg, do multiple thing
    mouse_x, mouse_y = pygame.mouse.get_pos()

    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # reset and start the game
        stats.reset_stats()
        stats.game_active = True

        # empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # create a new fleet and center the ship
        create_fleet(screen, ai_settings, aliens)
        player_ship.init_position()


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


def update_screen(ai_settings, stats, screen, player_ship, bullets, aliens, play_button):
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

    # draw playbutton if game is not active
    if not stats.game_active:
        play_button.draw_button()
    
    # make the change!
    pygame.display.flip()

def update_bullets(bullets, aliens):
    ''' update bullets motion and delete unused bullets '''
    bullets.update()
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)

def update_ships(player_ship):
    # movement update 
    player_ship.update()


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    ''' Responde to ship being hit by alien '''
    if stats.ships_left > 0:
        # deduce one ship
        stats.ships_left -= 1

        # Empty all the ships
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(screen, ai_settings, aliens)
        ship.init_position()

        # Pause
        sleep(1)
    else:
        stats.game_active = False
        print "You lose!!!"


def update_aliens(screen, ai_settings, stats, aliens, ship, bullets):
    ''' update full fleet of aliens'''
    aliens.update()

    # repopulate
    if len(aliens) == 0:
        create_fleet(screen, ai_settings, aliens)
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


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

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    screen_bottom = screen.get_rect().bottom

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break



