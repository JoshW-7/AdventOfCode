import re


with open("input.txt") as file:
    lines = file.read().split("\n")


def evaluate(statement):
    while not statement.isdigit():
        if m := re.search(r"[0-9]* [+] [0-9]*", statement):
            s = m.group(0)
            result = eval(s)
            statement = statement[0:statement.find(s)] + str(result) + statement[statement.find(s) + len(s):]
        else:
            break
    while not statement.isdigit():
        if m := re.search(r"[0-9]* [*] [0-9]*", statement):
            s = m.group(0)
            result = eval(s)
            statement = statement[0:statement.find(s)] + str(result) + statement[statement.find(s) + len(s):]
    return statement


results = []
for line in lines:
    while True:
        if ps := re.findall(r"\(([^)()]*)\)", line):
            for p in ps:
                new_str = evaluate(p)
                line = line[0:line.find(p)-1] + new_str + line[1 + line.find(p) + len(p):]
        else:
            break
    results.append(int(evaluate(line)))

print(sum(results))