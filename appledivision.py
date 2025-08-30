from itertools import combinations

n = int(input())
numbers = list(map(int, input().split()))

if n == 1:
    print(numbers[0])
    exit(0)

total = sum(numbers)
best_result = float("inf")
for i in range(1, n // 2 + 1):
    for comb in combinations(numbers, i):
        current_sum = sum(comb)
        best_result = min(best_result, abs(total - 2 * current_sum))
print(best_result)
