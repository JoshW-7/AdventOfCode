

def get_id(seat_encoding):
    row_data = seat_encoding[0:7]
    col_data = seat_encoding[7:]

    # Get row
    row = 0
    for i,c in enumerate(reversed(row_data)):
        if c == "B":
            row |= 1 << i

    # Get col
    col = 0
    for i,c in enumerate(reversed(col_data)):
        if c == "R":
            col |= 1 << i
    
    return row * 8 + col

with open("input.txt") as file:
    lines = file.read().split("\n")

n_rows = 128
n_cols = 8
seats = []
for line in lines:
    seat = get_id(line)
    seats.append(seat)

minimum = min(seats)
for i in range(len(seats)):
    if i > minimum:
        if i not in seats:
            print(i)
            break