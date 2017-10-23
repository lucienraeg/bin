def wolfram_encode(line, iterations=2):
	line = [int(c) for c in list(line)]
	rule = {0: True, 1: False, 2: True, 3: False}

	print(line)

	for i in range(iterations):
		prev_line = line
		for c in range(len(line)):
			if c == 0:
				line[c] = 0
			elif c == len(line)-1:
				line[c] = 0
			else:
				n = prev_line[c]
				line[c] = n

		print(line)

a = "101110100"
b = wolfram_encode(a)