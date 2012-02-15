import pygame

import settings


class Node(object):
	"""Een node binnen een cluster.
		Dit is de superklasse van alle cluster klasses.
	"""

	def __init__(self, level, parent, rect, depth=1):
		"""Maak een nieuwe Node.
		
			level:
				Verwijzing naar het level object.
			
			parent:
				Verwijzing naar de parent Node. Mag None zijn.
			
			rect:
				De rect van deze node.
				
			depth:
				Wordt (intern) gebruikt om bij te houden hoe diep je in de
				cluster tree zit.
				
		"""
		self.level = level
		self.parent = parent
		self.rect = rect
		self.depth = depth

	def getGameObjectList(self, collidingRect):
		"""Return lijst met game objects.
			Deze methode returned een lijst met alle game objects van de
			blocks die colliden met 'collidingRect'.
		"""
		raise Exception, "Overwrite me!"


class Block(Node):
	"""Een cluster block.
	
		Dit is de onderste 'laag' in een cluster van clusters. De Blocks
		bevatten de daadwerkelijke lijst met game objects.
	"""
	
	def __init__(self, level, parent, rect, depth):
		Node.__init__(self, level, parent, rect, depth)
		
		# Lijst met alle game objects van dit block.
		self.gameObjectList = []
		
		# Vul de lijst met game objects.
		for gameObject in self.parent.getContainedGameObjects():
			if gameObject.rect.colliderect(self.rect) == True:
				self.gameObjectList.append(gameObject)
				
	def getGameObjectList(self, collidingRect):
		"""Return de lijst met game objects.
		"""
		return self.gameObjectList


class Cluster(Node):
	"""Een cluster.
	
		Elk cluster is opgedeeld in 4 nodes. Een node kan een Cluster of een
		Block zijn. De onderste laag in de tree van (sub)clusters is altijd
		een Block. De grootte van de blocks wordt bepaald door 'BLOCK_SIZE'.
	
	"""
	
	def __init__(self, level, parent, rect, depth=1):
		Node.__init__(self, level, parent, rect, depth)

		# Lijst met de nodes.
		self.nodes = [[None, None], [None, None]]

		# Bepaal de object lijst van de parent.
		#
		# Als de parent None is, worden alle game objects uit het level
		# gebruikt.
		#
		if self.parent == None:
			parentGameObjectList = self.level.getGameObjectList()
		else:
			parentGameObjectList = self.parent.getContainedGameObjects()

		# Lijst met objecten die binnen dit cluster vallen.
		self.containedGameObjects = []
		for gameObject in parentGameObjectList:
			if self.rect.colliderect(gameObject) == True:
				self.containedGameObjects.append(gameObject)
			
		# Vul de nodes.	
		self.fillNodes()
		
	def fillNodes(self):
		"""Vul de nodes van dit cluster.
		
			Er wordt mbv. BLOCK_SIZE bepaald of de volgende laag Blocks of
			Clusters moeten worden.
		"""
		
		# Bepaal of de volgende laag Blocks of Clusters moeten worden.
		blockSize = self.rect.width/settings.TILE_WIDTH/2
		if blockSize == settings.BLOCK_SIZE:
			blockClass = Block
		else:
			blockClass = Cluster

		# De grootte van de nodes.
		width = self.rect.width/2
		height = self.rect.height/2
		
		# Vul linksboven.
		x = self.rect.left + 0
		y = self.rect.top + 0
		rect = pygame.Rect(x, y, width, height)
		self.nodes[0][0] = blockClass(self.level, self, rect, self.depth+1)
		
		# Vul Rechtsboven.
		x = self.rect.left + (self.rect.width/2)
		y = self.rect.top + 0
		rect = pygame.Rect(x, y, width, height)
		self.nodes[1][0] = blockClass(self.level, self, rect, self.depth+1)

		# Vul Linksonder.
		x = self.rect.left + 0
		y = self.rect.top + (self.rect.height/2)
		rect = pygame.Rect(x, y, width, height)
		self.nodes[0][1] = blockClass(self.level, self, rect, self.depth+1)

		# Vul rechtsonder.
		x = self.rect.left + (self.rect.width/2)
		y = self.rect.top + (self.rect.height/2)
		rect = pygame.Rect(x, y, width, height)
		self.nodes[1][1] = blockClass(self.level, self, rect, self.depth+1)
		
	def getGameObjectList(self, collidingRect):
		"""Return de lijst met game objects.
			Deze methode returned alle game objects die in Blocks zitten die
			colliden met 'collidingRect'.
		"""
		# Lijst met game objects.
		gameObjectList = []
		
		# Loop door de nodes heen.
		for x in xrange(2):
			for y in xrange(2):
				node = self.nodes[y][x]
				
				# Voeg game objects toe aan de lijst als de node collide met
				# 'collidingRect'.
				#
				if node.rect.colliderect(collidingRect) == True:
					gameObjectList += node.getGameObjectList(collidingRect)

		# Return lijst met game objects.
		return gameObjectList

	def getContainedGameObjects(self):
		"""Return lijst met objecten die binnen de rect van deze node vallen.
		"""
		return self.containedGameObjects


	
		
