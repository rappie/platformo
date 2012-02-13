import os
import pygame

import settings

import inputstate
inputState = inputstate.getInstance()

from gameobjects.gameobject import GameObject


# Basis plaatje van de player.
imageBase = pygame.image.load(os.path.join(".", "data", "tiles", "player.png"))


class Player(GameObject):
	"""Object voor de player in een level.
		
		Deze klasse de attributen van de player bij en update de positie.
	
	"""
	
	def __init__(self, level):
		GameObject.__init__(self)
		self.level = level
		
		# De image.
		self.image = imageBase.copy()

		# De rect van de player.
		initialX = 1*settings.TILE_WIDTH
		initialY = (settings.LEVEL_HEIGHT-2)*settings.TILE_HEIGHT
		self.rect = pygame.Rect(initialX, initialY, settings.TILE_WIDTH, settings.TILE_HEIGHT)
		
		# De snelheid.
		self.velocityX = 0
		self.velocityY = 0
		
		# Variabele die bepaalt of je op de grond staat.
		self.onGround = False
		
		# Variabele die bepaalt of je aan het springen bent.
		self.jumping = False
		
	def update(self):
		"""Update de player.
		"""
		self.updatePosition()
		self.updateImage()
		
	def updateImage(self):
		"""Update de image van de player.
		"""
		# Als je naar links loopt het basis plaatje flippen.
		if self.velocityX < 0:
			self.image = pygame.transform.flip(imageBase, True, False)

		# Als je naar rechts loopt het basis plaatje zoals hij normaal is.		
		elif self.velocityX > 0:
			self.image = imageBase.copy()
	
	def updatePosition(self):
		"""Update de position van de player.
		"""
		
		# Check of de gebruiker een jump heeft onderbroken.
		if self.jumping == True and inputState.getMovementState("up") == False:
			self.jumping = False
			
			# Vertraag de jump.
			if self.velocityY < settings.PLAYER_JUMP_CUTOFF_SPEED:
				self.velocityY = settings.PLAYER_JUMP_CUTOFF_SPEED
		
		# Springen.
		if inputState.getMovementState("up") == True:
			
			# Als je al springt kan je niet nog eens springen
			if self.jumping == False:
			
				# Je kan alleen springen als je op de grond staat.
				if self.onGround == True:
					
					self.velocityY = settings.PLAYER_JUMP_SPEED
					self.jumping = True
		
		# Naar rechts lopen.
		if inputState.getMovementState("right") == True:
			if self.velocityX <= 0:
				self.velocityX += 1
			else:
				self.velocityX += settings.PLAYER_WALK_SPEED
		
		# Naar links lopen.
		elif inputState.getMovementState("left") == True:
			if self.velocityX >= 0:
				self.velocityX += -1
			else:
				self.velocityX += -settings.PLAYER_WALK_SPEED
		
		# Als je niks doet sta je stil.
		else:
			self.velocityX = 0

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

		# Move eerst verticaal.
		self.collideVertical()
		self.rect = self.rect.move((0, self.velocityY))

		# Move daarna horizontaal.
		self.collideHorizontal()
		self.rect = self.rect.move((self.velocityX, 0))

	def collideVertical(self):
		"""Voer collision detection uit voor de verticale as.
		"""
		
		# Ga er van uit dat we in de lucht zweven.
		self.onGround = False
		
		# Loop alle bricks in de omgeving van de player bij langs.
		for brick in self.level.cluster.getGameObjectList(self.getClusterCollisionRect()):
			
			# Vertical collision detection.
			verticalMoveRect = self.rect.move((0, self.velocityY))
			if verticalMoveRect.colliderect(brick) == True:
				
				# Als je naar beneden moved.
				if self.velocityY > 0:
					self.velocityY = brick.rect.top - self.rect.bottom
					self.onGround = True
					self.jumping = False
					
				# Als je naar boven moved.
				elif self.velocityY < 0:
					self.velocityY = self.rect.top - brick.rect.bottom
		
	def collideHorizontal(self):
		"""Voer collision detection uit voor de verticale as.
		"""
		
		# Loop alle bricks in de omgeving van de player bij langs.
		for brick in self.level.cluster.getGameObjectList(self.getClusterCollisionRect()):
			
			# Horizontal collision detection.
			horizontalMoveRect = self.rect.move((self.velocityX, 0))
			if horizontalMoveRect.colliderect(brick) == True:
				
				# Als je naar rechts moved.
				if self.velocityX > 0:
					self.velocityX = brick.rect.left - self.rect.right
					
				# Als je naar links moved.
				elif self.velocityX < 0:
					self.velocityX = self.rect.left - brick.rect.right
	
	def getClusterCollisionRect(self):
		"""Return rect waarbinnen we game objects moeten ophalen om te checken
			op collisions.
			
			Dit is de rect van de player met daaromheen net zoveel pixels als
			de max speed van de player.
		"""
		return self.getRect().inflate((settings.PLAYER_MAX_SPEED_HORIZONTAL*2, settings.PLAYER_MAX_SPEED_VERTICAL*2))
	
	def getRect(self):
		"""Return de rect van de player.
		"""
		return self.rect
	
