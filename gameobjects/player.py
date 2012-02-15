import os
import pygame

import settings

import inputstate
inputState = inputstate.getInstance()

from gameobjects.gameobject import GameObject


# Plaatjes van de player.
imageStand = pygame.image.load(os.path.join(".", "data", "tiles", "player_stand.png"))
imageJump = pygame.image.load(os.path.join(".", "data", "tiles", "player_jump.png"))
walkImageList = []
walkImageList.append(pygame.image.load(os.path.join(".", "data", "tiles", "player_walk01.png")))
walkImageList.append(pygame.image.load(os.path.join(".", "data", "tiles", "player_walk02.png")))
walkImageList.append(pygame.image.load(os.path.join(".", "data", "tiles", "player_walk03.png")))
walkImageList.append(pygame.image.load(os.path.join(".", "data", "tiles", "player_walk04.png")))

# Geluiden.
soundJump = pygame.mixer.Sound(os.path.join(".", "data", "sound", "jump.wav"))
soundScream = pygame.mixer.Sound(os.path.join(".", "data", "sound", "scream.wav"))

class Player(GameObject):
	"""Object voor de player in een level.
		
		Deze klasse de attributen van de player bij en update de positie.
	
	"""
	
	def __init__(self, level):
		GameObject.__init__(self)
		self.level = level
		
		# De image.
		self.image = imageStand.copy()
		
		# De huidige frame van een animatie waar de character in zit.
		self.animationFrame = 0
		
		# Laatste tick wanneer de animatie is geupdate.
		self.lastAnimationUpdate = 0

		# De rect van de player.
		initialX = 1*settings.TILE_WIDTH
		initialY = (settings.LEVEL_HEIGHT-2)*settings.TILE_HEIGHT
		self.rect = pygame.Rect(initialX, initialY, settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT)
		
		# De snelheid.
		self.velocityX = 0
		self.velocityY = 0
		
		# Variabele die bepaalt of je op de grond staat.
		self.onGround = False
		
		# Variabele die bepaalt of je aan het springen bent.
		self.jumping = False
		
		# Variabele die bepaalt of je aan het vallen bent.
		#
		# Vallen betekent dat je je op maxspeed naar beneden beweegt en dat je
		# fall damage moet krijgen.
		#
		self.falling = False
		
	def update(self):
		"""Update de player.
		"""
		self.updatePosition()
		self.updateImage()
		
	def updateImage(self):
		"""Update de image van de player.
		"""
		# Als je springt.
		if self.onGround == False:
			self.image = imageJump.copy()

		# Movement naar links of rechts.
		elif self.velocityX != 0:
			
			# Haal ticks op.
			ticks = pygame.time.get_ticks()

			# Check of er een nieuwe frame getoond moet worden.
			if ticks - self.lastAnimationUpdate > settings.PLAYER_ANIMATION_SPEED:
				self.animationFrame += 1
				self.lastAnimationUpdate = ticks
			
			# Check of de nieuwe frame binnen de bounds van de image list past.
			if self.animationFrame >= len(walkImageList):
				self.animationFrame = 0

			# Haal frame op.
			walkImage = walkImageList[self.animationFrame]

			# Naar rechts lopen. Neem plaatje zoals hij is.
			if self.velocityX > 0:
				self.image = walkImage.copy()
				
			# Naar links lopen. Flip het plaatje.
			elif self.velocityX < 0:
				self.image = pygame.transform.flip(walkImage, True, False)
		
		# Als je stilstaat.
		elif self.velocityX == 0:
			self.image = imageStand.copy()
	
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
					
					# Update speed en enable jumpen.
					self.velocityY = settings.PLAYER_JUMP_SPEED
					self.jumping = True
					
					# Speel jump geluid af.
					soundJump.play()
		
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

		# Bepaal of je aan het vallen bent.
		if self.velocityY >= settings.PLAYER_MAX_SPEED_VERTICAL:
			if self.oldVelocityY < settings.PLAYER_MAX_SPEED_VERTICAL:
				soundScream.play()
			self.falling = True
			
		# Move eerst verticaal.
		self.collideVertical()
		self.rect = self.rect.move((0, self.velocityY))

		# Move daarna horizontaal.
		self.collideHorizontal()
		self.rect = self.rect.move((self.velocityX, 0))
		
		# Sla de snelheid/positie op zodat de volgende frame dit zou kunnen
		# gebruiken.
		#
		self.oldVelocityX = self.velocityX
		self.oldVelocityY = self.velocityY
		self.oldRect = self.rect.copy()

	def collideVertical(self):
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

				gameObject.collideVertical(self)
				
	def collideHorizontal(self):
		"""Voer collision detection uit voor de verticale as.
		"""
		
		# Loop alle game objects bij langs.
		for gameObject in self.level.cluster.getGameObjectList(self.getClusterCollisionRect()):
			
			# Horizontal collision detection.
			horizontalMoveRect = self.rect.move((self.velocityX, 0))
			if horizontalMoveRect.colliderect(gameObject) == True:
				
				gameObject.collideHorizontal(self)
				
	
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
	
