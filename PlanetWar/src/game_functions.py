import sys
import pygame


def check_event(ship):

	for event in pygame.event.get():

			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.type == pygame.K_RIGHT:
					ship.rect.centerx += 1
		
def update_screen(ai_setting, screen, ship):
	screen.fill(ai_setting.bg_color)
	ship.blitme()
	pygame.display.flip()