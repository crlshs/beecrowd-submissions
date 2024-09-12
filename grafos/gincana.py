def dfs(grafo, visitado, node):
    # cesta para visitar depois
    pilha = [node]
    while pilha:
        atual = pilha.pop()
        if atual not in visitado:
            visitado.add(atual)

        # ver as amigas de V, para visitar elas depois
        for v in grafo[atual]:
            if v not in visitado:
                pilha.append(v)

n, m = map(int, input().split())

grafo = {i : [] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    grafo[a].append(b)
    grafo[b].append(a)

visitado = set()
times = 0

for v in range(1, n+1):
    if v not in visitado:
        dfs(grafo, visitado, v)
        times += 1
print(times)