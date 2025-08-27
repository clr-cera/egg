from collections import defaultdict

idk_dict = defaultdict(int)
for c in input():
    idk_dict[c] += 1

even_count = 0
even_char = ""
for k, v in idk_dict.items():
    if v % 2 == 1:
        even_count += 1
        if even_count > 1:
            print("NO SOLUTION")
            exit()
        even_char = k

other_dict = {k: v // 2 for k, v in idk_dict.items()}

print(
    "".join(k * v for k, v in sorted(other_dict.items()))
    + even_char
    + "".join(k * v for k, v in sorted(other_dict.items(), reverse=True))
)
