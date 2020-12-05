

def get_id(seat_encoding):
    row_data = seat_encoding[0:7]
    col_data = seat_encoding[7:]

    # Get row
    low,high = (0, n_rows)
    for c in row_data:
        width = high - low
        if c == "F":
            high = low + width / 2
        elif c == "B":
            low = low + width / 2
    row = int(low)

    # Get col
    low,high = (0, n_cols)
    for c in col_data:
        width = high - low
        if c == "L":
            high = low + width / 2
        elif c == "R":
            low = low + width / 2
    col = int(low)
    
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