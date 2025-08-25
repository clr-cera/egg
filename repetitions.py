# CSES repetitions
last = " "
maxv = 0
count = 0
for c in input():
    if c == last:
        count += 1
    else:
        maxv = max(maxv, count)
        count = 1
        last = c

print(max(maxv, count))
