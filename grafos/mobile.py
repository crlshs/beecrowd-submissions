n = int(input())

grafo = {i : [] for i in range(n+1)}
for _ in range(n):
    a, b = map(int, input().split())
    grafo[a].append(b)
    grafo[b].append(a)


def dfs(grafo, node):
    visitados = set()
    tamanhos_submobiles = {}

    pilha = [node]
    ligacoes = len(grafo[node])
    while pilha:
        atual = pilha[-1]

        if atual in visitados:
            pilha.pop()
        
        visitados.add(atual)

        tamanhos = []

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                pilha.append(vizinho)
            else:
                tamanhos.append(tamanhos_submobiles.get(vizinho, 1))

        if tamanhos and len(set(tamanhos)) > 1:
            return "mal"

        tamanhos_submobiles[atual] = sum(tamanhos) + 1

    return "bem"

print(dfs(grafo, 1))