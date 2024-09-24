import heapq
n, m, k = map(int, input().split())

# numero de estacoes
# numero de ligacoes
# quantidade de tipos de transportes

precos = list(map(int, input().split()))
precos = [0] + precos
# preco 1, preco 2, preco 3 etc etc

grafo = {}

def add_node(node):
    if node not in grafo:
        grafo[node] = []

def add_edge(node1, node2, custo):
    add_node(node1)
    grafo[node1].append((node2, custo))

for _ in range(m):
    v, u, t = map(int, input().split())
    add_edge((u, t), (v, t), 0)
    add_edge((v, t), (u, t), 0)

    add_edge((u, t), (u, k + 1), 0)
    add_edge((v, t), (v, k + 1), 0)

    add_edge((u, k + 1), (u, t), precos[t])
    add_edge((v, k + 1), (v, t), precos[t])

inicio, fim = map(int, input().split())

estado_inicial = (inicio, k + 1)
distancias = {estado_inicial: 0}
fila_prioridade = [(0, estado_inicial)]
heapq.heapify(fila_prioridade)
visitados = set()

while fila_prioridade:
    dist_atual, no_atual = heapq.heappop(fila_prioridade)
    if no_atual in visitados:
        continue
    visitados.add(no_atual)
    
    if no_atual in grafo:
        for vizinho, custo in grafo[no_atual]:
            nova_dist = dist_atual + custo
            if vizinho not in distancias or nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                heapq.heappush(fila_prioridade, (nova_dist, vizinho))

estado_final = (fim, k + 1)
print(distancias.get(estado_final, -1))
