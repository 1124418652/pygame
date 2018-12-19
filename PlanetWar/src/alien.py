# -*- coding: utf-8 -*-

import pygame
import random
from pygame.sprite import Sprite

__all__ = ["Alien"]


class Alien(Sprite):

	count = 0   

	def __init__(self, screen):
		
		super().__init__()

		self.screen = screen
		self.image = pygame.image.load("../images/ufo.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		
		begin = self.rect.width // 2
		end = self.screen_rect.width - begin
		self.rect.centerx = random.randint(begin, end)    # the alien appears randomly
		self.rect.top = self.screen_rect.top
		self.rect.x = float(self.rect.x)
		self.rect.y = float(self.rect.y)
		self.x_speed_factor = 1
		self.y_speed_factor = 1

		Alien.count += 1

	def update(self):
		self.screen.blit(self.image, self.rect)
		direction = random.randint(0, 50)
		left_flag = False
		right_flag = False
		if 0 == direction and self.rect.right < self.screen_rect.right:
			right_flag = True
			left_flag = False
		elif 1 == direction and self.rect.left > self.screen_rect.left:
			left_flag = True
			right_flag = False
		self.rect.y += self.y_speed_factor
		if left_flag:
			self.rect.x -= self.x_speed_factor
		if right_flag:
			self.rect.x += self.x_speed_factor