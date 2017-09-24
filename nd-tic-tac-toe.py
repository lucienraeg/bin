import numpy as np
import pygame

class Board:

	def __init__(self):
		pass


class Game:

	def __init__(self):
		pygame.init()

		self.FNT_SMALL = pygame.font.SysFont("arial", 11)

		self.display = pygame.display.set_mode((400, 400))

	def main(self):
		self.display.fill((255, 255, 255))

		self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

		# display loop
		if True:
			self.display_hud()
			self.display_board()

		pygame.display.update()

	def display_hud(self):
		text = self.FNT_SMALL.render("{}, {}".format(self.mouse_x, self.mouse_y), True, (0, 0, 0))
		self.display.blit(text, (4, 4))

	def display_board(self):
		pass


if __name__ == "__main__":
	game = Game()
	board = Board()

	running = True

	while running:
		game.main()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

	pygame.quit()
	quit()