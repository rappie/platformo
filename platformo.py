import pygame
pygame.mixer.init(44100, -16, 2, 512)
pygame.init()


from game import Game


if __name__ == "__main__":
	
	game = Game()
	game.run()
	
	