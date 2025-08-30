q = int(input())

a = [0]
dicti = {0: 0}

for i in range(1, q + 1):
    tu = list(map(int, input().split()))

    if tu[0] == 1:
        for pair in dicti.items():
            if pair[1] > dicti[tu[1]]:
                dicti[pair[0]] += 1
        a.insert(dicti[tu[1]] + 1, i)
        dicti[i] = dicti[tu[1]] + 1

    elif tu[0] == 2:
        p0 = dicti[tu[1]]
        p1 = dicti[tu[2]]
        small = min(p0, p1)
        big = max(p0, p1)
        acc = 0

        for j in range(small + 1, big):
            acc += a[j]
        for j in range(big - small - 1):
            a.pop(small + 1)
        for pair in dicti.items():
            if pair[1] >= big:
                dicti[pair[0]] -= big - small - 1
        print(acc)
