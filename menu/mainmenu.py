import sys

from menu import Menu
from choicelist import ChoiceList

import gamemenu
import loadmenu

class MainMenu(Menu):
	"""Het hoofd menu als je het spel opstart.
	"""
	
	def __init__(self, gui):
		Menu.__init__(self, gui)

		# Lijst met keuzes.
		self.choices = []
		self.choices.append("New game")
		self.choices.append("Load game")
		self.choices.append("Options")
		self.choices.append("Quit")
		
		# Maak choice list aan.
		self.choiceList = ChoiceList(self.gui.getScreen(), self.choices, (300, 100), self.onSelection)
		
	def handleInput(self, events):
		"""Input afhandelen.
		"""
		self.choiceList.handleInput(events)

	def draw(self):
		"""Tekenen.
		"""
		screen = self.gui.getScreen()

		# Scherm zwart maken.
		screen.fill((0, 0, 0))
		
		# Choice list tekenen.
		self.choiceList.draw()
		
	def onSelection(self, index):
		"""Methode die wordt aangeroepen als er een selectie is gemaakt.
		"""
		
		# Nieuw spel starten.
		if self.choices[index] == "New game":
			self.gui.setCurrentMenu(gamemenu.GameMenu(self.gui))

		# Spel laden.
		elif self.choices[index] == "Load game":
			self.gui.setCurrentMenu(loadmenu.LoadMenu(self.gui))

		# Afsluiten.
		elif self.choices[index] == "Quit":
			sys.exit(0)


