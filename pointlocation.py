t = int(input())

for _ in range(t):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())

    ini = (x1, y1)
    vec1 = (x2 - x1, y2 - y1)
    vec2 = (x3 - x1, y3 - y1)

    cross_product = vec1[0] * vec2[1] - vec1[1] * vec2[0]

    if cross_product == 0:
        print("TOUCH")
    elif cross_product > 0:
        print("LEFT")
    else:
        print("RIGHT")
