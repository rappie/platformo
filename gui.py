import sys
import pygame

import settings

from menu.mainmenu import MainMenu


class GUI(object):
	"""De hoofd container voor alle GUI.
	
		Deze klasse toont altijd 1 huidig menu. Dit is bijvoorbeeld het main
		menu of het menu waar de game in zit.
	"""
	
	def __init__(self):

		# Maak het scherm aan.
		if "-windowed" in sys.argv:
			flags = 0
		else:
			flags = pygame.FULLSCREEN
		self.screen = pygame.display.set_mode((800, 600), flags)

		# Maak clock aan.
		self.clock = pygame.time.Clock()

		# Variabele voor het huidige menu.
		self.currentMenu = MainMenu(self)
	
	def run(self):
		"""Run commando voor het starten van de main loop.
		"""
		
		# Start de main loop.
		while True:
			
			# Haal de events op.
			events = pygame.event.get()

			# Keybinding voor Q om er snel uit te gaan.
			for event in events:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						sys.exit()
	
			# Update het current menu.
			self.getCurrentMenu().handleInput(events)
			self.getCurrentMenu().update()
			self.getCurrentMenu().draw()
	
			# Update de display.
			pygame.display.flip()

			# Update de clock voor de juiste FPS.
			self.clock.tick(settings.MAX_FPS)

	def setCurrentMenu(self, menu):
		"""Set het huidige menu.
		"""
		self.currentMenu = menu
		
	def getCurrentMenu(self):
		"""Haal het huidige menu op.
		"""
		return self.currentMenu

	def getScreen(self):
		"""Haal screen op.
		"""
		return self.screen
	
	def getClock(self):
		"""Haal clock op.
		"""
		return self.clock

	

