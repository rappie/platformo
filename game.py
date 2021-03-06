import sys
import pygame

import settings

import inputstate
inputState = inputstate.getInstance()

from gameobjects.player import Player
from level import Level
from camera import Camera


class Game(object):
	"""De main klasse van het spel.
		Hier worden alle basis dingen zoals het level en de player en de camera
		in bijgehouden. Met 'run()' kan je de main loop starten.
	"""
	
	def __init__(self, screen, gui):
		self.screen = screen
		self.gui = gui

		# Maak level aan.
		self.level = Level()

		# Bepaal rect van de Player.
		initialX = 1*settings.TILE_WIDTH
		initialY = (settings.LEVEL_HEIGHT-2)*settings.TILE_HEIGHT
		playerRect = pygame.Rect(initialX, initialY, settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT)

		# Maak player aan.
		self.player = Player(self.level, playerRect)
		self.level.setPlayer(self.player)

		# Maak een camera object aan.
		self.camera = Camera(self)

	def handleInput(self, events):
		"""Input afhandelen.
			Dit sturen we allemaal rechtstreeks door naar de input state.
		"""
		inputState.handleInput(events)
		
	
	def update(self):
		"""Update het spel/level.
		"""
		
		# Update alle game objects (Actors).
		gameObjectsToUpdate = self.level.getActorList()
		gameObjectsToUpdate.append(self.player)
		for gameObject in gameObjectsToUpdate:
			gameObject.update()
		
		# Update de camera.
		self.camera.update()
	
	def draw(self):
		"""Tekenen.
		"""
		self.camera.draw()
			
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
		return self.gui.getClock()
			
