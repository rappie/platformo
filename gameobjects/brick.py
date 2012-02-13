import os
import pygame

import settings

from gameobjects.gameobject import GameObject


# Maak de image hier aan zodat hij maar 1x wordt ingelezen.
brickImage = pygame.image.load(os.path.join(".", "data", "tiles", "brick.png"))


class Brick(GameObject):
	"""Een brick in het level.
	"""
	
	def __init__(self, position):
		GameObject.__init__(self)

		# De image.		
		self.image = brickImage

		# De rect.
		self.rect = pygame.Rect(position, (settings.TILE_WIDTH, settings.TILE_HEIGHT))
		
		
		
	
	
