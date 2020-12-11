from copy import deepcopy


with open("input.txt") as file:
    lines = file.read().split("\n")
    seats = [[c for c in line] for line in lines]
    seats.append(["." for i in range(len(seats[0]))])
    seats.insert(0, ["." for i in range(len(seats[0]))])
    for row in seats:
        row.insert(0, ".")
        row.append(".")

changed = True
while changed:
    changed = False
    new_seats = deepcopy(seats)
    for y,row in enumerate(seats):
        for x,seat in enumerate(row):
            if seat == "L":
                if seats[y-1][x-1] != "#" and seats[y-1][x] != "#" and seats[y-1][x+1] != "#" and seats[y+1][x-1] != "#" and seats[y+1][x] != "#" and seats[y+1][x+1] != "#" and seats[y][x-1] != "#" and seats[y][x+1] != "#":
                    changed = True
                    new_seats[y][x] = "#"
            elif seat == "#":
                count = 0
                for s in [seats[y-1][x-1], seats[y-1][x], seats[y-1][x+1], seats[y+1][x-1], seats[y+1][x], seats[y+1][x+1], seats[y][x-1], seats[y][x+1]]:
                    if s == "#":
                        count += 1
                if count >= 4:
                    changed = True
                    new_seats[y][x] = "L"
    seats = new_seats


count = 0
for y,row in enumerate(seats):
    for x,seat in enumerate(row):
        if seat == "#":
            count += 1

print(count)