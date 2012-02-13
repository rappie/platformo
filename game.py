import sys
import pygame

import settings

import inputstate
inputState = inputstate.getInstance()

from gameobjects.player import Player
from level import Level
from drawer import Drawer


class Game(object):
	"""De main klasse van het spel.
		Hier worden alle basis dingen zoals het level en de player en de drawer
		in bijgehouden. Met 'run()' kan je de main loop starten.
	"""
	
	def __init__(self):

		# Maak level en player objecten aan.
		self.level = Level()
		self.player = Player(self.level)
		self.level.setPlayer(self.player)

		# Maak het scherm aan.
		if "-windowed" in sys.argv:
			flags = 0
		else:
			flags = pygame.FULLSCREEN
		self.screen = pygame.display.set_mode((800, 600), flags)
	
		# Maak Clock object aan.
		self.clock = pygame.time.Clock()
	
		# Maak drawer object aan.
		self.drawer = Drawer(self)

	
	def run(self):
		"""Start de main loop van het spel.
		"""
		
		# Start de main loop.
		while True:
			
			# Update de input state.
			#
			# Dit checkt of er keys zijn ingedrukt of losgelaten.
			#
			inputState.update()
			
			# Update de positie van de player.
			self.player.update()
			
			# Update de drawer omdat de positie van de player veranderd kan zijn.
			self.drawer.update()
					
			# Teken het level opnieuw.
			self.drawer.draw()
			
			# Wissel de buffers.
			pygame.display.flip()
			
			# Time delay.
			self.clock.tick(settings.MAX_FPS)
			
	def getScreen(self):
		"""Return het screen object.
		"""
		return self.screen
	
	def getCurrentLevel(self):
		"""Return het huidige level.
		"""
		return self.level
	
	def getClock(self):
		"""Return de clock.
		"""
		return self.clock
			
