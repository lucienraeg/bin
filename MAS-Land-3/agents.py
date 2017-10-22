class Agent:

	def __init__(self, index, x, y):
		self.index = index
		self.x, self.y = x, y

	def __repr__(self):
		return "Agent({}, {}, {})".format(self.index, self.x, self.y)