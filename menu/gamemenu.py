import pygame

from menu import Menu

import mainmenu
import escmenu

from game import Game


class GameMenu(Menu):
	"""Menu voor het spel.
	
		Dit is in principe een hele simpele container voor het Game object waar
		het spel zich in afspeelt.
	"""
	
	def __init__(self, gui):
		Menu.__init__(self, gui)
		
		# Maak game object aan.
		self.game = Game(self.gui.getScreen(), self.gui)

	def handleInput(self, events):
		"""Input afhandelen.
		"""
		
		# ESC voor het escape/pauze menu.
		for event in events:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.gui.setCurrentMenu(escmenu.ESCMenu(self.gui))
		
		# Stuur events door naar game.
		self.game.handleInput(events)
	
	def update(self):
		"""Updaten.
		"""
		self.game.update()
			
	def draw(self):
		"""Tekenen.
		"""
		self.game.draw()


