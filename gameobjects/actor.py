import os
import pygame

import settings

from gameobjects.gameobject import GameObject


class Actor(GameObject):
	"""Een actor game object.
	
		Een actor houdt in dat het object actief acties doet. Er zit dus physics
		in voor lopen/vallen/etc. en collision detection.
		
		De movement van de actor kan je zelf bepalen als je 'updateMovement()'
		overschrijft.
	
	"""
	
	def __init__(self, level, rect):
		GameObject.__init__(self, level, rect)

		# De snelheid.
		self.velocityX = 0
		self.velocityY = 0

		# Oude waardes van positie en snelheid.
		#
		# Dit kan worden gebruikt om te zien wat er in het vorige frame
		# gebeurde. Je kan bijvoorbeeld bepalen of je al op de grond stond de
		# vorige frame of dat je net geland bent.
		#
		self.oldVelocityX = self.velocityX
		self.oldVelocityY = self.velocityY
		self.oldRect = self.rect.copy()

		# Variabele die bepaalt of je op de grond staat.
		#
		# Deze wordt elk frame opnieuw bepaald. Als je collide met een
		# gameobject dat onder je zit wordt deze op True gezet.
		#
		self.onGround = False
		
		# Variabele die bepaalt of je aan het springen bent.
		#
		# Zodra je 'stopt' met springen wordt deze op false gezet. Dit kan ge-
		# bruikt worden om je jump off te cutten zodat je controle hebt over
		# hoe hoog je springt door eerder de key los te laten.
		#
		self.jumping = False
		
		# Variabele die bepaalt of je aan het vallen bent.
		#
		# Vallen betekent dat je je op maxspeed naar beneden beweegt en dat je
		# fall damage moet krijgen.
		#
		self.falling = False

	def update(self):
		"""Update de actor.
		"""
		self.updateMovement()
		self.updatePhysics()
		
	def updateMovement(self):
		"""Update de movement.
			Een default actor staat stil, dus hier doen we niks.
		"""
		pass
	
	def onFall(self):
		"""Methode die wordt aangeroepen als de actor valt.
		"""
		pass

	def updatePhysics(self):
		"""Update de physics.
		"""
		
		# Zwaartekracht.
		if 1 > self.velocityY  > -1:
			self.velocityY += 1
		else:
			self.velocityY += settings.GRAVITY

		# Max speed.
		if self.velocityX > settings.PLAYER_MAX_SPEED_HORIZONTAL:
			self.velocityX = settings.PLAYER_MAX_SPEED_HORIZONTAL
		if self.velocityX < -settings.PLAYER_MAX_SPEED_HORIZONTAL:
			self.velocityX = -settings.PLAYER_MAX_SPEED_HORIZONTAL
		if self.velocityY > settings.PLAYER_MAX_SPEED_VERTICAL:
			self.velocityY = settings.PLAYER_MAX_SPEED_VERTICAL
		if self.velocityY < -settings.PLAYER_MAX_SPEED_VERTICAL:
			self.velocityY = -settings.PLAYER_MAX_SPEED_VERTICAL

		# Bepaal of je aan het vallen bent.
		if self.velocityY >= settings.PLAYER_MAX_SPEED_VERTICAL:
			if self.oldVelocityY < settings.PLAYER_MAX_SPEED_VERTICAL:
				self.onFall()
			self.falling = True
			
		# Move eerst verticaal.
		self.checkVerticalCollisions()
		self.rect = self.rect.move((0, self.velocityY))

		# Move daarna horizontaal.
		self.checkHorizontalCollisions()
		self.rect = self.rect.move((self.velocityX, 0))
		
		# Sla de snelheid/positie op zodat de volgende frame dit zou kunnen
		# gebruiken.
		#
		self.oldVelocityX = self.velocityX
		self.oldVelocityY = self.velocityY
		self.oldRect = self.rect.copy()

	def checkVerticalCollisions(self):
		"""Voer collision detection uit voor de verticale as.
		"""
		
		# Ga er van uit dat we in de lucht zweven.
		#
		# Als er een collision plaatsvindt met de grond onder ons wordt deze
		# in het loopje vanzelf weer op True gezet.
		#
		self.onGround = False
		
		# Loop alle game objects bij langs.
		for gameObject in self.level.cluster.getGameObjectList(self.getClusterCollisionRect()):
			
			# Vertical collision detection.
			verticalMoveRect = self.rect.move((0, self.velocityY))
			if verticalMoveRect.colliderect(gameObject) == True:

				# Voer collision uit.
				gameObject.collideVertical(self)
				
	def checkHorizontalCollisions(self):
		"""Voer collision detection uit voor de horizontale as.
		"""
		
		# Loop alle game objects bij langs.
		for gameObject in self.level.cluster.getGameObjectList(self.getClusterCollisionRect()):
			
			# Horizontal collision detection.
			horizontalMoveRect = self.rect.move((self.velocityX, 0))
			if horizontalMoveRect.colliderect(gameObject) == True:
				
				# Voer collision uit.
				gameObject.collideHorizontal(self)

	def getClusterCollisionRect(self):
		"""Return rect waarbinnen we game objects moeten ophalen om te checken
			op collisions.
			
			Dit is de rect van de player met daaromheen net zoveel pixels als
			de max speed van de player.
		"""
		return self.rect.inflate((settings.PLAYER_MAX_SPEED_HORIZONTAL*2, settings.PLAYER_MAX_SPEED_VERTICAL*2))



