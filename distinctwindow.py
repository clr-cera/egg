n = int(input())

arv = []


string = input()
arv = list(map(int, string.split()))


fp = 0

same = {}
maximum = 0
spout = 0
for sp in range(len(arv)):
    if arv[sp] not in same.keys():
        same[arv[sp]] = sp
        maximum = max(maximum, sp - fp + 1)

    else:
        maximum = max(maximum, sp - same[arv[sp]])
        final_index = same[arv[sp]]
        while fp < final_index + 1:
            same.pop(arv[fp])
            fp += 1
        same[arv[sp]] = sp
    spout = sp


maximum = max(maximum, spout - fp + 1)

print(maximum)
