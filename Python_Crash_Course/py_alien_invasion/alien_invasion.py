import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(ai_settings.screen_size)
    pygame.display.set_caption("alien_invasion")

    player_ship = Ship(screen)

    while True:
        gf.check_event(player_ship)
        player_ship.update()
        gf.update_screen(ai_settings, screen, player_ship)


run_game()
