import os
import pygame

import settings

from gameobjects.gameobject import GameObject


# Lees geluiden in.
soundLand = pygame.mixer.Sound(os.path.join(".", "data", "sound", "land.wav"))
soundCrash = pygame.mixer.Sound(os.path.join(".", "data", "sound", "crash.wav"))

# Image van brick.
brickImage = pygame.image.load(os.path.join(".", "data", "tiles", "brick.png"))


class Brick(GameObject):
	"""Een brick in het level.
	"""
	
	def __init__(self, level, position):
		GameObject.__init__(self, level)

		# De image.		
		self.image = brickImage

		# De rect.
		self.rect = pygame.Rect(position, (settings.TILE_WIDTH, settings.TILE_HEIGHT))

	def collideVertical(self, gameObject):
		"""Voer verticale collision detection uit met game object.
		"""
		
		# Als er naar beneden wordt gemoved.
		if gameObject.velocityY > 0:
			
			# Pas de speed aan.
			gameObject.velocityY = self.rect.top - gameObject.rect.bottom
			
			# Als de aangepaste speed nul is betekent het dat je op de grond
			# staat. Dit kan zowel betekenen dat je op de grond rondloopt of dat
			# je net uit de lucht landt.
			#
			if not gameObject.velocityY > 0:

				# Als dit de eerste frame is dat je op de grond staat
				# moet er een geluid worden afgespeeld.
				#
				if gameObject.oldVelocityY > 0:
					
					# Speel afhankelijk van hoe je valt een ander geluid af.
					if gameObject.falling == False:
						soundLand.play()
					else:
						soundCrash.play()

				# Update alle statussen.
				gameObject.onGround = True
				gameObject.jumping = False
				gameObject.falling = False
			
		# Als er naar boven wordt gemoved.
		elif gameObject.velocityY < 0:
			gameObject.velocityY = gameObject.rect.top - self.rect.bottom

	def collideHorizontal(self, gameObject):
		"""Voer horizontale collision detection uit met game object.
		"""

		# Als er naar rechts wordt gemoved.
		if gameObject.velocityX > 0:
			gameObject.velocityX = self.rect.left - gameObject.rect.right
			
		# Als er naar links wordt gemoved.
		elif gameObject.velocityX < 0:
			gameObject.velocityX = gameObject.rect.left - self.rect.right
		
