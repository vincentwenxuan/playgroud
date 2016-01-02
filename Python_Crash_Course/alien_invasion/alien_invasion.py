import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet
from game_stats import GameStats
from button import Button

import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(ai_settings.screen_size)
    pygame.display.set_caption("alien_invasion")

    play_button = Button(ai_settings, screen, "Play")

    # initialize game stats
    stats = GameStats(ai_settings)

    # initialize player ship
    player_ship = Ship(screen, ai_settings)
    

    # create sprite groups for bullets and aliens
    bullets = Group()
    aliens = Group()

    # create fleet of alien
    gf.create_fleet(screen, ai_settings, aliens)

    while True:
        gf.check_event(player_ship, aliens, bullets, play_button, stats, ai_settings, screen)

        if stats.game_active == True:
            gf.update_ships(player_ship)
            gf.update_bullets(bullets, aliens)
            gf.update_aliens(screen, ai_settings, stats, aliens, player_ship, bullets)
        
        # screen display update
        gf.update_screen(ai_settings, stats, screen, player_ship, bullets, aliens, play_button)
        



if __name__ == '__main__':
    run_game()
