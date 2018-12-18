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

		Alien.count += 1

	def update(self):
		pass

	def blitme(self):
		self.screen.blit(self.image, self.rect)
		