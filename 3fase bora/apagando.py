res = []
while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0: break
    numero = list(input())

    for _ in range(d):
        numero.pop(numero.index(min(numero), -1, 0))
    res.append("".join(numero))

print("\n".join(str(i) for i in res))