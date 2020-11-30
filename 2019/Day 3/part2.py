

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

def get_closest_intersection(crossings):
    shortest = None
    index = None
    for i,crossing in enumerate(crossings):
        d = manhattan_distance(crossing)
        if shortest is None or d < shortest:
            shortest = d
            index = i
    return crossing

def calculate_delay(crossing, wire):
    position = [0, 0]
    history = []
    delay = 0
    for move in wire:
        movement = relative_coordinates(move)
        if movement[0]:
            for x in range(1, abs(movement[0])+1):
                if movement[0] < 0:
                    x *= -1
                history.append((position[0]+x, position[1]))
                delay += 1
                if history[-1] == crossing:
                    return delay
        elif movement[1]:
            for y in range(1, abs(movement[1])+1):
                if movement[1] < 0:
                    y *= -1
                history.append((position[0], position[1]+y))
                delay += 1
                if history[-1] == crossing:
                    return delay
        
        position[0] += movement[0]
        position[1] += movement[1]

with open("input.txt") as file:
    wires = []
    for line in file.readlines():
        wires.append(line.replace("\n", "").split(","))

coordinates = {}
crossings = []
create_wire(wires[0], "w1")
create_wire(wires[1], "w2")

delay_data = {"w1": {}, "w2": {}, "total": {}}
for crossing in crossings:
    delay_data["w1"][crossing] = calculate_delay(crossing, wires[0])
    delay_data["w2"][crossing] = calculate_delay(crossing, wires[1])
    delay_data["total"][crossing] = delay_data["w1"][crossing] + delay_data["w2"][crossing]

# Get minimum delay intersection
shorest_delay = None
shorest_crossing = None
for crossing,delay in delay_data["total"].items():
    if shorest_delay is None or delay < shorest_delay:
        shorest_delay = delay
        shorest_crossing = crossing

print(shorest_delay)

