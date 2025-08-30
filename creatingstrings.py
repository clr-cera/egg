from math import factorial
from itertools import permutations


string = input()
n = len(string)
permutation_num = factorial(n)
for c in set(string):
    permutation_num //= factorial(string.count(c))

print(permutation_num)
sorted_string = sorted(string)
p = set()

for possibility in permutations(sorted_string):
    perm = "".join(possibility)
    if perm not in p:
        p.add(perm)
        print(perm)
