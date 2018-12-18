# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Sprite 

__all__ = ['Bullet']


class Bullet(Sprite):

	def __init__(self, ai_setting, screen, ship):
		super().__init__()    # inititalize the father class
		self.screen = screen

		# create a rectangle to place buttle and set it's location
		self.rect = pygame.Rect(0, 0, ai_setting.bullet_width
								, ai_setting.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		self.y = float(self.rect.y)  # store the location of bullet
		self.color = ai_setting.bullet_color
		self.speed_factor = ai_setting.bullet_speed_factor

	def update(self):
		self.y -= self.speed_factor
		self.rect.y = self.y

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)