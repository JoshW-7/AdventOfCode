

def transform(subject_number, loop_size):
    value = 1
    for i in range(loop_size):
        value *= subject_number
        value %= 20201227
    return value

card_key = 1526110
door_key = 20175123

result = 1
loop_size_1 = 0
while True:
    loop_size_1 += 1
    result *= 7
    result %= 20201227
    if result == card_key:
        break

result = 1
loop_size_2 = 0
while True:
    loop_size_2 += 1
    result *= 7
    result %= 20201227
    if result == door_key:
        break

result = transform(door_key, loop_size_1)
print(result)