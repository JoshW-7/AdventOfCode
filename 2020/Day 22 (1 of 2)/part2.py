

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

rounds = set()
while True:
    round_hash = hash((str(players[1]), str(players[2])))
    if round_hash in rounds:
        winner = 1
        break
    rounds.add(round_hash)

    p1 = players[1].pop(0)
    p2 = players[2].pop(0)

    p1_recurse = False
    p2_recurse = False
    if len(players[1]) >= p1:
        p1_recurse = True
    if len(players[2]) >= p2:
        p2_recurse

    if p1_recurse and p2_recurse:
        pass
    else:
        if p1_recurse:
            winner = 1
            break
        else:
            winner = 2



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