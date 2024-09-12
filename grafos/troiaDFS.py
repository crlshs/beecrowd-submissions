n, m = map(int, input().split())

grafo = {i : [] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    grafo[a].append(b)
    grafo[b].append(a)

def dfs(grafo, visitado, vertice):
    # dfs iterativo
    pilha = [vertice]

    while pilha:
        atual = pilha.pop()
        if atual not in visitado:
            visitado.add(atual)

        for vizinho in grafo[atual]:
            if vizinho not in visitado:
                pilha.append(vizinho)

visitado = set()
familias = 0

for i in range(1, n+1):
    if i not in visitado:
        dfs(grafo, visitado, i)
        familias += 1

# pilha = []
# visitados = [1, 3, 4, 2, 5, 6]
# familias = 1 + 1

print(familias)