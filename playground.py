a_base = (0, 0, 0, 0)
b = []

for d3 in range(3):
	for d2 in range(3):
		for d1 in range(3):
			for d0 in range(3):
				a = list(a_base)
				a[0] = d0-1
				a[1] = d1-1
				a[2] = d2-1
				a[3] = d3-1
				if not a == [0, 0, 0, 0]:
					b.append(tuple(a))

print(b)