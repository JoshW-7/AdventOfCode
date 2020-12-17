import math
import copy


with open("input.txt") as file:
    lines = [[c for c in line] for line in file.read().split("\n")]

cubes = {}

count = 0
for y,line in enumerate(lines):
    for x,cube in enumerate(line):
        cubes[(x, y, 0)] = cube
        count += 1

def get_neighbors(x, y, z):
    global cubes
    global next_cubes

    new_coords = set()
    relative_coords = [
        (-1, -1, -1), (0, -1, -1), (1, -1, -1), (-1, 0, -1), (0, 0, -1), (1, 0, -1), (-1, 1, -1), (0, 1, -1), (1, 1, -1),
        (-1, -1, 0), (0, -1, 0), (1, -1, 0), (-1, 0, 0), (1, 0, 0), (-1, 1, 0), (0, 1, 0), (1, 1, 0),
        (-1, -1, 1), (0, -1, 1), (1, -1, 1), (-1, 0, 1), (0, 0, 1), (1, 0, 1), (-1, 1, 1), (0, 1, 1), (1, 1, 1),
    ]
    active_neighbors = 0
    for coord in relative_coords:
        rel_coord = (x+coord[0], y+coord[1], z+coord[2])
        if rel_coord not in cubes:
            new_coords.add(rel_coord)
        if rel_coord in cubes:
            if cubes[rel_coord] == "#":
                active_neighbors += 1

    return active_neighbors, new_coords
    
def print_layer(z, cubes):

    coords = sorted([(coord[0],coord[1]) for coord in cubes if coord[2] == z])
    size = round(math.sqrt(len(coords)))
    layer = [[None for x in range(size)] for y in range(size)]
    for (x,y) in coords:
        layer[y][x] = cubes[(x, y, z)]
    for row in layer:
        print("".join(row))
    print()

cycle = 0
while cycle < 6:
    print_layer(0, cubes)
    next_cubes = copy.deepcopy(cubes)
    for (x,y,z),cube in cubes.items():
        active_neighbors, new_coords = get_neighbors(x, y, z)
        if cube == "#" and active_neighbors not in [2, 3]:
            next_cubes[(x, y, z)] = "."
        elif cube == "." and active_neighbors == 3:
            next_cubes[(x, y, z)] = "#"
        for (nx,ny,nz) in new_coords:
            next_cubes[(nx, ny, nz)] = "."
            active_neighbors, _ = get_neighbors(nx, ny, nz)
            if next_cubes[(nx, ny, nz)] == "#" and active_neighbors not in [2, 3]:
                next_cubes[(nx, ny, nz)] = "."
            elif next_cubes[(nx, ny, nz)] == "." and active_neighbors == 3:
                next_cubes[(nx, ny, nz)] = "#"

    cubes = copy.deepcopy(next_cubes)
    cycle += 1

count = 0
for cube in cubes.values():
    if cube == "#":
        count += 1

print(count)