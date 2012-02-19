import os
import random
import pygame

import settings

from gameobjects.actor import Actor
from gameobjects.player import Player


# Maak de image hier aan zodat hij maar 1x wordt ingelezen.
imageMonster = pygame.image.load(os.path.join(".", "data", "tiles", "monster.png"))


class Monster(Actor):
	"""Een simpel monster.
	"""
	
	def __init__(self, level, rect):
		Actor.__init__(self, level, rect)

		# De image.		
		self.image = imageMonster
		
		# Snelheid van het monster.
		self.speed = 1
		
		# Variabelen voor het veranderen van richting.
		self.nextMovementSwitch = 0
		self.movementSwitch = False
	
	def updateMovement(self):
		"""Update movement van het monster.
		"""
		
		# Haal ticks op.
		ticks = pygame.time.get_ticks()
		
		# Als het tijd is om te veranderen van richting.
		if ticks > self.nextMovementSwitch:
			
			# Verander van richting.
			self.velocityX = self.speed if self.movementSwitch == True else -self.speed
			
			# Sla nieuwe status van richting shit op.
			self.nextMovementSwitch = ticks + random.randint(1000, 5000)
			self.movementSwitch = not self.movementSwitch
		
	def collision(self, gameObject):
		"""Verwijder de coin.
		"""
		if isinstance(gameObject, Player):
			gameObject.takeDamage(10.0)
			self.remove()
		
	def collideVertical(self, gameObject):
		"""Stuur door naar generieke collision() methode.
		"""
		self.collision(gameObject)
		
	def collideHorizontal(self, gameObject):
		"""Stuur door naar generieke collision() methode.
		"""
		self.collision(gameObject)
	
