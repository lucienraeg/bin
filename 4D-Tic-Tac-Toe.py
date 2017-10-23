import numpy as np

class Board:

	def __init__(self, shape=(3, 3, 3)):
		self.shape = shape
		array_default = [[[0]*shape[0]]*shape[1]]*shape[2]
		self.grid = np.array(array_default)

	def display(self):
		for x in range(self.shape[0]):
			for y in range(self.shape[0]):
				print(self.grid[x, y])



board = Board()

board.display()