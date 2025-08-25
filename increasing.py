_ = input()

acc = 0
array = list(map(int, input().split()))
for idx, x in enumerate(array):
    if idx == 0:
        continue

    if x < array[idx - 1]:
        acc += array[idx - 1] - x
        array[idx] = array[idx - 1]

print(acc)
