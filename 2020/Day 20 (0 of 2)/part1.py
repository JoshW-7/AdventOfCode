import math
import copy

from itertools import permutations


with open("test.txt") as file:
    lines = file.read().split("\n")
    tiles = {}
    tile_data = []
    for line in lines:
        if line.startswith("Tile"):
            tile_number = int(line.split(" ")[1].rstrip(":"))
        elif len(line) == 0:
            tiles[tile_number] = tile_data
            tile_data = []
        else:
            tile_data.append(line)

size = int(math.sqrt(len(tiles)))

def print_configuration(configuration):
    global size

    for n in range(size):
        configuration_tiles = configuration[n*3:n*3+3]
        for y in range(10):
            for (tile_number,tile_data) in configuration_tiles:
                print(tile_data[y], end=" ")
            print()
        print()

def make_permutations():
    global tiles
    global size

for configuration in permutations([(tile_number,tile_data) for tile_number,tile_data in tiles.items()], r=len(tiles)):
    print_configuration(configuration)