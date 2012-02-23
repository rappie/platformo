import sys

from menu import Menu
from choicelist import ChoiceList

import mainmenu


class LoadMenu(Menu):
	"""Menu om een game te loaden.
	"""
	
	def __init__(self, gui):
		Menu.__init__(self, gui)

		# Lijst met keuzes.
		self.choices = []
		self.choices.append("Game #01")
		self.choices.append("Game #02")
		self.choices.append("Game #03")
		self.choices.append("Back")
		
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
		# Terug naar main menu.
		if self.choices[index] == "Back":
			self.gui.setCurrentMenu(mainmenu.MainMenu(self.gui))
		

