import re


with open("input.txt") as file:
    lines = file.read().split("\n")

def evaluate(statement):

    # Evaluate addition operations
    while not statement.isdigit():

        # Look for "number + number"
        # If we can't find one, break out
        if m := re.search(r"\d* \+ \d*", statement):
            s = m.group(0)

            # Evaluate the addition operation, then substitute the result back into the whole statement
            statement = statement[0:m.start()] + str(eval(s)) + statement[m.end():]
        else:
            break

    # Evaluate multiplication operations
    while not statement.isdigit():

        # Look for "number * number"
        if m := re.search(r"\d* \* \d*", statement):
            s = m.group(0)

            # Evaluate the multiplication operation, then substitute the result back into the whole statement
            statement = statement[0:m.start()] + str(eval(s)) + statement[m.end():]
    return statement

results = []
for line in lines:
    while True:

        # Find parenthetical statements
        # If we can't find one, break out and evaluate the final non-parenthetical statement
        if ps := re.findall(r"\(([^)()]*)\)", line):
            for p in ps:

                # Evaluate the parenthetical statement, then substitute the result back into the whole statement
                new_str = evaluate(p)
                line = line[0:line.find(p)-1] + new_str + line[1 + line.find(p) + len(p):]
        else:
            break
    results.append(int(evaluate(line)))

print(sum(results))