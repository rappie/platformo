import os
import pygame

import settings

from gameobjects.gameobject import GameObject
from gameobjects.player import Player


# Sounds inlezen.
soundCheer = pygame.mixer.Sound(os.path.join(".", "data", "sound", "cheer.wav"))

# Maak de image hier aan zodat hij maar 1x wordt ingelezen.
imageExit = pygame.image.load(os.path.join(".", "data", "tiles", "exit.png"))


class Exit(GameObject):
	"""De uitgang van het level.
	"""
	
	def __init__(self, level, rect):
		GameObject.__init__(self, level, rect)

		# De image.		
		self.image = imageExit
		
		# Bijhouden of er al een keer gefinished is omdat de collision detection
		# dubbel is.
		#
		self.finished = False
	
	def collision(self, gameObject):
		"""Verwijder de coin.
		"""
		if isinstance(gameObject, Player):
			if self.finished == False:
				soundCheer.play()
				self.getLevel().setFinished(True)
				self.finished = True
		
	def collideVertical(self, gameObject):
		"""Stuur door naar generieke collision() methode.
		"""
		self.collision(gameObject)
		
	def collideHorizontal(self, gameObject):
		"""Stuur door naar generieke collision() methode.
		"""
		self.collision(gameObject)
	
	
