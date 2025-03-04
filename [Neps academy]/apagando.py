res = []
while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0: break
    numero = list(input())
    pilha = []

    for i in numero:
        while d > 0 and pilha and pilha[-1] < i:
            pilha.pop()
            d -= 1
        pilha.append(i)

    final = pilha[:len(pilha) - d]

    res.append("".join(final))

print("\n".join(res), end="")