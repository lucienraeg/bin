import pygame
import random
import agents
import display

def main():
	general_info = {"paused": paused}
	display.main(general_info)

	display.display_agent_panel(0, 56, agent_list)

	display.update_display()

if __name__ == "__main__":
	agent_list = []
	for i in range(35):
		new_agent = agents.Agent(i, random.randint(0, 16), random.randint(0, 16))
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