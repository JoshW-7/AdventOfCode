

with open("input.txt") as file:
    lines = file.read().split("\n")
    seats = [[c for c in line] for line in lines]
    seats.append(["." for i in range(len(seats[0]))])
    seats.insert(0, ["." for i in range(len(seats[0]))])
    for row in seats:
        row.insert(0, ".")
        row.append(".")


def get_visible_occupied(x, y):
    global seats

    occupied = 0

    # Left
    done = False
    for i in reversed(range(0, x)):
        if done:
            break
        if seats[y][i] == "#":
            occupied += 1
            done = True
        elif seats[y][i] == "L":
            done = True

    # Right
    done = False
    for i in range(x+1, len(row)):
        if done:
            break
        if seats[y][i] == "#":
            occupied += 1
            done = True
        elif seats[y][i] == "L":
            done = True

    # Up
    done = False
    for j in reversed(range(0, y)):
        if done:
            break
        if seats[j][x] == "#":
            occupied += 1
            done = True
        elif seats[j][x] == "L":
            done = True

    # Down
    done = False
    for j in range(y+1, len(seats)):
        if done:
            break
        if seats[j][x] == "#":
            occupied += 1
            done = True
        elif seats[j][x] == "L":
            done = True

    # Left-Up
    i = x - 1
    j = y - 1
    done = False
    while not done and i >= 0 and j >= 0:
        if not done and seats[j][i] == "#":
            occupied += 1
            done = True
        elif seats[j][i] == "L":
            done = True
        i -= 1
        j -= 1

    # Right-Up
    i = x + 1
    j = y - 1
    done = False
    while not done and i < len(row) and j >= 0:
        if not done and seats[j][i] == "#":
            occupied += 1
            done = True
        elif seats[j][i] == "L":
            done = True
        i += 1
        j -= 1

    # Right-Down
    i = x + 1
    j = y + 1
    done = False
    while not done and i < len(row) and j < len(seats):
        if not done and seats[j][i] == "#":
            occupied += 1
            done = True
        elif seats[j][i] == "L":
            done = True
        i += 1
        j += 1

    # Left-Down
    i = x - 1
    j = y + 1
    done = False
    while not done and i >= 0 and j < len(seats):
        if not done and seats[j][i] == "#":
            occupied += 1
            done = True
        elif seats[j][i] == "L":
            done = True
        i -= 1
        j += 1

    return occupied

changed = True
while changed:
    changed = False
    changes = set()
    for y,row in enumerate(seats):
        for x,seat in enumerate(row):
            if seat == "#":
                occupied = get_visible_occupied(x, y)
                if occupied >= 5:
                    changes.add(((y,x), "L"))
                    changed = True
            elif seat == "L":
                occupied = get_visible_occupied(x, y)
                if occupied == 0:
                    changes.add(((y,x), "#"))
                    changed = True

    for change in changes:
        pos,value = change
        seats[pos[0]][pos[1]] = value

count = 0
for y,row in enumerate(seats):
    for x,seat in enumerate(row):
        if seat == "#":
            count += 1

print(count)