import os
import pygame


class Drawer(object):
	"""Drawer klasse.
	
		Deze houdt het level bij en tekent elke turn het level opnieuw.
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
		
		# Ga alle bricks bij langs.
		#for gameObject in level.cluster.getGameObjectList(level.getPlayer().getClusterCollisionRect()):
		#for gameObject in level.cluster.getGameObjectList(level.getPlayer().getRect()):
		for gameObject in level.cluster.getGameObjectList(self.view):
			
			# Bepaal de relatieve positie van het game object.
			relativeRect = gameObject.rect.move((-self.view.left, -self.view.top))
			
			# Teken het game object.
			screen.blit(gameObject.image, relativeRect)

		# Teken de player.
		player = level.getPlayer()
		relativePlayerRect = player.rect.move((-self.view.left, -self.view.top))
		screen.blit(player.image, relativePlayerRect)

		# Teken de fps.
		text = self.font.render("%0.4f" % self.game.getClock().get_fps(), False, (255, 255, 255))
		screen.blit(text, text.get_rect())




