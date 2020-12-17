import math
import time
import copy
from itertools import product

dimension = 4

with open("input.txt") as file:
    lines = [[c for c in line] for line in file.read().split("\n")]

    cubes = {}
    for y,line in enumerate(lines):
        for x,cube in enumerate(line):
            cubes[(x, y, *(0 for i in range(dimension-2)))] = cube

relative_coords = [coord for coord in product([-1, 0, 1], repeat=dimension) if coord != (0, *(0 for i in range(dimension-1)))]

def get_neighbors(*coords):
    global cubes
    global next_cubes
    global relative_coords
    global dimension

    new_coords = set()
    active_neighbors = 0
    for coord in relative_coords:
        rel_coord = (coords[0]+coord[0], *(coords[i]+coord[i] for i in range(1, dimension)))
        if rel_coord not in cubes:
            new_coords.add(rel_coord)
        if rel_coord in cubes:
            if cubes[rel_coord] == "#":
                active_neighbors += 1

    return active_neighbors, new_coords

cycle = 0
while cycle < 6:
    next_cubes = copy.deepcopy(cubes)
    for coords,cube in cubes.items():
        active_neighbors, new_coords = get_neighbors(*coords)
        if cube == "#" and active_neighbors not in [2, 3]:
            next_cubes[coords] = "."
        elif cube == "." and active_neighbors == 3:
            next_cubes[coords] = "#"
        for new_coord in new_coords:
            next_cubes[new_coord] = "."
            active_neighbors, _ = get_neighbors(*new_coord)
            if next_cubes[new_coord] == "#" and active_neighbors not in [2, 3]:
                next_cubes[new_coord] = "."
            elif next_cubes[new_coord] == "." and active_neighbors == 3:
                next_cubes[new_coord] = "#"

    cubes = next_cubes
    cycle += 1

count = 0
for cube in cubes.values():
    if cube == "#":
        count += 1

print(count)