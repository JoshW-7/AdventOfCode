

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

my_ticket = [int(num) for num in lines[22].split(",")]

ticket_data = lines[25:]
tickets = []
for line in ticket_data:
    tickets.append([int(num) for num in line.split(",")])

invalid_nums = []
invalid_tickets = []
for ticket in tickets:
    added = False
    ticket_invalid = False
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
            ticket_invalid = True
            if ticket not in invalid_tickets:
                invalid_tickets.append(ticket)

valid_tickets = []
for ticket in tickets:
    if ticket not in invalid_tickets:
        valid_tickets.append(ticket)

names = [name for name in fields.keys()]
indexes = {name: [] for name in names}
for i in range(20):
    numbers = [ticket[i] for ticket in valid_tickets]
    for name in names:
        range_low = fields[name]["range_low"]
        range_high = fields[name]["range_high"]
        valid = True
        for num in numbers:
            if range_low[0] <= num <= range_low[1]:
                pass
            elif range_high[0] <= num <= range_high[1]:
                pass
            else:
                valid = False
        if valid:
            indexes[name].append(i)

mapping = {}
while True:
    for name,values in indexes.items():
        if len(values) == 1:
            mapping[name] = values[0]
        else:
            for value in values:
                unique = True
                for other_name,other_values in indexes.items():
                    if other_name != name:
                        for other_value in other_values:
                            if other_value == value:
                                unique = False
                                break
                    if not unique:
                        break
                if unique:
                    mapping[name] = value
                    break
    for name in mapping:
        if name in indexes:
            del indexes[name]
    if indexes == {}:
        break
            
print(my_ticket[mapping["departure track"]] * my_ticket[mapping["departure station"]] * my_ticket[mapping["departure platform"]] * my_ticket[mapping["departure location"]] * my_ticket[mapping["departure time"]] * my_ticket[mapping["departure date"]])