import numpy as np
import pygame

class Board:

	def __init__(self):
		self.shape = (3, 3, 3, 3, 1, 1)
		self.active_dimensions = 4 # max 6

		self.cells = np.array([[[[[[""]*self.shape[5]]*self.shape[4]]*self.shape[3]]*self.shape[2]]*self.shape[1]]*self.shape[0])

		self.win_cells = []

	def check_for_row(self, coords):
		tile = "X"

		in_row = True
		c_list = []
		if coords[5] == 0:
			for i in range(coords[5], coords[5]+3):
				if not self.cells[i, coords[4], coords[3], coords[2], coords[1], coords[0]] == tile: in_row = False
				else: c_list.append([i, coords[4], coords[3], coords[2], coords[1], coords[0]])
		else:
			if coords[4] == 0:
				for i in range(coords[4], coords[4]+3):
					if not self.cells[coords[5], i, coords[3], coords[2], coords[1], coords[0]] == tile: in_row = False
					else: c_list.append([coords[5], i, coords[3], coords[2], coords[1], coords[0]])
			else:
				if coords[3] == 0:
					for i in range(coords[3], coords[3]+3):
						if not self.cells[coords[5], coords[4], i, coords[2], coords[1], coords[0]] == tile: in_row = False
						else: c_list.append([coords[5], coords[4], i, coords[2], coords[1], coords[0]])
				else:
					in_row = False>	

		if in_row:
			self.win_cells = c_list

		return in_row


class Game:

	def __init__(self):
		pygame.init()

		# fonts
		self.FNT_SMALL = pygame.font.SysFont("arial", 11)

		# colors
		self.C_WHITE = (255, 255, 255)
		self.C_BLACK = (0, 0, 0)
		self.C_BEIGE1 = (255, 222, 191)
		self.C_BEIGE2 = (234, 188, 145)
		self.C_BEIGE3 = (209, 139, 71)
		self.C_BROWN = (81, 64, 51)
		self.C_RED = (255, 50, 50)

		# misc
		self.focus_cell = (0, 0, 0, 0, 0, 0)

		# image
		self.nought_img = pygame.image.load('nought.png')
		self.cross_img = pygame.image.load('cross.png')

		self.display = pygame.display.set_mode((736, 756))

	def main(self):
		self.display.fill(self.C_WHITE)

		self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

		# display loop
		if True:
			self.display_hud(0, 0)
			self.display_board(Board)

		pygame.display.update()

	def display_hud(self, x1, y1):
		text = self.FNT_SMALL.render("{}".format(self.focus_cell[6-Board.active_dimensions:]), True, self.C_BLACK)
		self.display.blit(text, (x1+4, y1+4))

	def display_board(self, board):
		for d1 in range(Board.shape[5]):
			for d2 in range(Board.shape[4]):
				for d3 in range(Board.shape[3]):
					for d4 in range(Board.shape[2]):
						for d5 in range(Board.shape[1]):
							for d6 in range(Board.shape[0]):
								self.display_cell((d1, d2, d3, d4, d5, d6))

	def display_cell(self, coords):
		cell = Board.cells[coords[5], coords[4], coords[3], coords[2], coords[1], coords[0]]
		x, y = 16+(240*coords[1])+(76*coords[3])+(coords[5]*24), 36+(240*coords[0])+(76*coords[2])+(coords[4]*24)

		adjacency_score = int(self.focus_cell[0] == coords[0]) \
		+ int(self.focus_cell[1] == coords[1]) \
		+ int(self.focus_cell[2] == coords[2]) \
		+ int(self.focus_cell[3] == coords[3]) \
		+ int(self.focus_cell[4] == coords[4]) \
		+ int(self.focus_cell[5] == coords[5])

		if x < self.mouse_x < x+24 and y < self.mouse_y < y+24: # focus
			self.focus_cell = coords

			# debug placing
			if pygame.mouse.get_pressed()[0]:
				Board.cells[coords[5], coords[4], coords[3], coords[2], coords[1], coords[0]] = "X"
			elif pygame.mouse.get_pressed()[2]:
				Board.cells[coords[5], coords[4], coords[3], coords[2], coords[1], coords[0]] = "O"

			outline = cell == ""
			col = self.C_BEIGE1
		elif adjacency_score >= 5: # adjacent
			outline = False
			col = self.C_BEIGE1
		else: # default
			outline = False
			col = self.C_BEIGE2

		# display cell
		pygame.draw.rect(self.display, col, (x, y, 22, 22))
		if outline: pygame.draw.rect(self.display, self.C_BROWN, (x, y, 22, 22), 2)
		if Board.check_for_row(coords) or [coords[5], coords[4], coords[3], coords[2], coords[1], coords[0]] in Board.win_cells: pygame.draw.rect(self.display, self.C_RED, (x, y, 22, 22), 2)

		# debug cell text
		text = self.FNT_SMALL.render("{}".format(adjacency_score), True, self.C_BLACK)
		self.display.blit(text, (x+3, y+1))

		# display tile
		if cell == "X":
			self.display.blit(self.cross_img, (x, y))
		elif cell == "O":
			self.display.blit(self.nought_img, (x, y))



if __name__ == "__main__":
	Game = Game()
	Board = Board()

	running = True

	while running:
		Game.main()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

	pygame.quit()
	quit()