n, r = map(int, input().split())

grafo = {i : set() for i in range(1, n+1)}

for _ in range(r):
    x, y = map(int, input().split())
    grafo[x].add(y)
    grafo[y].add(x)

contador = 0
for v in range(1, n+1):
    for p in range(v+1, n+1):
        if p not in grafo[v]:
            grafo[v].add(p)
            grafo[p].add(v)
            contador+=1

print(contador)