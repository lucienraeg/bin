import pygame
import numpy as np
import math

pygame.init()
display_w, display_h = (1280, 720)
display = pygame.display.set_mode((display_w, display_h))
clock = pygame.time.Clock()

color = {"white": (255, 255, 255),
"lt_gray": (200, 200, 200),
"gray": (150, 150, 150),
"black": (0, 0, 0),
"red": (255, 0, 0)}

font = {"small": pygame.font.SysFont("arial", 14)}

def extend_direction(x1, y1, angle, d):
	theta_rad = np.radians(-angle)
	return x1 + d*np.cos(theta_rad), y1 + d*np.sin(theta_rad)

def point_distance(x1, y1, x2, y2):
	return np.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)

def point_direction(x1, y1, x2, y2, offset=0):
	return (180 - offset - np.rad2deg(np.arctan2(y1 - y2, x1 - x2))) % 360

def display_agent(a):
	# sensors
	for i, sensor in enumerate(a.sensors):
		col = (color["gray"], color["red"])[len(sensor.detected) > 0]
		x2, y2 = extend_direction(a.x, a.y, a.angle+sensor.angle, sensor.length)
		pygame.draw.line(display, col, (a.x, a.y), (x2, y2), (1, 2)[i == len(a.sensors) // 2])

	# body
	pygame.draw.circle(display, color["lt_gray"], (a.x, a.y), 12)
	pygame.draw.circle(display, color["black"], (a.x, a.y), 12, 2)

	# label
	text = font["small"].render("{}".format(a.index), True, color["red"])
	display.blit(text, text.get_rect(center=(a.x, a.y)))

	# debug info
	text = font["small"].render("{}".format([sensor.detected for sensor in a.sensors]), True, color["black"])
	display.blit(text, text.get_rect(center=(a.x, a.y+32)))


def main():
	display.fill(color["white"])

def update_display():
	pygame.display.set_caption("FPS: {}".format(round(clock.get_fps(), 2)))
	pygame.display.update()
	clock.tick(60)

if __name__ == "__main__":
	print(display)
	print(clock)