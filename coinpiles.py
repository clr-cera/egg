t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    bigger = max(a, b)
    smaller = min(a, b)

    smaller -= bigger - smaller

    if smaller < 0 or smaller % 3 != 0:
        print("NO")
    else:
        print("YES")
