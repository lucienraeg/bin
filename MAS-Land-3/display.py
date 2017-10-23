import pygame
import math

pygame.init()
display_w, display_h = (1280, 720)
display = pygame.display.set_mode((display_w, display_h))
clock = pygame.time.Clock()

color = {"white": (255, 255, 255),
"lt_gray": (200, 200, 200),
"gray": (150, 150, 150),
"black": (0, 0, 0),
"red": (255, 0, 0),
"lime": (0, 255, 0),
"blue": (0, 0, 255)}

font = {"small": pygame.font.SysFont("couriernew", 12)}

focus = None
world_offset_x, world_offset_y = 0, 0 

dragging = False
drag_from_x, drag_from_y = 0, 0
drag_offset_x, drag_offset_y = 0, 0

def point_distance(x1, y1, x2, y2):
	return math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)

def display_info_panel(x, y, title, **info):
	y_offset = (0, 14)[title != None]
	w, h = 180, len(info)*16+8+y_offset
	value_offset = max([len(str(key)) for key in list(info)])*8+8

	pygame.draw.rect(display, color["black"], (x+2, y+2, w-4, h-4))
	pygame.draw.rect(display, color["white"], (x+2, y+2, w-4, h-4), 2)

	if title != None:
		pygame.draw.rect(display, color["white"], (x+2, y+2, w-4, 16))
		text = font["small"].render("{}".format(title), True, color["black"])
		display.blit(text, (x+7, y+4))

	for i, key in enumerate(info):
		value = info[key]
		text = font["small"].render("{}".format(key), True, color["lt_gray"])
		display.blit(text, (x+7, y+6+i*16+y_offset))

		col = color["white"]
		if type(value) == bool:
			col = (color["red"], color["lime"])[value]

		text = font["small"].render("{}".format(value), True, col)
		display.blit(text, (x+7+value_offset, y+6+i*16+y_offset))

def display_agent_panel(x, y, agents):
	global focus

	if focus == None:
		display_agent_list(x, y, agents)
	else:
		display_info_panel(x, y, "Agent #{}".format(focus.index), Pos=(focus.x, focus.y))

def display_agent_list(x, y, agents):
	global focus

	mouse_x, mouse_y = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()[0]

	w, h = 180, 50+((len(agents)-1) // 7)*24

	pygame.draw.rect(display, color["black"], (x+2, y+2, w-4, h-4))
	pygame.draw.rect(display, color["white"], (x+2, y+2, w-4, h-4), 2)

	pygame.draw.rect(display, color["white"], (x+2, y+2, w-4, 16))
	text = font["small"].render("{}".format("Agents"), True, color["black"])
	display.blit(text, (x+7, y+4))

	for i, agent in enumerate(agents):
		xx = x+7+(i % 7)*24
		yy = y+21+(i // 7)*24

		hover = xx < mouse_x < xx+22 and yy < mouse_y < yy+22

		col = (color["gray"], color["white"])[hover]
		pygame.draw.rect(display, col, (xx, yy, 22, 22), 2)

		text = font["small"].render("{}".format(agent.index), True, color["white"])
		text_rect = text.get_rect(center=(xx+11, yy+11))
		display.blit(text, text_rect)

		if hover and click:
			focus = agent

def display_agent(agent):
	global focus

	mouse_x, mouse_y = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()[0]

	a_x = agent.x+world_offset_x
	a_y = agent.y+world_offset_y

	pygame.draw.circle(display, color["white"], (a_x, a_y), 4)

	if agent == focus:
		pygame.draw.rect(display, color["red"], (a_x-8, a_y-8, 16, 16), 2)
		text = font["small"].render("{}".format(agent.index), True, color["red"])
		text_rect = text.get_rect(center=(a_x, a_y-16))
		display.blit(text, text_rect)
	else:
		if point_distance(a_x, a_y, mouse_x, mouse_y) < 8 and click:
			focus = agent

def main():
	global dragging, drag_from_x, drag_from_y, drag_offset_x, drag_offset_y, world_offset_x, world_offset_y

	display.fill(color["black"])

	# dragging
	mouse_x, mouse_y = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()[0]

	if click and not dragging and mouse_x > 180:
		drag_from_x = mouse_x
		drag_from_y = mouse_y
		dragging = 1
	if not click or mouse_x < 180:
		drag_offset_x = world_offset_x
		drag_offset_y = world_offset_y
		dragging = 0
	if dragging:
		world_offset_x = mouse_x-drag_from_x+drag_offset_x
		world_offset_y = mouse_y-drag_from_y+drag_offset_y



def update_display():
	pygame.display.set_caption("FPS: {}".format(round(clock.get_fps(), 2)))
	pygame.display.update()
	clock.tick(60)

if __name__ == "__main__":
	print(display)
	print(clock)