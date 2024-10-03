n, origem, destino =  map(int, input().split())

grafo = {i : [] for i in range(1, n+1)}
distancias = {i : 0 for i in range(1, n+1)}
vals = {}

for _ in range(n - 1):
    x, y, d = map(int, input().split())
    grafo[x].append(y)
    grafo[y].append(x)

    if x > y:
        vals[(x, y)] = d
    else:
        vals[(y, x)] = d

def bfs(grafo, node):
    fila = [node]
    visitados = [node]

    while fila:
        atual = fila.pop()

        for v in grafo[atual]:
            if v not in visitados:
                if v > atual:
                    distancias[v] = distancias[atual] + vals[(v, atual)]
                else:
                    distancias[v] = distancias[atual] + vals[(atual, v)]

                fila.append(v)
                visitados.append(v)

bfs(grafo, origem)
print(distancias[destino])