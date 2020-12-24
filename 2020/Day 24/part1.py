import re


with open("input.txt") as file:
    lines = file.read().split("\n")

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

tile_locations = []
for line in lines:
    tile_locations.append(parse(line))

tiles = {}
for i,moves in enumerate(tile_locations):
    x = 0
    y = 0
    for move in moves:
        x += {
            "e": 2,
            "w": -2,
            "se": 1,
            "sw": -1,
            "ne": 1,
            "nw": -1,
        }[move]
        y += {
            "e": 0,
            "w": 0,
            "se": 1,
            "sw": 1,
            "ne": -1,
            "nw": -1,
        }[move]
    
    if (x, y) not in tiles:
        tiles[(x, y)] = "white"
    color = tiles[(x, y)]
    if color == "white":
        color = "black"
    else:
        color = "white"

    print(f"Setting {(x, y)} to {color}")
    tiles[(x, y)] = color

    
black_tiles = 0
for color in tiles.values():
    if color == "black":
        black_tiles += 1
print(black_tiles)