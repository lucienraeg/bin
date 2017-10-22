import pygame
import random
import agents
import display

def main():
	display.main()

	for agent in agent_list:
		display.display_agent(agent)

	display.display_info_panel(0, 0, None, FPS=round(display.clock.get_fps(), 2), Paused=paused, 
		MousePos=tuple(pygame.mouse.get_pos()), Offset=(display.world_offset_x, display.world_offset_y))
	display.display_agent_panel(0, 72, agent_list)

	display.update_display()

if __name__ == "__main__":
	agent_list = []
	for i in range(35):
		new_agent = agents.Agent(i, random.randint(0, 1280), random.randint(0, 1280))
		agent_list.append(new_agent)
	print("{} agents created".format(len(agent_list)))

	running = True
	paused = False

	while running:

		main()

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					paused = (True, False)[paused]
				if event.key == pygame.K_ESCAPE:
					display.focus = None
			if event.type == pygame.QUIT:
				running = False

	pygame.quit()
	quit()