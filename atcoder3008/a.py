n = int(input())

aaa = {}
for i in range(n):
    aaa[i] = input()

pair = input().split()

room = int(pair[0])
name = pair[1]


if aaa[room - 1] == name:
    print("Yes")
else:
    print("No")
