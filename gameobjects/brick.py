import pygame

import settings

from gameobjects.gameobject import GameObject


class Brick(GameObject):
	"""Een brick in het level.
	"""
	
	def __init__(self, position):
		GameObject.__init__(self)
		
		self.rect = pygame.Rect(position, (settings.TILE_WIDTH, settings.TILE_HEIGHT))
		
		
	
	
