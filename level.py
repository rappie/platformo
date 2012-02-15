import pygame

import settings

import levelgenerator

from cluster import Cluster
from gameobjects.brick import Brick
from gameobjects.coin import Coin


class Level(object):
	"""Object voor een level.
		
		Hierin staat opgeslagen waar alle bricks zitten.
	
	"""
	
	def __init__(self):
		
		# Player object.
		self.player = None
		
		# Lijst met alle game objects.
		self.gameObjectList = []
		
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

				# Voeg een brick toe.
				if tile == 1:
					brick = Brick((posX, posY))
					self.gameObjectList.append(brick)

				# Voeg een coin toe.
				if tile == 2:
					coin = Coin((posX, posY))
					self.gameObjectList.append(coin)

		# Maak cluster aan.
		self.cluster = Cluster(self, None, self.getRect())
					
	def getGameObjectList(self):
		"""Return lijst met alle game objects.
		"""
		return self.gameObjectList
	
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
		