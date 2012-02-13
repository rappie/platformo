import pygame


class GameObject(pygame.sprite.Sprite):
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.rect = None
		self.image = None
		
		
	def update(self):
		pass



