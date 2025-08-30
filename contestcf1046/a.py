t = int(input())


def check(x, y):
    bigger = max(x, y)
    smaller = min(x, y)

    if bigger == 0 or smaller >= (bigger - 1) // 2:
        return True
    return False


for _ in range(t):
    a, b, c, d = map(int, input().split())
    c -= a
    d -= b

    if check(a, b) and check(c, d):
        print("Yes")
    else:
        print("No")
