tu = list(map(int, input().split()))

takashi = (tu[1], tu[0])
aoki = (tu[3], tu[2])

n, m, L = map(int, input().split())

takashi_moves = []
for _ in range(m):
    name, quantity = input().split()
    takashi_moves.append((name, int(quantity)))

aoki_moves = []
for _ in range(L):
    name, quantity = input().split()
    aoki_moves.append((name, int(quantity)))

acc = 0
while True:
    aoki_final = aoki
    takashi_final = takashi
    moves = min(aoki_moves[0][1], takashi_moves[0][1])
    if aoki_moves[0][1] > takashi_moves[0][1]:
        if takashi_moves[0][0] == "U":
            takashi_final = (takashi_final[0], takashi_final[1] - takashi_moves[0][1])
        elif takashi_moves[0][0] == "D":
            takashi_final = (takashi_final[0], takashi_final[1] + takashi_moves[0][1])
        elif takashi_moves[0][0] == "L":
            takashi_final = (takashi_final[0] - takashi_moves[0][1], takashi_final[1])
        elif takashi_moves[0][0] == "R":
            takashi_final = (takashi_final[0] + takashi_moves[0][1], takashi_final[1])
        if aoki_moves[0][0] == "U":
            aoki_final = (aoki_final[0], aoki_final[1] - takashi_moves[0][1])
        elif aoki_moves[0][0] == "D":
            aoki_final = (aoki_final[0], aoki_final[1] + takashi_moves[0][1])
        elif aoki_moves[0][0] == "L":
            aoki_final = (aoki_final[0] - takashi_moves[0][1], aoki_final[1])
        elif aoki_moves[0][0] == "R":
            aoki_final = (aoki_final[0] + takashi_moves[0][1], aoki_final[1])

        aoki_moves[0][1] -= takashi_moves[0][1]
        takashi_moves.pop(0)

    if aoki_moves[0][1] < takashi_moves[0][1]:
        if takashi_moves[0][0] == "U":
            takashi_final = (takashi_final[0], takashi_final[1] - aoki_moves[0][1])
        elif takashi_moves[0][0] == "D":
            takashi_final = (takashi_final[0], takashi_final[1] + aoki_moves[0][1])
        elif takashi_moves[0][0] == "L":
            takashi_final = (takashi_final[0] - aoki_moves[0][1], takashi_final[1])
        elif takashi_moves[0][0] == "R":
            takashi_final = (takashi_final[0] + aoki_moves[0][1], takashi_final[1])
        if aoki_moves[0][0] == "U":
            aoki_final = (aoki_final[0], aoki_final[1] - aoki_moves[0][1])
        elif aoki_moves[0][0] == "D":
            aoki_final = (aoki_final[0], aoki_final[1] + aoki_moves[0][1])
        elif aoki_moves[0][0] == "L":
            aoki_final = (aoki_final[0] - aoki_moves[0][1], aoki_final[1])
        elif aoki_moves[0][0] == "R":
            aoki_final = (aoki_final[0] + aoki_moves[0][1], aoki_final[1])

    if takashi == aoki:
        if takashi_final == aoki_final:
            acc += moves
        else:
            acc += 1
    else:
        if aoki[0] == aoki_final[0]:
            takashi_range = sorted([takashi[1], takashi_final[1]])
            aaaaaaaa

    aoki = aoki_final
    takashi = takashi_final
