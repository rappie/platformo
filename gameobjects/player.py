import os
import pygame

import settings

import inputstate
inputState = inputstate.getInstance()

from gameobjects.actor import Actor


# Plaatjes van de player.
imageStand = pygame.image.load(os.path.join(".", "data", "tiles", "player_stand.png"))
imageJump = pygame.image.load(os.path.join(".", "data", "tiles", "player_jump.png"))
walkImageList = []
walkImageList.append(pygame.image.load(os.path.join(".", "data", "tiles", "player_walk01.png")))
walkImageList.append(pygame.image.load(os.path.join(".", "data", "tiles", "player_walk02.png")))
walkImageList.append(pygame.image.load(os.path.join(".", "data", "tiles", "player_walk03.png")))
walkImageList.append(pygame.image.load(os.path.join(".", "data", "tiles", "player_walk04.png")))

# Sounds inlezen.
soundScream = pygame.mixer.Sound(os.path.join(".", "data", "sound", "scream.wav"))
soundJump = pygame.mixer.Sound(os.path.join(".", "data", "sound", "jump.wav"))
soundLand = pygame.mixer.Sound(os.path.join(".", "data", "sound", "land.wav"))
soundCrash = pygame.mixer.Sound(os.path.join(".", "data", "sound", "crash.wav"))


class Player(Actor):
	"""Object voor de player in een level.
		
		Deze klasse de attributen van de player bij en update de positie.
	
	"""
	
	def __init__(self, level, rect):
		Actor.__init__(self, level, rect)
		self.level = level
		
		# De image.
		self.image = imageStand.copy()
		
		# De huidige frame van een animatie waar de character in zit.
		self.animationFrame = 0
		
		# Laatste tick wanneer de animatie is geupdate.
		self.lastAnimationUpdate = 0
		
		# Health van de player.
		self.health = 100.0
		
		# Score van de player.
		self.score = 0

	def update(self):
		"""Extend het updaten van actor.
			De image moet worden geupdate. Uiteindelijk willen we hier een extra
			klasse voor 'AnimatedGameObject' oid. die dit voor ons afhandelt.
		"""
		Actor.update(self)
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
	
	def updateMovement(self):
		"""Handel de movement van de player af.
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
			
	def onFall(self):
		"""Laat een schrik-geluid horen als je valt.
		"""
		soundScream.play()

	def onLand(self):
		"""Laat een landing-geluid horen als je op de grond landt.
		"""
		soundLand.play()
		
	def takeFallDamage(self, verticalVelocity):
		"""Fall damage.
			Op dit moment is er geen damage maar alleen een geluid.
		"""
		soundCrash.play()
		self.health -= 20.0
		
	def takeDamage(self, amount):
		"""Normale damage.
		"""
		self.health -= amount
		
	def getHealth(self):
		"""Return de health van de player.
		"""
		return self.health
	
	def addScore(self, amount):
		"""Voeg score toe aan de score van de player.
		"""
		self.score += 1
		
	def getScore(self):
		"""Return de score van de player.
		"""
		return self.score