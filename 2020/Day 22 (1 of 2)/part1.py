

with open("input.txt") as file:
    lines = file.read().split("\n")
    players = {}
    current_player = None
    for line in lines:
        if line.startswith("Player"):
            current_player = int(line.split(" ")[1][0])
            players[current_player] = []
        elif len(line) > 0:
            players[current_player].append(int(line))

while True:
    if players[1][0] > players[2][0]:
        p1 = players[1].pop(0)
        players[1].append(p1)
        p2 = players[2].pop(0)
        players[1].append(p2)
    else:
        p2 = players[2].pop(0)
        players[2].append(p2)
        p1 = players[1].pop(0)
        players[2].append(p1)

    if len(players[1]) == 0 or len(players[2]) == 0:
        winner = 1 if len(players[1]) > len(players[2]) else 2
        break

winner_cards = players[winner]
score = 0
multiplier = len(winner_cards)
for i,card in enumerate(winner_cards):
    score += multiplier * card
    multiplier -= 1
print(score)