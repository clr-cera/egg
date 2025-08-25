array = range(1, int(input()) + 1)
if 2 <= array[-1] <= 3:
    print("NO SOLUTION")
    exit(0)
if array[-1] != 1:
    print(*array[1::2], end=" ")
print(*array[0::2], end=" ")
