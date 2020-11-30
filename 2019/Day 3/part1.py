

def relative_coordinates(move):
    return {
        "L": (-1*int(move[1:]), 0),
        "R": (int(move[1:]), 0),
        "U": (0, -1*int(move[1:])),
        "D": (0, int(move[1:])),
    }.get(move[0])

def create_wire(wire, name):
    global coordinates
    global crossings

    position = [0, 0]
    for move in wire:
        movement = relative_coordinates(move)
        if movement[0]:
            for x in range(1, abs(movement[0])+1):
                if movement[0] < 0:
                    x *= -1
                current_value = coordinates.get((position[0]+x, position[1]))
                if current_value not in [None, name]:
                    crossings.append((position[0]+x, position[1]))
                coordinates[(position[0]+x, position[1])] = name
        elif movement[1]:
            for y in range(1, abs(movement[1])+1):
                if movement[1] < 0:
                    y *= -1
                current_value = coordinates.get((position[0], position[1]+y))
                if current_value not in [None, name]:
                    crossings.append((position[0], position[1]+y))
                coordinates[(position[0], position[1]+y)] = name
        position[0] += movement[0]
        position[1] += movement[1]

def manhattan_distance(coordinate):
    return abs(coordinate[0]) + abs(coordinate[1])

with open("input.txt") as file:
    wires = []
    for line in file.readlines():
        wires.append(line.split(","))

coordinates = {}
crossings = []
create_wire(wires[0], "w1")
create_wire(wires[1], "w2")

print(min([manhattan_distance(coordinate) for coordinate in crossings]))