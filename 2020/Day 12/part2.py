import math

with open("input.txt") as file:
	lines = file.read().split("\n")
	directions = [(line[0], int(line[1:])) for line in lines]

heading = "E"
marker = [10, -1]
pos = [0, 0]
for letter,amount in directions:

	if letter == "N":
		marker[1] -= amount
	if letter == "S":
		marker[1] += amount
	if letter == "E":
		marker[0] += amount
	if letter == "W":
		marker[0] -= amount
	
	if letter == "F":
		for i in range(amount):
			dx = marker[0] - pos[0]
			dy = marker[1] - pos[1]
			pos[0] += dx
			pos[1] += dy
			marker[0] += dx
			marker[1] += dy

	if letter == "L":
		for i in range(amount // 90):
			dx = marker[0] - pos[0]
			dy = marker[1] - pos[1]
			marker[0] = pos[0] - (-1 * dy)
			marker[1] = pos[1] - (dx)

	if letter == "R":
		for i in range(amount // 90):
			dx = marker[0] - pos[0]
			dy = marker[1] - pos[1]
			marker[0] = pos[0] - dy
			marker[1] = pos[1] - (-1 * dx)

dx = abs(pos[0] - 0)
dy = abs(pos[1] - 0)
print(dx + dy)