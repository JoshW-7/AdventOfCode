

with open("input.txt") as file:
    lines = file.read().split("\n")


fields = {}
i = 0
while lines[i] != "":
    name,data = lines[i].split(": ")
    range_low,range_high = data.split(" or ")
    range_low = [int(range_low.split("-")[0]), int(range_low.split("-")[1])]
    range_high = [int(range_high.split("-")[0]), int(range_high.split("-")[1])]
    fields[name] = {
        "range_low": range_low,
        "range_high": range_high,
    }
    i += 1

my_ticket = [int(num) for num in lines[22].split(",")] # 22

ticket_data = lines[25:] # 25
tickets = []
for line in ticket_data:
    tickets.append([int(num) for num in line.split(",")])

invalid_nums = []
for ticket in tickets:
    for num in ticket:
        valid = False
        for field,data in fields.items():
            range_low = data["range_low"]
            range_high = data["range_high"]
            if range_low[0] <= num <= range_low[1]:
                valid = True
            if range_high[0] <= num <= range_high[1]:
                valid = True
        if not valid:
            invalid_nums.append(num)

print(sum(invalid_nums))

# 654442