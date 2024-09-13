n = int(input())

grafo = {i : [] for i in range(n+1)}
for _ in range(n):
    a, b = map(int, input().split())
    grafo[a].append(b)
    grafo[b].append(a)

def dfs(grafo, visitado, vertice):
    pilha = [vertice]

    while pilha:
        atual = pilha.pop()

        vizinhos = grafo[atual]
        # [5, 6]
        if len(vizinhos) > 2:
            vizinhos = vizinhos[1:]
            # print(atual, "a", vizinhos)
            numfilhos = len(grafo[vizinhos[0]])
            # print(vizinhos[0], " - ", numfilhos, " - ", grafo[vizinhos[0]])

            for filho in range(1, len(vizinhos)):
                numfilhosdois = len(grafo[vizinhos[filho]])

                # print(vizinhos[filho], " - ", numfilhosdois, " - ", grafo[vizinhos[filho]], "b")

                # print(f"{atual} - {vizinhos} - {numfilhos} - {numfilhosdois}")

                if numfilhosdois != numfilhos: return "mal"

        if atual not in visitado:
            visitado.add(atual)

        for v in grafo[atual]:
            if v not in visitado:
                pilha.append(v)
    return "bem"

visitado = set()

print(dfs(grafo, visitado, 0))