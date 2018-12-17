# -*- coding: utf-8 -*-

import pygame


class Ship():

	def __init__(self, screen):
		"""
		initialize the ship and it's initial location
		"""

		self.screen = screen
		self.image = pygame.image.load('../images/ship1.bmp')
		self.rect = self.image.get_rect()  # get the region of image
		self.screen_rect = self.screen.get_rect()

		# put the ship to the bottom of screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def blitme(self):
		self.screen.blit(self.image, self.rect)   # show the image in rect