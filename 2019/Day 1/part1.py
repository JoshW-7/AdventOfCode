

def calculate_fuel(mass):
    return mass // 3 - 2

with open("input.txt") as file:
    masses = [int(line) for line in file.readlines()]
    fuels = [calculate_fuel(mass) for mass in masses]

print(sum(fuels))