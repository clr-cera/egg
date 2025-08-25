t = int(input())
for _ in range(t):
    y, x = map(int, input().split())
    if max(y, x) % 2 == 1:
        x, y = y, x
    if y > x:
        print(y**2 - x + 1)
    else:
        print((x - 1) ** 2 + y)
