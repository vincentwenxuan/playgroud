import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(ai_settings.screen_size)
    pygame.display.set_caption("alien_invasion")

    player_ship = Ship(screen, ai_settings)
    alien = Alien(screen, ai_settings)

    bullets = Group()
    

    while True:
        gf.check_event(player_ship, bullets)

        gf.update_ships(player_ship)
        gf.update_bullets(bullets)

        # screen display update
        gf.update_screen(ai_settings, screen, player_ship, bullets, alien)
        




run_game()
