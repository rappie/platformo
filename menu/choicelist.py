import os

import pygame

import settings


class ChoiceList(object):
	"""Lijst met keuzes om uit te kiezen.
		
		Dit is de text die onder elkaar staat in de meeste menu's (zoals het
		main menu) en waar je dan een keuze kan maken.
	
	"""
	
	def __init__(self, screen, choices, position, selectionHook, defaultIndex=0, font=None):
		"""Maak een choice list aan.
		
			screen:
				Verwijzing naar het screen object waarop de choice list getekend
				moet worden.
				
			choices:
				Lijst met strings. De keuzes die de gebruiker kan maken.
				
			position:
				Positie waar de choice list moet komen.
			
			selectionHook:
				Deze functie wordt aangeroepen zodra er een keuze is gemaakt.
			
			defaultIndex:
				De default keuze die geselecteerd moet staan.
				
			font:
				Het font van de text.
		
		"""
		self.screen = screen
		self.choices = choices
		self.position = position
		self.selectionHook = selectionHook
		self.selectedIndex = defaultIndex

		# Maak zelf een font aan als er geen is mee gegeven.
		if font != None:
			self.font = font
		else:
			self.font = pygame.font.Font(os.path.join(".", "data", "fonts", settings.MENU_FONTNAME), 30)
			
	def handleInput(self, events):
		"""Handle input af.
			Dit wordt gebruikt voor het naar boven en beneden bewegen binnen
			de keuzes.
		"""
		for event in events:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.changeSelection(-1)
				if event.key == pygame.K_DOWN:
					self.changeSelection(1)
				if event.key == pygame.K_RETURN:
					self.select()

	def draw(self):
		"""Teken de choice list.
		"""
		# Loop door alle choices heen.
		for index, choice in enumerate(self.choices):
			
			# Bepaal de kleur van de text.
			if index == self.selectedIndex:
				color = settings.MENU_COLOR_SELECTED
			else:
				color = settings.MENU_COLOR_NORMAL
				
			# Render de text.
			text = self.font.render(choice, True, color)
			
			# Teken de text.
			posX = self.position[0]
			posY = self.position[1] + (50 * index)
			self.screen.blit(text, (posX, posY))

	def changeSelection(self, direction):
		"""Verander de selectie.
			Deze methode verandert de selectie aan de hand van 'direction'. Er
			wordt rekening gehouden met wanneer je out of bounds zou moven.
		"""
		# Verander selectie.
		self.selectedIndex += direction
		
		# Check op bounds.
		if self.selectedIndex < 0:
			self.selectedIndex = len(self.choices) - 1
		elif self.selectedIndex >= len(self.choices):
			self.selectedIndex = 0

	def select(self):
		"""Selecteer het gekozen item.
			Roep de listener aan.
		"""
		self.selectionHook(self.selectedIndex)

	def getSelection(self):
		"""Return de geselecteerde index.
		"""
		return self.selectedIndex
	
	def getStringSelection(self):
		"""Return de string van de geselecteerde index.
		"""
		return self.choices[self.selectedIndex]
	

