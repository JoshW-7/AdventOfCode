

def get_orbits(m):
    if orbit_map[m] == "COM":
        return 1
    else:
        return 1 + get_orbits(orbit_map[m])

with open("input.txt") as file:
    orbits = [orbit.rstrip("\n") for orbit in file.readlines()]
    orbit_map = {}
    for orbit in orbits:
        M,m = orbit.split(")")
        orbit_map[m] = M

    count = 0
    for m in orbit_map:
        count += get_orbits(m)

print(count)