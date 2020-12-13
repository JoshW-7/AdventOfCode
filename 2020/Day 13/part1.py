

with open("input.txt") as file:
    lines = file.read().split("\n")

departure_time = int(lines[0])
buses = [int(num) for num in lines[1].split(",") if num != "x"]
print(buses)

i = departure_time
t = -1
chosen_bus = None
counter = 0
done = False
while True:
    if done:
        break
    for bus in buses:
        if i % bus == 0:
            print("yes")
            t = i
            chosen_bus = bus
            done = True

    i += 1
    counter += 1

wait_time = t - departure_time
print(chosen_bus * wait_time)