# -*- coding: utf-8 -*-


class Settings():
	"""
	store the settings of the game
	"""

	def __init__(self):

		# the setting of screen 
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# the setting of bullet
		self.bullet_color = (20, 40, 50)
		self.bullet_speed_factor = 10
		self.bullet_width = 5
		self.bullet_height = 10

		# the setting of aliens
		self.alien_num = 10