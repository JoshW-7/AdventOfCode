

def calculate_fuel(mass):
    fuel = mass // 3 - 2
    if fuel < 0:
        return 0
    return fuel + calculate_fuel(fuel)

with open("input.txt") as file:
    masses = [int(line) for line in file.readlines()]
    fuels = [calculate_fuel(mass) for mass in masses]

print(sum(fuels))

    