from itertools import combinations

with open("input.txt") as file:
    lines = file.read().split("\n")

memory = {}
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
for line in lines:
    if line.startswith("mask"):
        mask = line.split(" = ")[1]
    elif line.startswith("mem"):
        address = int(line[4:line.find("]")])
        value = int(line.split(" = ")[1])
        options = set()
        for i,c in enumerate(reversed(mask)):
            if c in "1X":
                if c == "1":
                    address |= (0x1 << i)
                elif c == "X":
                    options.add(i)
        combos = [c for c in combinations(options, 0)]
        for i in range(len(options)):
            combos += [c for c in combinations(options, i+1)]

        addresses = set({address})
        if len(options) > 0:
            combos = [c for c in combinations(options, 0)]
            for i in range(len(options)):
                combos.extend([c for c in combinations(options, i+1)])
            for combo in combos:
                temp_address = address
                for bit in options:
                    if bit in combo:
                        temp_address |= (0x01 << bit)
                    else:
                        temp_address &= ~(0x01 << bit)
                addresses.add(temp_address)

        for addr in addresses:
            if addr not in memory:
                memory[addr] = 0
            new_value = 0
            for i in range(36):
                new_value |= (value & (0x1 << i))
            memory[addr] = new_value

total = 0
for address in memory:
    total += memory[address]
                
print(total)
