import os
import pygame

from gameobjects.actor import Actor


class Camera(object):
	"""Camera klasse.
	
		Deze houdt het level bij en tekent elk frame het level opnieuw.
	"""
	
	def __init__(self, game):
		self.game = game
		
		# Maak font aan voor tekenen van de FPS.
		self.font = pygame.font.Font(None, 20)
		
		# View rect.
		self.view = self.game.getScreen().get_rect()
	
	def update(self):
		"""Update de positie van de view.
		"""
		playerRect = self.game.getCurrentLevel().getPlayer().rect
		self.view.center = playerRect.center
		
	def draw(self):
		"""Teken het level opnieuw.
		"""
		screen = self.game.getScreen()
		level = self.game.getCurrentLevel()
		
		# Maak het scherm zwart.
		screen.fill((0, 0, 0))
		
		# Als de player dood is tekenen we alleen game over.
		if level.getPlayer().isAlive() == False:
			text = self.font.render("Game over!", False, (255, 255, 255))
			screen.blit(text, (400, 300))
			return

		# Als het level gehaald is tekenen we alleen congratulations.
		if level.isFinished() == True:
			text = self.font.render("Congratulations! You've escaped.", False, (255, 255, 255))
			screen.blit(text, (300, 300))
			return
		
		# Lijst met alle game objects die we willen tekenen.
		gameObjectList = []
		
		# Voeg alle statische dingen toe door ze uit het cluster op te halen.
		#gameObjectList += level.cluster.getGameObjectList(level.getPlayer().getClusterCollisionRect())
		#gameObjectList += level.cluster.getGameObjectList(level.getPlayer().getRect())
		staticObjectList = level.cluster.getGameObjectList(self.view)
		staticObjectList = [k for k in staticObjectList if isinstance(k, Actor) == False]
		gameObjectList += staticObjectList
		
		# Voeg alle actors toe die in beeld zijn.
		actorList = level.getActorList()
		actorList = [k for k in actorList if self.view.colliderect(k.rect) == True]
		gameObjectList += actorList
		
		# Voeg de player toe.
		gameObjectList.append(level.getPlayer())
		
		# Ga de game objects bij langs.
		for gameObject in gameObjectList:
			
			# Bepaal de relatieve positie van het game object.
			relativeRect = gameObject.rect.move((-self.view.left, -self.view.top))
			
			# Teken het game object.
			screen.blit(gameObject.image, relativeRect)

		# Teken de fps.
		text = self.font.render("%0.4f" % self.game.getClock().get_fps(), False, (255, 255, 255))
		screen.blit(text, (0, 0))

		# Teken de health.
		text = self.font.render("%0.1f" % level.getPlayer().getHealth(), False, (255, 255, 255))
		screen.blit(text, (100, 0))

		# Teken de score.
		text = self.font.render("%i" % level.getPlayer().getScore(), False, (255, 255, 255))
		screen.blit(text, (600, 0))
		
	def getView(self):
		"""Return de rect van de huidige view.
		"""
		return self.view




