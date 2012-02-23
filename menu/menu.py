

class Menu(object):
	"""Superklasse voor alle menu's.
		
		Dit is in principe een interface.
		
		Elk menu heeft een verwijziging naar de GUI. De GUI update elk frame
		het huidige menu. Dit gaat in de volgende stappen:
		
		  1) Input afhandelen met 'handleInput()'
		  2) Game-logic etc. afhandelen met 'update()'
		  3) Opnieuw tekenen met 'draw()'
		  
		Elk menu moet de draw() methode implementeren om uberhaubt iets te
		kunnen tekenen.
	
	"""
	
	def __init__(self, gui):
		self.gui = gui

	def handleInput(self, events):
		"""Handle input af.
		"""
		pass
	
	def update(self):
		"""Update de status oid.
		"""
		pass

	def draw(self):
		"""Tekenen.
		"""
		pass

