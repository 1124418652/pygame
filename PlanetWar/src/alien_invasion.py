#-*- coding: utf-8 -*-
import pygame
import game_functions as gf 
from setting import Settings
from ship import Ship 
from alien import Alien
from pygame.sprite import Group


def run_game():
	# initialize the game and show the window of game

	pygame.init()
	ai_set = Settings()
	screen = pygame.display.set_mode((ai_set.screen_width, ai_set.screen_height))
	pygame.display.set_caption("Alian Invasion")

	ship = Ship(screen)
	aliens = Group()     # create a group to store aliens
	bullets = Group()    # create a group to store bullets

	# begin the main loop
	while True:
		
		# supervision the moment of mouse and keyboard
		gf.check_event(ai_set, screen, ship, bullets)
		ship.update()    # update the status of ship
		bullets.update() # update the status of bullet

		for bullet in bullets:
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)

		gf.update_screen(ai_set, screen, ship, bullets, aliens)

run_game()