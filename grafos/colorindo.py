n, m, x, y, k = map(int, input().split())

x -= 1
y -= 1

matriz = [[0] * m for _ in range(n)]

inicio = matriz[x][y]

for _ in range(k):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    matriz[a][b] = 1

def get_vizinhas(x, y):
    direita, esquerda, cima, baixo = None, None, None, None
    if y+1 < m: direita = (x, y+1)
    if y-1 >= 0: esquerda = (x, y-1)

    if x+1 < n: baixo = (x+1, y)
    if x-1 >= 0: cima = (x-1, y)

    diagonaldb, diagonaldc, diagonaleb, diagonalec = None, None, None, None

    if y+1 < m and x+1 < n: diagonaldb = (x+1, y+1)
    if y+1 < m and x-1 >= 0: diagonaldc = (x-1, y+1)

    if y-1 >= 0 and x+1 < n: diagonaleb = (x+1, y-1)
    if y-1 >= 0 and x-1 >= 0: diagonalec = (y-1, x-1)

    return [i for i in [direita, esquerda, cima, baixo, diagonaldb, diagonaldc, diagonaleb, diagonalec] if i is not None]

def dfs(matriz, visitados, x, y):
    pilha = [(x, y)]
    vezes = 0

    while pilha:
        atual = pilha.pop()
        if atual not in visitados:
            visitados.add(atual)
            vezes += 1

        vizinhas = get_vizinhas(atual[0], atual[1])

        for v in vizinhas:
            if matriz[v[0]][v[1]] == 0 and v not in visitados:
                pilha.append(v)

    return vezes

visitados = set()
print(dfs(matriz, visitados, x, y))