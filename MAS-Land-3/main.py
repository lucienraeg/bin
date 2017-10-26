import pygame
import random
import numpy as np
import display

random.seed(0)

def point_distance(x1, y1, x2, y2):
	return np.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)

def point_direction(x1, y1, x2, y2, offset=0):
	return (180 - offset - np.rad2deg(np.arctan2(y1 - y2, x1 - x2))) % 360

class Sensor:

	def __init__(self, parent, index, angle, length):
		self.parent = parent
		self.index = index
		self.angle = angle
		self.length = length
		self.detected = []

class Agent:

	def __init__(self, index, x, y, angle):
		self.index = index
		self.x, self.y = x, y
		self.angle = angle

		# body parts
		self.sensor_n = 5 # odd
		self.sensor_gap = 25
		self.sensor_range = 64
		self.sensors = []
		for i in range(self.sensor_n):
			new_sensor = Sensor(self, i, i*self.sensor_gap-(self.sensor_gap*(self.sensor_n-1)/2), self.sensor_range)
			self.sensors.append(new_sensor)

	def __repr__(self):
		return "Agent({}, {}, {}, {})".format(self.index, self.x, self.y, self.angle)

	def move(self):
		pass
		
	def main(self):
		nearby_agents = [a for a in agent_list if point_distance(self.x, self.y, a.x, a.y) < self.sensor_range and self != a]
		sensor_limits = (-(self.sensor_gap*(self.sensor_n-1)/2), (self.sensor_gap*(self.sensor_n-1)/2))
		detected_agents = [a for a in nearby_agents if sensor_limits[0] < int(point_direction(self.x, self.y, a.x, a.y, offset=self.angle+180)-180) < sensor_limits[1]]

		for a in detected_agents:
			a_angle = int(point_direction(self.x, self.y, a.x, a.y, offset=self.angle+180)-180)

			for sensor in self.sensors:
				sensor.detected = []
				if abs(sensor.angle-a_angle) < self.sensor_gap/2:
					sensor.detected.append(a)

		# for sensor in self.sensors:
		# 	sensor.detected = detected_agents

def main():
	display.main()

	for a in agent_list:
		display.display_agent(a)
		a.main()

	display.update_display()

if __name__ == "__main__":

	# init agents
	agent_list = []
	for i in range(48):
		new_agent = Agent(i, random.randint(0, 1280), random.randint(0, 720), random.randint(0, 360))
		agent_list.append(new_agent)

	print("Created {} agents".format(len(agent_list)))

	running = True

	while running:

		main()

		# pygame event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

	pygame.quit()
	quit()