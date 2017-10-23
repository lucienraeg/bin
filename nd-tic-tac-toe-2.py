import numpy as np
import pygame

class Cell:

	def __init__(self, *coords):
		self.coords = coords
		self.state = ""
		self.win = False

	def __repr__(self):
		return "Cell{} {} {}".format(self.coords, self.state, self.win)

class Game:

	def __init__(self):
		pygame.init()

		# fonts
		self.FNT_SMALL = pygame.font.SysFont("arial", 11)
		self.FNT_MEDIUM = pygame.font.SysFont("arial", 15)
		self.FNT_LARGE = pygame.font.SysFont("arial", 22)

		# colors
		self.C_WHITE = (255, 255, 255)
		self.C_GRAY = (150, 150, 150)
		self.C_LTGRAY = (200, 200, 200)
		self.C_BLACK = (0, 0, 0)
		self.C_RED = (255, 100, 100)
		self.C_LIME = (100, 200, 100)

		# misc
		self.focus = Cell(-1, -1, -1, -1)
		self.turn = "X"
		self.cooldown = 0
		self.turns = 0
		self.score = {"X": 0, "O": 0}
		self.display = pygame.display.set_mode((1280, 960))

	def main(self):
		self.display.fill(self.C_WHITE)
		self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

		self.display_hud()
		self.display_board(board, board_shape, (12, 48), 64)

		if self.cooldown > 0:
			self.cooldown -= 1/60

		pygame.display.update()

	def display_hud(self):
		text = self.FNT_LARGE.render("Coords: {}, Turn: {}, Score: {} : {}".format(self.focus.coords, self.turn, self.score["X"], self.score["O"]), True, self.C_BLACK)
		self.display.blit(text, (12, 12))

	def display_board(self, b, bsh, coords, c_size):
		x_offset, y_offset = coords[0], coords[1]

		if c_size > 40: font = self.FNT_LARGE
		elif c_size > 25: font = self.FNT_MEDIUM
		else: font = self.FNT_SMALL

		for d3 in range(bsh[3]):
			for d2 in range(bsh[2]):
				for d1 in range(bsh[1]):
					for d0 in range(bsh[0]):
						c = b[d0, d1, d2, d3]
						xx, yy = x_offset+(d2*(c_size*bsh[0]+6))+(d0*c_size), y_offset+(d3*(c_size*bsh[1]+6))+(d1*c_size)

						hover = xx < self.mouse_x < xx+c_size and yy < self.mouse_y < yy+c_size
						lclick = pygame.mouse.get_pressed()[0]
						rclick = pygame.mouse.get_pressed()[2]
						can_place = c.state == ""

						col = self.C_LTGRAY

						if hover:
							self.focus = c
							col = self.C_GRAY

							if lclick and self.cooldown <= 0 and can_place:
								c.state = self.turn

								if self.turn == "X": self.turn = "O"
								else: self.turn = "X"

								self.turns += 1

								print("{}. {} {}".format(self.turns, c.state, c.coords))

								winning_place = self.check_for_row(c)

								self.cooldown = 1.5

						if c.win: col = self.C_LIME
						pygame.draw.rect(self.display, col, (xx, yy, c_size-2, c_size-2))

						if not c.state == "":
							text = font.render("{}".format(c.state), True, self.C_BLACK)
							text_rect = text.get_rect(center=(xx+(c_size-2)/2, yy+(c_size-2)/2))
							self.display.blit(text, text_rect)
						else:
							# adjacency test
							sc = c.coords
							fc = self.focus.coords
							adj_score = int(fc[0]==sc[0]) + int(fc[1]==sc[1]) + int(fc[2]==sc[2]) + int(fc[3]==sc[3])

							if adj_score > 1:
								col_val = 200-((adj_score-1)*20)
								col = (col_val, col_val, col_val)
								size = adj_score
								pygame.draw.rect(self.display, col, (xx+(c_size-2)/2-size, yy+(c_size-2)/2-size, size*2, size*2))

	def check_for_row(self, c):
		# base 2 (-1), 4 digits, all except (0, 0, 0, 0)
		shift_list = [(-1, -1, -1, -1), (0, -1, -1, -1), (1, -1, -1, -1), (-1, 0, -1, -1), (0, 0, -1, -1), (1, 0, -1, -1), (-1, 1, -1, -1), 
		(0, 1, -1, -1), (1, 1, -1, -1), (-1, -1, 0, -1), (0, -1, 0, -1), (1, -1, 0, -1), (-1, 0, 0, -1), (0, 0, 0, -1), (1, 0, 0, -1), 
		(-1, 1, 0, -1), (0, 1, 0, -1), (1, 1, 0, -1), (-1, -1, 1, -1), (0, -1, 1, -1), (1, -1, 1, -1), (-1, 0, 1, -1), (0, 0, 1, -1), 
		(1, 0, 1, -1), (-1, 1, 1, -1), (0, 1, 1, -1), (1, 1, 1, -1), (-1, -1, -1, 0), (0, -1, -1, 0), (1, -1, -1, 0), (-1, 0, -1, 0), 
		(0, 0, -1, 0), (1, 0, -1, 0), (-1, 1, -1, 0), (0, 1, -1, 0), (1, 1, -1, 0), (-1, -1, 0, 0), (0, -1, 0, 0), (1, -1, 0, 0), 
		(-1, 0, 0, 0), (1, 0, 0, 0), (-1, 1, 0, 0), (0, 1, 0, 0), (1, 1, 0, 0), (-1, -1, 1, 0), (0, -1, 1, 0), (1, -1, 1, 0), (-1, 0, 1, 0), 
		(0, 0, 1, 0), (1, 0, 1, 0), (-1, 1, 1, 0), (0, 1, 1, 0), (1, 1, 1, 0), (-1, -1, -1, 1), (0, -1, -1, 1), (1, -1, -1, 1), (-1, 0, -1, 1), 
		(0, 0, -1, 1), (1, 0, -1, 1), (-1, 1, -1, 1), (0, 1, -1, 1), (1, 1, -1, 1), (-1, -1, 0, 1), (0, -1, 0, 1), (1, -1, 0, 1), (-1, 0, 0, 1), 
		(0, 0, 0, 1), (1, 0, 0, 1), (-1, 1, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (-1, -1, 1, 1), (0, -1, 1, 1), (1, -1, 1, 1), (-1, 0, 1, 1), 
		(0, 0, 1, 1), (1, 0, 1, 1), (-1, 1, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1)]

		for shift in shift_list:
			if self.check_shift(c, shift):
				winner = ("X", "O")[self.turn == "X"]
				print("{} got a row! (shift: {})".format(winner, shift))
				self.score[winner] += 1
				return

	def check_shift(self, c, shift):
		winning = False

		coords = c.coords

		c_list = []
		for i in range(row_goal):
			d0 = coords[0]+i*shift[0]
			d1 = coords[1]+i*shift[1]
			d2 = coords[2]+i*shift[2]
			d3 = coords[3]+i*shift[3]

			try:
				c_list.append(board[d0, d1, d2, d3])
			except IndexError:
				pass

		c_list_states = [cell.state for cell in c_list]

		if c_list_states == ['X']*row_goal or c_list_states == ['O']*row_goal:
			winning = True
			for cell in c_list:
				cell.win = True

		return winning

if __name__ == "__main__":

	# init board
	row_goal = 3
	board_shape = (3, 3, 3, 3)

	board = np.array([[[[None]*board_shape[3]]*board_shape[2]]*board_shape[1]]*board_shape[0])

	for d3 in range(board_shape[3]):
		for d2 in range(board_shape[2]):
			for d1 in range(board_shape[1]):
				for d0 in range(board_shape[0]):
					board[d0, d1, d2, d3] = Cell(d0, d1, d2, d3)

	# init game
	game = Game()

	running = True

	while running:
		game.main()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

	pygame.quit()
	quit()