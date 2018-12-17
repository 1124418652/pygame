#-*- coding: utf-8 -*-
import pygame
import game_functions as gf 
from setting import Settings
from ship import Ship 


def run_game():
	# initialize the game and show the window of game

	pygame.init()
	ai_set = Settings()
	screen = pygame.display.set_mode((ai_set.screen_width, ai_set.screen_height))
	pygame.display.set_caption("Alian Invasion")

	ship = Ship(screen)

	# begin the main loop
	while True:
		
		# supervision the moment of mouse and keyboard
		gf.check_event()
		gf.update_screen(ai_set, screen, ship)

run_game()