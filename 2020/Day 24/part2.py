import re
import copy


def parse(text):
    moves = []
    while len(text) > 0:
        if m := re.match(r"([e|w]{1})", text):
            moves.append(m.group(1))
            text = text[m.end():]
        elif m := re.match(r"([se|sw|ne|nw]{2})", text):
            moves.append(m.group(1))
            text = text[m.end():]
    return moves

def setup():
    global tiles

    for moves in tile_locations:
        x = 0
        y = 0
        for move in moves:
            dx,dy = {
                "ne": (0, -1),
                "e": (1, 0),
                "se": (1, 1),
                "sw": (-1, 1),
                "w": (-1, 0),
                "nw": (-1, -1),
            }[move]
            x += dx
            y += dy
        
        if (x, y) not in tiles:
            tiles[(x, y)] = "white"
        
        if tiles[(x, y)] == "white":
            tiles[(x, y)] = "black"
        else:
            tiles[(x, y)] = "white"

def get_adjacent(x, y):
    global tiles

    relative_coords = [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)]
    neighbors = []
    for relative_coord in relative_coords:
        neighbors.append((x + relative_coord[0], y + relative_coord[1]))
    return neighbors

def count_black():
    global tiles

    count = 0
    for color in tiles.values():
        if color == "black":
            count += 1
    return count

with open("input.txt") as file:
    lines = file.read().split("\n")

tile_locations = []
for line in lines:
    tile_locations.append(parse(line))   
tiles = {}
setup()

print(f"Day 0: {count_black()}")
for day in range(1, 101):
    changes = {}
    new_tiles = []

    for (x,y),color in tiles.items():
        black_count = 0
        for coord in get_adjacent(x, y):
            if coord not in tiles:
                new_tiles.append(coord)
            else:
                if tiles[coord] == "black":
                    black_count += 1
        
        if color == "white" and black_count == 2:
            changes[(x, y)] = "black"

        if color == "black":
            if black_count == 0 or black_count > 2:
                changes[(x, y)] = "white"

    for new_coord in new_tiles:
        tiles[new_coord] = "white"
        black_count = 0
        for coord in get_adjacent(x, y):
            if coord in tiles and tiles[coord] == "black":
                black_count += 1

        if black_count == 2:
            changes[new_coord] = "black"

    for coord,color in changes.items():
        tiles[coord] = color

    print(f"Day {day}: {count_black()}")