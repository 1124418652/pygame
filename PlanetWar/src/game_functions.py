#-*- coding: utf-8 -*-

import sys
import pygame
from bullet import Bullet


def check_event(ai_setting, screen, ship, bullets):

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:

			if event.key == pygame.K_SPACE:
				new_bullet = Bullet(ai_setting, screen, ship)
				bullets.add(new_bullet)
			elif event.key == pygame.K_RIGHT:
				ship.move_right = True
			elif event.key == pygame.K_LEFT:
				ship.move_left = True
			elif event.key == pygame.K_UP:
				ship.move_up = True
			elif event.key == pygame.K_DOWN:
				ship.move_down = True

		elif event.type == pygame.KEYUP:
			
			if event.key == pygame.K_RIGHT:
				ship.move_right = False
			elif event.key == pygame.K_LEFT:
				ship.move_left = False
			elif event.key == pygame.K_UP:
				ship.move_up = False
			elif event.key == pygame.K_DOWN:
				ship.move_down = False
		
def update_screen(ai_setting, screen, ship, bullets, aliens):
	"""
	repaint the screen
	"""

	screen.fill(ai_setting.bg_color)
	ship.blitme()  # draw the ship
	aliens.blitme()

	for bullet in bullets.sprites():   # draw all bullets created
		bullet.draw_bullet()

	pygame.display.flip()

def add_alien():
