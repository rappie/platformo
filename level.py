import pygame

import settings

import levelgenerator

from cluster import Cluster
from gameobjects.actor import Actor
from gameobjects.brick import Brick
from gameobjects.coin import Coin
from gameobjects.monster import Monster


# Map van levelmap-id naar klasse voor game object.
ID_TO_OBJECT_CLASS = {}
ID_TO_OBJECT_CLASS[levelgenerator.BRICK] = Brick
ID_TO_OBJECT_CLASS[levelgenerator.COIN] = Coin
ID_TO_OBJECT_CLASS[levelgenerator.MONSTER] = Monster


class Level(object):
	"""Object voor een level.
		
		Hierin staat opgeslagen waar alle bricks zitten.
	
	"""
	
	def __init__(self):
		
		# Player object.
		self.player = None
		
		# Lijst met alle game objects.
		self.gameObjectList = []
		
		# Lijst met alle actors.
		self.actorList = []
		
		# Maak een level aan.
		self.levelMap = levelgenerator.generateLevelMap()
		
		# Bepaal de rect van het gehele level.
		self.rect = pygame.Rect(0, 0, settings.TILE_WIDTH*settings.LEVEL_WIDTH, settings.TILE_HEIGHT*settings.LEVEL_HEIGHT)
		
		# Vul de game object list aan de hand van de level map.
		#
		# Loop door alle tiles heen.
		#
		for y in xrange(len(self.levelMap)):
			for x in xrange(len(self.levelMap[0])):
				
				# Bepaal de x/y positie.
				posX = x * settings.TILE_WIDTH
				posY = y * settings.TILE_HEIGHT

				# Haal tile op.
				tile = self.levelMap[y][x]
				
				# Loop door alle game object id's in de tile heen.
				for gameObjectId in tile:
					
					# Bepaal de class van het game object.
					gameObjectClass = ID_TO_OBJECT_CLASS[gameObjectId]
					
					# Maak aan en zet in de lijst.
					gameObjectRect = pygame.Rect(posX, posY, settings.TILE_WIDTH, settings.TILE_HEIGHT)
					gameObject = gameObjectClass(self, gameObjectRect)
					self.gameObjectList.append(gameObject)
					
					# Voeg toe aan actor list als het een actor is.
					if isinstance(gameObject, Actor):
						self.actorList.append(gameObject)

		# Maak cluster aan.
		self.cluster = Cluster(self, None, self.getRect())

	def removeGameObject(self, gameObject):
		"""Verwijder een game object uit het level.
		"""
		# Verwijder game object uit het cluster.
		self.cluster.removeGameObject(gameObject)
		
		# Verwijder game object uit de lijst met alle objecten.
		if gameObject in self.gameObjectList:
			self.gameObjectList.remove(gameObject)
					
	def getGameObjectList(self):
		"""Return lijst met alle game objects.
		"""
		return self.gameObjectList[:]
	
	def getActorList(self):
		"""Return lijst met alle actors.
		"""
		return self.actorList[:]

	def getPlayer(self):
		"""Return het player object.
		"""
		return self.player
	
	def setPlayer(self, player):
		"""Set het player object.
		"""
		self.player = player
	
	def getRect(self):
		"""Return de rect van het gehele level.
		"""
		return self.rect
		