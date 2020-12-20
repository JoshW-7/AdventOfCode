

with open("input.txt") as file:
    lines = file.read().split("\n")
    rules = {}
    messages = []
    parse_messages = False
    for line in lines:
        if len(line) == 0:
            parse_messages = True
            continue
        elif parse_messages:
            messages.append(line)
        else:
            number,text = line.split(": ")
            text = text.replace('"', '')
            rules[int(number)] = text

def matches(number, text):
    global rules

    rule = rules[number]
    if "a" in rule or "b" in rule:
        if text.startswith(rule):
            return 1, ""
        return 0, ""
    else:
        options = rule.split(" | ")
        options = [[int(num) for num in option.split(" ")] for option in options]
        for option in options:
            valid = True
            text_temp = text
            length = 0
            for num in option:
                if result := matches(num, text_temp):
                    match_length,_ = result
                    if match_length == 0:
                        break
                    length += match_length
                    text_temp = text_temp[match_length:]
                else:
                    valid = False
            if valid:
                return length, text_temp
        return 0, ""


count = 0
for message in messages:
    if result := matches(0, message):
        if result[0] != 0 and result[0] < len(result[1]):
            count += 1

print(count)