n = int(input())

points = []
for _ in range(n):
    point = tuple(map(int, input().split()))
    points.append(point)

points = sorted(points)

if len(points) <= 1:
    print(len(points))
    print(points[0][0], points[0][1])
    exit(0)

lower = []
upper = []


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


for p in points:
    while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
        lower.pop()
    lower.append(p)

for p in reversed(points):
    while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
        upper.pop()
    upper.append(p)


lower.pop()
upper.pop()


convex_hull = lower + upper

print(len(convex_hull))
for point in convex_hull:
    print(point[0], point[1])
