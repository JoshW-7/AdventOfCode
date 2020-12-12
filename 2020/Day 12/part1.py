import math

with open("input.txt") as file:
    lines = file.read().split("\n")
    directions = [(line[0], int(line[1:])) for line in lines]


heading = "E"
start = (0, 0)
pos = [0, 0]
for letter,amount in directions:
    if letter == "N":
        pos[1] -= amount
    if letter == "S":
        pos[1] += amount
    if letter == "E":
        pos[0] += amount
    if letter == "W":
        pos[0] -= amount
    
    if letter == "L":
        for i in range(amount // 90):
            heading = {
                "N": "W",
                "S": "E",
                "E": "N",
                "W": "S",
            }[heading]
    if letter == "R":
        for i in range(amount // 90):
            heading = {
                "N": "E",
                "S": "W",
                "E": "S",
                "W": "N",
            }[heading]

    if letter == "F":
        if heading == "E":
            pos[0] += amount
        if heading == "W":
            pos[0] -= amount
        if heading == "N":
            pos[1] -= amount
        if heading == "S":
            pos[1] += amount

    print(pos)

    

print(pos)

dx = abs(pos[0] - start[0])
dy = abs(pos[1] - start[1])
print(dx + dy)