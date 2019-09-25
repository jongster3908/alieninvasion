import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # initialize
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make play button
    play_button = Button(ai_settings, screen, "Play")

    # create instance to store game stats
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # make ship
    ship = Ship(ai_settings, screen)

    # make group to store bullets
    bullets = Group()
    aliens = Group()

    # create fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start main loop
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()