def calc(post, posb):
    return sum(abs(post[i] - posb[i]) for i in range(len(posb)))


n = int(input())
string = input()

pos1 = [x for x in range(2 * n) if x % 2 == 1]
pos2 = [x for x in range(2 * n) if x % 2 == 0]

posb = [x for x in range(2 * n) if string[x] == "B"]


print(min(calc(pos1, posb), calc(pos2, posb)))
