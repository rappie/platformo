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
		
		# Lees de images in.
		self.playerImage = pygame.image.load(os.path.join(".", "data", "tiles", "player.png"))#.convert()
		self.brickImage = pygame.image.load(os.path.join(".", "data", "tiles", "brick.png"))#.convert()
		
		# View rect.
		self.view = self.game.getScreen().get_rect()
	
	def update(self):
		"""Update de positie van de view.
		"""
		playerRect = self.game.getCurrentLevel().getPlayer().getRect()
		self.view.center = playerRect.center
		
	def draw(self):
		"""Teken het level opnieuw.
		"""
		screen = self.game.getScreen()
		level = self.game.getCurrentLevel()
		
		# Maak het scherm zwart.
		screen.fill((0, 0, 0))
		
		# Ga alle bricks bij langs.
		#for brick in level.cluster.getGameObjectList(level.getPlayer().getClusterCollisionRect()):
		#for brick in level.cluster.getGameObjectList(level.getPlayer().getRect()):
		for brick in level.cluster.getGameObjectList(self.view):
			
			# Teken hem als hij in beeld is.
			if self.view.colliderect(brick) == True:
				relativeBrickRect = brick.rect.move((-self.view.left, -self.view.top))
				screen.blit(self.brickImage, relativeBrickRect)

		# Teken de player.
		playerRect = level.getPlayer().getRect()
		relativePlayerRect = playerRect.move((-self.view.left, -self.view.top))
		screen.blit(self.playerImage, relativePlayerRect)

		# Teken de fps.
		text = self.font.render("%0.4f" % self.game.getClock().get_fps(), False, (255, 255, 255))
		screen.blit(text, text.get_rect())




