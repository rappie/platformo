import pygame


class GameObject(pygame.sprite.Sprite):
	"""Een object in een level.
	
		Dit is de superklasse van alle objecten in level.
		
	"""
	
	def __init__(self, level):
		pygame.sprite.Sprite.__init__(self)
		
		self.level = level
		self.rect = None
		self.image = None
		
	def update(self):
		"""Update het game object.
		"""
		pass

	def collideVertical(self, gameObject):
		"""Voer verticale collision detection uit.
		"""
		pass

	def collideHorizontal(self, gameObject):
		"""Voer horizontale collision detection uit.
		"""
		pass
	
	def remove(self):
		"""Verwijder dit game object uit het level.
		"""
		self.getLevel().removeGameObject(self)
	
	def getLevel(self):
		"""Return level van dit game object.
		"""
		return self.level
	
	def setLevel(self, level):
		"""Set level van dit game object.
		"""
		self.level = level


