import os
import pygame

import settings

from gameobjects.gameobject import GameObject
from gameobjects.player import Player


# Lees geluiden in.
soundCoin = pygame.mixer.Sound(os.path.join(".", "data", "sound", "coin.wav"))

# Maak de image hier aan zodat hij maar 1x wordt ingelezen.
imageCoin = pygame.image.load(os.path.join(".", "data", "tiles", "coin.png"))


class Coin(GameObject):
	"""Een coin in het level.
	"""
	
	def __init__(self, level, rect):
		GameObject.__init__(self, level, rect)

		# De image.		
		self.image = imageCoin
	
	def collision(self, gameObject):
		"""Verwijder de coin.
		"""
		if isinstance(gameObject, Player):
			gameObject.addScore(1)
			soundCoin.play()
			self.remove()
		
	def collideVertical(self, gameObject):
		"""Stuur door naar generieke collision() methode.
		"""
		self.collision(gameObject)
		
	def collideHorizontal(self, gameObject):
		"""Stuur door naar generieke collision() methode.
		"""
		self.collision(gameObject)
	
	
