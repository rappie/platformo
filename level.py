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
		
		
		# Bepaal de rect van het gehele level.
		self.rect = pygame.Rect(0, 0, settings.TILE_WIDTH*settings.LEVEL_WIDTH, settings.TILE_HEIGHT*settings.LEVEL_HEIGHT)
		
		
		# Bepaal de lijst met alle game objects van dit level.
		#
		# Dit doen we door eerst een levelmap te genereren met een level-
		# generator. Vervolgens lopen we de level map door en maken we alle game
		# objects aan.
		#
		levelMap = levelgenerator.generateLevelMap()
		gameObjectList = self.getGameObjectListFromLevelMap(levelMap)
		
		# Maak cluster aan waar alle game objects in worden opgeslagen.
		staticObjectList = [k for k in gameObjectList if isinstance(k, Actor) == False]
		self.cluster = Cluster(self, staticObjectList, self.rect)

		# Maak lijst aan met alle actors.
		self.actorList = [k for k in gameObjectList if isinstance(k, Actor) == True]

	def getGameObjectListFromLevelMap(self, levelMap):
		"""Return lijst met alle game objects beschreven in 'levelMap'.
		"""
		# De lijst met game objects die we gaan returnen.
		gameObjectList = []
		
		# Loop door alle tiles heen.
		for y in xrange(len(levelMap)):
			for x in xrange(len(levelMap[0])):
				
				# Bepaal de x/y positie.
				posX = x * settings.TILE_WIDTH
				posY = y * settings.TILE_HEIGHT

				# Haal tile op.
				tile = levelMap[y][x]
				
				# Loop door alle game object id's in de tile heen.
				for gameObjectId in tile:
					
					# Bepaal de class van het game object.
					gameObjectClass = ID_TO_OBJECT_CLASS[gameObjectId]
					
					# Maak aan en zet in de lijst.
					gameObjectRect = pygame.Rect(posX, posY, settings.TILE_WIDTH, settings.TILE_HEIGHT)
					gameObject = gameObjectClass(self, gameObjectRect)
					gameObjectList.append(gameObject)
		
		# Return de game objects.
		return gameObjectList
					
	def removeGameObject(self, gameObject):
		"""Verwijder een game object uit het level.
		"""
		self.cluster.removeGameObject(gameObject)
		
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

		