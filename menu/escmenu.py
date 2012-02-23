import sys

from menu import Menu
from choicelist import ChoiceList

import gamemenu
import mainmenu


class ESCMenu(Menu):
	"""Menu voor als je op ESC drukt tijdens het spelen.
	"""
	
	def __init__(self, gui):
		Menu.__init__(self, gui)

		# Lijst met keuzes.
		self.choices = []
		self.choices.append("Back")
		self.choices.append("Options")
		self.choices.append("Main Menu")
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
		# Terug naar het spel.
		if self.choices[index] == "Back":
			self.gui.setCurrentMenu(gamemenu.GameMenu(self.gui))

		# Main menu.
		elif self.choices[index] == "Main Menu":
			self.gui.setCurrentMenu(mainmenu.MainMenu(self.gui))

		# Afsluiten.
		elif self.choices[index] == "Quit":
			sys.exit(0)


