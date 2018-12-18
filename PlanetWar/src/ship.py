# -*- coding: utf-8 -*-

import pygame


class Ship():

	def __init__(self, screen):
		"""
		initialize the ship and it's initial location

		param
		@ screen: the screen of this game 
		"""

		self.screen = screen
		self.image = pygame.image.load('../images/ship1.bmp')
		self.rect = self.image.get_rect()  # get the region of image
		self.screen_rect = self.screen.get_rect()

		# put the ship to the bottom of screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# whether the ship should move
		self.move_right = False
		self.move_left = False
		self.move_up = False
		self.move_down = False

	def update(self):  
		"""
		update the location of ship
		"""

		if self.move_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += 1
		if self.move_left and self.rect.left > self.screen_rect.left:
			self.rect.centerx -= 1
		if self.move_up and self.rect.top > self.screen_rect.top:
			self.rect.centery -= 1    # y coordinate is inverse
		if self.move_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery += 1

	def blitme(self):
		self.screen.blit(self.image, self.rect)   # show the image in rect