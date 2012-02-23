import pygame
pygame.mixer.init(44100, -16, 2, 512)
pygame.init()

from gui import GUI


if __name__ == "__main__":
	gui = GUI()
	gui.run()
	