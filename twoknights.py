diff = 0
multiplier = 0

n = int(input())

for k in range(1, n + 1):
    if k == 1:
        print(0)
        continue

    multiplier += diff
    combinations = (k * k) * ((k * k) - 1) / 2
    bad_combinations = 8 * multiplier
    diff += 1
    result = combinations - bad_combinations

    print(int(result))

