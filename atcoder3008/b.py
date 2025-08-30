def f(x):
    return int("".join(list(reversed(str(x)))))


x, y = map(int, input().split())

lista = [x, y]

for i in range(2, 10):
    lista.append(f(lista[i - 1] + lista[i - 2]))

print(lista[9])
