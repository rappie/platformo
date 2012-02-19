import os
import pygame

import settings

from gameobjects.gameobject import GameObject
from gameobjects.player import Player


# Maak de image hier aan zodat hij maar 1x wordt ingelezen.
imageExit = pygame.image.load(os.path.join(".", "data", "tiles", "exit.png"))


class Exit(GameObject):
	"""De uitgang van het level.
	"""
	
	def __init__(self, level, rect):
		GameObject.__init__(self, level, rect)

		# De image.		
		self.image = imageExit
	
	def collision(self, gameObject):
		"""Verwijder de coin.
		"""
		if isinstance(gameObject, Player):
			self.getLevel().setFinished(True)
		
	def collideVertical(self, gameObject):
		"""Stuur door naar generieke collision() methode.
		"""
		self.collision(gameObject)
		
	def collideHorizontal(self, gameObject):
		"""Stuur door naar generieke collision() methode.
		"""
		self.collision(gameObject)
	
	
