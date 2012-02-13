import pygame

import settings

import levelgenerator

from cluster import Cluster
from gameobjects.brick import Brick


class Level(object):
	"""Object voor een level.
		
		Hierin staat opgeslagen waar alle bricks zitten.
	
	"""
	
	def __init__(self):
		
		# Player object.
		self.player = None
		
		# Lijst met alle bricks.
		self.brickList = []
		
		# Maak een level aan.
		self.levelMap = levelgenerator.generateLevelMap()
		
		# Bepaal de rect van het gehele level.
		self.rect = pygame.Rect(0, 0, settings.TILE_WIDTH*settings.LEVEL_WIDTH, settings.TILE_HEIGHT*settings.LEVEL_HEIGHT)
		
		# Vul de brick list aan de hand van de level map.
		#
		# Loop door alle tiles heen.
		#
		for y in xrange(len(self.levelMap)):
			for x in xrange(len(self.levelMap[0])):
				
				# Bepaal de x/y positie.
				posX = x * settings.TILE_WIDTH
				posY = y * settings.TILE_HEIGHT
				
				# Voeg een brick toe.
				tile = self.levelMap[y][x]
				if tile == 1:
					brick = Brick((posX, posY))
					self.brickList.append(brick)

		# Maak cluster aan.
		self.cluster = Cluster(self, None, self.getRect())
					
	def getBrickList(self):
		"""Return lijst met alle bricks in het level.
		"""
		return self.brickList
	
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
		