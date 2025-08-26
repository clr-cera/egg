from collections import defaultdict

n = int(input())

all = (n + 1) * (n / 2)
if all % 2 == 1:
    print("NO")
    exit(0)
else:
    print("YES")

half = int(all // 2)

acc = 0
accvector = defaultdict()

for i in range(n, 0, -1):
    if half - acc >= i:
        acc += i
        accvector[i] = True

    else:
        if half - acc > 0:
            accvector[half - acc] = True
            acc += half - acc
        break

print(len(accvector.keys()))
print(*accvector.keys())

print(n - len(accvector))

for i in range(1, n + 1):
    if i not in accvector:
        print(i, end=" ")
